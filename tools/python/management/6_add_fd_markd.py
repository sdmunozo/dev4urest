import os
import re

def encontrar_clave_y_agregar_codigo(ruta):
    # Verificar si la ruta existe
    if not os.path.exists(ruta):
        print("La ruta especificada no existe.")
        return

    # Regex para capturar la clave en la estructura especificada
    regex_clave = re.compile(r'^#\s+([A-Z]+)\s+:', re.MULTILINE)

    # Recorrer los archivos en la ruta especificada
    for archivo in os.listdir(ruta):
        print(f"Procesando: {archivo}")  # Depuración: Imprimir el nombre del archivo en proceso
        # Construir la ruta completa al archivo
        ruta_completa = os.path.join(ruta, archivo)
        # Verificar si es un archivo .md
        if os.path.isfile(ruta_completa) and archivo.endswith('.md'):
            try:
                # Leer el contenido del archivo y luego escribir al final
                with open(ruta_completa, 'r') as file:
                    contenido = file.read()
                    match = regex_clave.search(contenido)

                # Si se encuentra una clave, escribir el código al final del archivo
                if match:
                    clave = match.group(1)
                    #print(f"Encontrada clave: {clave}")  # Depuración: Imprimir la clave encontrada
                    codigo_a_insertar = (
                        f"\n\n## Diagrama de Flujo\n\n"
                        f"<div style=\"border: 1px solid black; width: 800px; height: 600px; overflow: hidden;\">\n"
                        f"    <object data=\"/diagrams/fl/fl_svg/FL_ADMIN_{clave}.svg\" type=\"image/svg+xml\" id=\"diagramaSvg\" width=\"100%\" height=\"100%\"></object>\n"
                        "</div>\n\n"
                        "<script>\n"
                        "window.addEventListener(\"load\", function() {\n"
                        "    var svgElement = document.querySelector('#diagramaSvg').contentDocument.documentElement;\n"
                        "    svgPanZoom(svgElement, {\n"
                        "        zoomEnabled: true,\n"
                        "        controlIconsEnabled: true\n"
                        "    });\n"
                        "});\n\n"
                        "</script>\n\n"
                    )
                    # Abrir el archivo nuevamente para escribir al final
                    with open(ruta_completa, 'a') as file:  # 'a' abre el archivo para agregar al final
                        file.write(codigo_a_insertar)
                        print(f"Código agregado a {archivo}")
                else:
                    print(f"No se encontró la clave en {archivo}")  # Depuración: No se encontró la clave
            except Exception as e:
                print(f"Error procesando el archivo {archivo}: {e}")  # Manejo de excepciones

# Establecer la ruta de entrada aquí o pedir al usuario que la introduzca
ruta_usuario = "../../docs/developer_guide/"
encontrar_clave_y_agregar_codigo(ruta_usuario)