def extraer_informacion(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        nombre_uc = ''
        buscando_actores = False

        for linea in archivo:
            # Encuentra la línea que inicia el caso de uso
            if linea.startswith('// INICIA >'):
                # Extrae el nombre del caso de uso y agrega un espacio después de ":"
                partes = linea.split('>')[1].split('Flow')[0].strip().split(':')
                clave = partes[0].strip()  # Guarda la clave que está antes del ":"
                nombre_uc = clave + ' : ' + partes[1].strip()
                # Inserta espacios después de los ":" y cada palabra del caso de uso
                nombre_uc = ' '.join(w if w.isupper() else ''.join(' '+c if c.isupper() else c for c in w) for w in nombre_uc.split())

            elif linea.strip() == 'DEF-INI':
                buscando_actores = True
            elif buscando_actores:
                actores = linea.strip()
                # Crea un archivo .puml para este caso de uso
                with open(f'../../docs/diagrams/uc/uc_puml/FL_ADMIN_{clave}.puml', 'w') as puml_file:
                    puml_file.write('@startuml\n\n')
                    puml_file.write('left to right direction\n\n')
                    puml_file.write(f'    usecase "{nombre_uc}" as UserCase\n')
                    puml_file.write(f'    "{actores}" --> UserCase\n\n')
                    puml_file.write('@enduml\n')
                buscando_actores = False

# Llama a la función con el nombre del archivo
extraer_informacion('comandos_con_claves_dot.txt')