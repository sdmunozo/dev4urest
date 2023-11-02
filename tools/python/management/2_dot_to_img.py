import os
import subprocess

def convert_dot_to_png_and_svg():
    # Ruta de entrada y salida
    input_path = '../../docs/developer-guide/diagrams/fl/fl_dot'
    output_path_png = '../../docs/developer-guide/diagrams/fl/fl_png'
    output_path_svg = '../../docs/developer-guide/diagrams/fl/fl_svg'
    
    # Verificar si Graphviz está instalado
    try:
        subprocess.run(["dot", "-V"], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError:
        print("Error: Graphviz no está instalado. Por favor, instálalo para continuar.")
        return

    # Crear carpetas de salida si no existen
    if not os.path.exists(output_path_png):
        os.makedirs(output_path_png)
    if not os.path.exists(output_path_svg):
        os.makedirs(output_path_svg)

    # Listar todos los archivos .dot en la carpeta de entrada
    dot_files = [f for f in os.listdir(input_path) if f.endswith('.dot')]

    for dot_file in dot_files:
        # Nombre del archivo sin extensión
        base_name = os.path.splitext(dot_file)[0]
        input_file_path = os.path.join(input_path, dot_file)
        
        # Convertir .dot a .png
        output_file_path_png = os.path.join(output_path_png, base_name + '.png')
        subprocess.run(["dot", "-Tpng", input_file_path, "-o", output_file_path_png])
        
        # Convertir .dot a .svg
        output_file_path_svg = os.path.join(output_path_svg, base_name + '.svg')
        subprocess.run(["dot", "-Tsvg", input_file_path, "-o", output_file_path_svg])

    print(f"{len(dot_files)} archivos .dot han sido convertidos a .png y .svg.")

if __name__ == "__main__":
    convert_dot_to_png_and_svg()
