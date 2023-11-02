import os

def procesar_definicion(content):
    # Función para procesar el bloque de definición
    # Busca el inicio y final del bloque DEF-INI ... DEF-END
    if "DEF-INI" not in content or "DEF-END" not in content:
        return content

    dentro_def = False
    ignore_block = False  # Variable para decidir si se ignora el bloque o no
    new_content = []
    bloque_definicion = []

    for line in content:
        if "COMANDO DEF-INI" in line:  # Si encontramos "COMANDO DEF-INI", marcamos para ignorar el bloque
            ignore_block = True
            continue

        if line == "DEF-INI":
            if ignore_block:  # Si está marcado para ignorar, continuamos
                continue

            dentro_def = True
            continue
        elif line == "DEF-END":
            if ignore_block:  # Si está marcado para ignorar, restablecemos la bandera y continuamos
                ignore_block = False
                continue

            dentro_def = False

            # Procesa el bloque de definición y agrega al new_content
            if len(bloque_definicion) == 6:  # Asegura que haya 6 líneas
                new_content.append("-")
                new_content.append("- **Actores:** " + bloque_definicion[0])
                new_content.append("-")
                new_content.append("- **Descripción:** " + bloque_definicion[1])
                new_content.append("-")
                new_content.append("- **Pre condiciones:** " + bloque_definicion[2])
                new_content.append("-")
                new_content.append("- **Post condiciones:** " + bloque_definicion[3])
                new_content.append("-")
                new_content.append("- **Fecha de creación:** " + bloque_definicion[4])
                new_content.append("-")
                new_content.append("- **Fecha de actualización:** " + bloque_definicion[5])
                new_content.append("-")
                new_content.append("-")
            else:
                print("Error: el bloque DEF-INI ... DEF-END no tiene 7 líneas.")

            bloque_definicion = []
        elif dentro_def:
            bloque_definicion.append(line)
        else:
            new_content.append(line)
    # print(new_content)
    return new_content

def generar_y_guardar_archivo(nf_blocks, ruta_destino):
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)

    for block in nf_blocks:
        if 'filename' not in block or not block['content']:
            continue
        
        filepath = os.path.join(ruta_destino, block['filename'])  # Construye la ruta completa del archivo
        try:
            with open(filepath, 'w') as file:
                for linea in block['content']:
                    file.write(linea + "\n")
            print(f"Archivo {filepath} generado con éxito!")
        except Exception as e:
            print(f"No se pudo crear el archivo {filepath}. Razón: {e}")


def procesar_comandos(archivo_entrada):
    with open(archivo_entrada, 'r') as file:
        lines = file.readlines()

    nf_blocks = []  # Una lista para almacenar los bloques de contenido entre NF y WR
    current_block = {}
    block_content = []

    for line in lines:
        line = line.strip()

        if line == "NF":
            # Iniciar un nuevo bloque
            current_block = {}
            block_content = []
            continue
        elif line.startswith("NFNA-"):
            # Establecer el nombre del archivo
            filename = line.split('NFNA-')[1] + '.md'
            current_block['filename'] = filename
            continue
        elif line == "WR":
            # Cerrar el bloque actual y agregarlo a la lista de bloques
            current_block['content'] = block_content.copy()
            nf_blocks.append(current_block)
            continue

        # Añadir contenido al bloque
        block_content.append(line)

    return nf_blocks

def procesar_linea(linea):
    partes = linea.split('-')
    
    # Verificación de la longitud de partes
    if len(partes) < 3:
        print(f"Error en la línea: {linea}")  # Imprimir la línea problemática
        return None, None, None, None

    tipo = partes[1]
    accion = partes[2]
    clave = partes[3]
    texto1 = partes[4] if len(partes) > 4 else ''
    texto2 = partes[5] if len(partes) > 5 else ''

    # Cambiar el texto de la acción según los comandos
    if accion == "MUE":
        accion = "«" + clave + "» Muestra"
    elif accion == "ING":
        accion = "«" + clave + "» Ingresa"
    elif accion == "EJE":
        accion = "«" + clave + "» Ejecuta"
    elif accion == "SEL":
        accion = "«" + clave + "» Selecciona"
    elif accion == "EVA":
        accion = "«" + clave + "» Evalúa"
    elif accion == "CAR":
        accion = "«" + clave + "» Carga"
    elif accion == "RED":
        accion = "«" + clave + "» Redirige a"
    elif accion == "CLO":
        accion = "«" + clave + "» Cierra"
    elif accion == "VIE1":
        accion = "«" + clave + "» Viene de"
    elif accion == "WAI":
        accion = "«" + clave + "» Espera acción de usuario"
        texto1 = ''

    return tipo, accion, texto1, texto2

def generar_tabla_from_content(content):
    tabla = []
    en_tabla = False
    en_tabla_codigo = False
    buffer_actor = None

    for line in content:
        line = line.strip()

        if not line:  # Ignorar líneas vacías
            continue

        # Ignorar líneas que no se deben procesar como tabla
        if line.startswith("#") or line.startswith("##") or line.startswith("###") or line.startswith("####") or line.startswith("**") or line.startswith("- ")  or line.startswith("-"):
            tabla.append("") if line == "-" else tabla.append(line)
            continue

        if line.startswith("//"):  # Ignorar comentarios
            continue
        elif line.startswith("FB-"):
            nombre = line.split('-')[1]
            tabla.append(f"### FLUJO BÁSICO: {nombre}\n")
            tabla.append("")
            continue
        elif line.startswith("FC-"):
            nombre = line.split('-')[1]
            tabla.append(f"### FLUJO CÓDIGO: {nombre}\n")
            tabla.append("")
            continue
        elif line.startswith("FG-"):
            texto1 = line.split('-')[1]
            texto2 = line.split('-')[2]
            tabla.append(f"### FLUJO {texto1}: {texto2}\n")
            tabla.append("")
            continue
        elif line.startswith("#-"):
            texto = line.split('-')[1]
            tabla.append(f"# {texto}\n")
            tabla.append("")
            continue
        elif line.startswith("##-"):
            texto = line.split('-')[1]
            tabla.append(f"## {texto}\n")
            tabla.append("")
            continue
        elif line.startswith("###-"):
            texto = line.split('-')[1]
            tabla.append(f"### {texto}\n")
            tabla.append("")
            continue
        elif line.startswith("####-"):
            texto = line.split('-')[1]
            tabla.append(f"#### {texto}\n")
            tabla.append("")
            continue
        elif line.startswith("IMG-"):
            texto1 = line.split('-')[1]
            texto2 = line.split('-')[2]
            tabla.append("")
            tabla.append(f"![{texto1}]({texto2})\n")
            tabla.append("")
            continue
        
        elif line == "NC":
            en_tabla_codigo = True
            tabla.append("| Código | Tipo | Mensaje | Descripción |")
            tabla.append("|:---:|:---:|:---:|:---|")
            continue
        elif line.startswith("CO-") and en_tabla_codigo:
            partes = line.split('-')
            codigo = partes[1]
            print(codigo)
            if codigo in ('E1', 'E2', 'E3', '404', '54'):
                tipo = 'error'
            else:
                tipo = 'success'
            mensaje = partes[2]
            descripcion = partes[3]
            tabla.append(f"| {codigo} | {tipo} | {mensaje} | {descripcion} |")
            continue
        elif line == "NT":
            en_tabla = True
            tabla.append("| # | ACTOR | # | SISTEMA | CÓDIGO |")
            tabla.append("|:---:|:---|:---:|:---|:---:|")
            continue
        elif line == "ET":
            if en_tabla_codigo:  # Cerrar la tabla de códigos
                en_tabla_codigo = False
                tabla.append("\n")  # Línea en blanco entre tablas de códigos
                continue
            en_tabla = False
            if buffer_actor:
                tabla.append(buffer_actor + "|   |   |   |")
                buffer_actor = None
            tabla.append("\n")  # Línea en blanco entre comandos
            continue
        else:
            try:
                tipo, accion, texto1, texto2 = procesar_linea(line)
            except Exception as e:
                print(f"Error en la línea: {line}")
                continue

            numero = line.split('-')[0]

            if tipo == "TA":
                if buffer_actor:
                    tabla.append(buffer_actor + "|   |   |   |")
                buffer_actor = f"| {numero} | {accion}: {texto1} "
                
            elif tipo == "TS":
                if buffer_actor:
                    tabla.append(f"{buffer_actor} | {numero} | {accion}: {texto1} | {texto2} |")
                    buffer_actor = None
                else:
                    tabla.append(f"|   |   | {numero} | {accion}: {texto1} | {texto2} |")

    return tabla


def main():
    print("Iniciando programa...")
    #archivo_entrada = "comandos_mark.txt"
    archivo_entrada = "comandos_con_claves_dot.txt"
    ruta_destino = "../../docs/developer_guide/"

    if not os.path.exists(archivo_entrada):
        print(f"Error: El archivo {archivo_entrada} no existe.")
        return

    nf_blocks = procesar_comandos(archivo_entrada)

    if not nf_blocks:
        print("No hay bloques para procesar.")
        return
    
    for block in nf_blocks:
        if 'content' in block:
            content_definicion = procesar_definicion(block['content'])
            block['content'] = generar_tabla_from_content(content_definicion)
    generar_y_guardar_archivo(nf_blocks, ruta_destino)

if __name__ == "__main__":
    main()

