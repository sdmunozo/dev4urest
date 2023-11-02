

print("main.py se está iniciando...")

print("1_dot_gen.py se está iniciando...")
exec(open('management/1_dot_gen.py').read())

print("2_dot_to_img.py se está iniciando...")
exec(open('management/2_dot_to_img.py').read())

print("3_dot_mrkd.py se está iniciando...")
exec(open('management/3_dot_mrkd.py').read())

print("4_gen_puml.py se está iniciando...")
exec(open('management/4_gen_puml.py').read())

print("5_puml_to_png.py se está iniciando...")
exec(open('management/5_puml_to_png.py').read())

print("main.py ha terminado.")

