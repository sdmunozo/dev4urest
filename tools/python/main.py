from management import s6_add_fd_markd, s1_dot_gen

print("main.py se está iniciando...")

print("- - - s1_dot_gen.py se está iniciando... - - - ")
#print("s1_dot_gen.py se está iniciando...")
#nombre_entidad = "User"
#ruta_commands_dot = "comandos_dot.txt"
#ruta_dot = "../../docs/developer_guide/diagrams/fl/fl_dot/"
#ruta_uc = "../../../developer_guide/diagrams/uc/uc_png/"
#s1_dot_gen.main(nombre_entidad, ruta_commands_dot, ruta_dot, ruta_uc)

exec(open('management/s1_dot_gen.py').read())

print("s2_dot_to_img.py se está iniciando...")
exec(open('management/s2_dot_to_img.py').read())

print("s3_dot_mrkd.py se está iniciando...")
exec(open('management/s3_dot_mrkd.py').read())

print("s4_gen_puml.py se está iniciando...")
exec(open('management/s4_gen_puml.py').read())

print("s5_puml_to_png.py se está iniciando...")
exec(open('management/s5_puml_to_png.py').read())

# - - - - - - - - - - - - - - - - - - - - - - - - 
print("- - - s6_add_fd_markd.py se está iniciando... - - - ")
s6_add_fd_markd.main("User", "../../docs/developer_guide/")
#s6_add_fd_markd.main("User", "../../docs/developer_guide/Entities/User")

print("main.py ha terminado.")

