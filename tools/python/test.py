def extraer_informacion(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        nombre_uc = ''
        buscando_actores = False

        for linea in archivo:
            # Encuentra la línea que inicia el caso de uso
            if linea.startswith('// INICIA >'):
                # Extrae el nombre del caso de uso y agrega un espacio después de ":"
                partes = linea.split('>')[1].split('Flow')[0].strip().split(':')
                nombre_uc = partes[0].strip() + ' : ' + partes[1].strip()
                # Inserta espacios después de los ":" y cada palabra del caso de uso
                nombre_uc = ' '.join(w if w.isupper() else ''.join(' '+c if c.isupper() else c for c in w) for w in nombre_uc.split())

            elif linea.strip() == 'DEF-INI':
                buscando_actores = True
            elif buscando_actores:
                actores = linea.strip()
                print(f'{nombre_uc}')
                buscando_actores = False

# Llama a la función con el nombre del archivo
extraer_informacion('comandos_con_claves_dot.txt')
