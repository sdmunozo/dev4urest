import os
from plantuml import PlantUML

def convert_puml_to_png(input_folder, output_folder):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Configurar el servicio web de PlantUML
    plantuml_service = PlantUML(url='http://www.plantuml.com/plantuml/png/')  # Cambiado a PNG

    # Listar todos los archivos .puml en la carpeta de entrada
    puml_files = [f for f in os.listdir(input_folder) if f.endswith('.puml')]

    for puml_file in puml_files:
        input_file_path = os.path.join(input_folder, puml_file)
        
        # Convertir .puml a .png
        output_file_path = os.path.join(output_folder, os.path.splitext(puml_file)[0] + '.png')  # Cambiado a PNG
        plantuml_service.processes_file(input_file_path, outfile=output_file_path)

    print(f"{len(puml_files)} archivos .puml han sido convertidos a .png.")  # Cambiado a PNG

if __name__ == "__main__":
    input_folder_path = "../../docs/developer-guide/diagrams/uc/uc_puml"
    output_folder_path = "../../docs/developer-guide/diagrams/uc/uc_png"
    convert_puml_to_png(input_folder_path, output_folder_path)  # Cambiado a PNG
