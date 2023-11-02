import re

comandos = []

def process_commands(commands):
    diagrams = []
    current_diagram = []

    for command in commands:
        if command == "ND":
            if current_diagram:
                diagrams.append(current_diagram)
                current_diagram = []
        elif command == "WR":
            if current_diagram:
                diagrams.append(current_diagram)
                current_diagram = []
        else:
            current_diagram.append(command)

    return diagrams

command_key_mapping = {}


def process_diagram(diagram_commands):
    
    comandos = []
    diagram_name = diagram_commands.pop(0)
    three_digit_key = diagram_commands.pop(0)
    filename = f"../../docs/developer_guide/diagrams/fl/fl_dot/FL_ADMIN_{three_digit_key}.dot"
    comandos.append("// INICIA > " + three_digit_key + " : " + diagram_name)
    comandos.append("")
    comandos.append("NF")
    comandos.append("NFNA-" + diagram_name)
    comandos.append("")
    comandos.append("### Detalle de caso de uso")
    comandos.append("# " + three_digit_key + " : " + re.sub(r'([a-z])([A-Z])', r'\1 \2', diagram_name).replace("Flow", ""))
    comandos.append("")
    comandos.append("## DEFINICIÓN\n")
    comandos.append("DEF-INI")
    comandos.append("Administrador")
    comandos.append("El usuario Administrador es capaz de ")
    comandos.append("PR")
    comandos.append("PO")
    comandos.append("1 de Noviembre 2023")
    comandos.append("1 de Noviembre 2023")
    comandos.append("DEF-END")
    comandos.append("")
    comandos.append("## DIAGRAMA: " + re.sub(r'([a-z])([A-Z])', r'\1 \2', diagram_name).replace("Flow", ""))
    ruta_img = "../developer_guide/diagrams/uc/uc_png/FL_ADMIN_" + three_digit_key + ".png"
    alt_text = three_digit_key + " : " + re.sub(r'([a-z])([A-Z])', r'\1 \2', diagram_name).replace("Flow", "")
    comandos.append("IMG-" + alt_text + "-" + ruta_img)
    comandos.append("")
    comandos.append("## FLUJO BÁSICO: " + re.sub(r'([a-z])([A-Z])', r'\1 \2', diagram_name).replace("Flow", ""))
    comandos.append("NT")

    with open(filename, 'w') as file:
        file.write(f"digraph {diagram_name} {{\n")
        file.write("    node [shape=box];\n")
        file.write("    edge [dir=forward];\n\n")
        file.write("    //Contenido\n\n")
        table_counter = 1
        summary = []
        
        reserved_keys = set()  # Set para mantener las claves reservadas


        for command in diagram_commands:
            # Verificar si el comando es EXIT para salir
            if command == "EXIT":
                break

            # Si el comando comienza con 2 dígitos, verifica y ajusta table_counter
            match = re.match(r'^(\d{2})-', command)
            if match:
                reserved_key = int(match.group(1))
                reserved_keys.add(reserved_key)
                #table_counter = reserved_key + 1  # Ajusta el contador al siguiente número después del número reservado

            # Si el table_counter actual está reservado, incrementa hasta encontrar uno no reservado
            while table_counter in reserved_keys:
                table_counter += 1

            # Generar el nombre de la tabla
            table_key = f"{table_counter:02}"  # Solo los dígitos.
            table_name = three_digit_key + table_key  # Para usar en el archivo .dot

            # Registrar y escribir el contenido en función de los comandos
            if command.startswith("TA-SEL-"):
                text = command[7:]
                summary.append(f"{table_name}-TA-SEL-{text}")
                cmd = (f"TA-SEL-{text}")
                cmd_upd = f"{cmd.split('-')[0]}-{cmd.split('-')[1]}-{table_name}-{cmd.split('-')[2]}"
                comandos.append("-" + cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="black">{table_name}: <FONT COLOR="blue">Actor</FONT></FONT>.</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="orange">Selecciona: </FONT>"{text}".</TD>
    </TR>
</TABLE>>];\n\n'''

            elif command.startswith("TA-ING-"):
                text = command[7:]
                summary.append(f"{table_name}-TA-ING-{text}")
                cmd = (f"TA-ING-{text}")
                cmd_upd = cmd_upd = f"{cmd.split('-')[0]}-{cmd.split('-')[1]}-{table_name}-{cmd.split('-')[2]}"
                comandos.append("-" + cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="black">{table_name}: <FONT COLOR="blue">Actor</FONT></FONT>.</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="orange">Ingresa: </FONT>"{text}".</TD>
    </TR>
</TABLE>>];\n\n'''
                
            elif command.startswith("TS-EVA-"):
                text = command[7:]
                summary.append(f"{table_name}-TS-EVA-{text}")
                cmd = (f"TS-EVA-{text}")
                cmd_upd = f"{cmd.split('-')[0]}-{cmd.split('-')[1]}-{table_name}-{cmd.split('-')[2]}"
                comandos.append("-" + cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="black">{table_name}: <FONT COLOR="green">Sistema</FONT></FONT>.</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="blue">Evalúa: </FONT>"{text}".</TD>
    </TR>
</TABLE>>];\n\n'''

            elif command.startswith("TS-CAR-"):
                text = command[7:]
                summary.append(f"{table_name}-TS-CAR-{text}")
                cmd = (f"TS-CAR-{text}")
                cmd_upd = f"{cmd.split('-')[0]}-{cmd.split('-')[1]}-{table_name}-{cmd.split('-')[2]}"
                comandos.append("-" + cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="black">{table_name}: <FONT COLOR="green">Sistema</FONT></FONT>.</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="blue">Carga: </FONT>"{text}".</TD>
    </TR>
</TABLE>>];\n\n'''

            elif command.startswith("TS-MUE-"):
                text = command[7:]
                summary.append(f"{table_name}-TS-MUE-{text}")
                cmd = (f"TS-MUE-{text}")
                cmd_upd = f"{cmd.split('-')[0]}-{cmd.split('-')[1]}-{table_name}-{cmd.split('-')[2]}"
                comandos.append("-" + cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="black">{table_name}: <FONT COLOR="green">Sistema</FONT></FONT>.</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="green">Muestra: </FONT>"{text}".</TD>
    </TR>
</TABLE>>];\n\n'''

            elif command.startswith("TS-EJE-"):
                text = command[7:]
                summary.append(f"{table_name}-TS-EJE-{text}")
                cmd = (f"TS-EJE-{text}")
                cmd_upd = cmd_upd = f"{cmd.split('-')[0]}-{cmd.split('-')[1]}-{table_name}-{cmd.split('-')[2]}"
                comandos.append("-" + cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="black">{table_name}: <FONT COLOR="green">Sistema</FONT></FONT>.</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="blue">Ejecuta: </FONT>"{text}".</TD>
    </TR>
</TABLE>>];\n\n'''

            elif command.startswith("TR-BAN-"):
                texts = command[7:].split('-')
                if len(texts) != 3:
                    print("El formato del comando TR-BAN debe tener tres partes de texto separadas por '-'.")
                    continue
                summary.append(f"{table_name}-TR-BAN-{texts[0]}-{texts[1]}-{texts[2]}")
                cmd = (f"TR-COD-{texts[0]}-{texts[1]}-{texts[2]}")
                cmd_upd = f"{cmd.split('-')[0]}-{cmd.split('-')[1]}-{table_name}-{cmd.split('-')[2]}-{cmd.split('-')[3]}-{cmd.split('-')[4]}"
                comandos.append(cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="black">{table_name}: <FONT COLOR="black">Response</FONT></FONT>.</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="purple">res_msg: </FONT>"{texts[0]}".</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="purple">dis_msg: </FONT>"{texts[1]}".</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="purple">type: </FONT>"{texts[2]}".</TD>
    </TR>
</TABLE>>];\n\n'''
                
            elif command.startswith("TR-RES-"):
                texts = command[7:].split('-')
                if len(texts) != 2:
                    print("El formato del comando TS-RES debe tener tres partes de texto separadas por '-'.")
                    continue
                summary.append(f"{table_name}-TR-RES-{texts[0]}-{texts[1]}")
                cmd = (f"TR-COD-{texts[0]}-{texts[1]}")
                cmd_upd = f"{cmd.split('-')[0]}-{cmd.split('-')[1]}-{table_name}-{cmd.split('-')[2]}-{cmd.split('-')[3]}"
                comandos.append(cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="black">{table_name}: <FONT COLOR="black">Response</FONT></FONT>.</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="purple">res_msg: </FONT>"{texts[0]}".</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="purple">res_obj: </FONT>"{texts[1]}".</TD>
    </TR>
</TABLE>>];\n\n'''
                
            elif command.startswith("RED-"):
                text = command[4:]
                summary.append(f"{table_name}-RED-{text}")
                cmd = (f"RED-{text}")
                cmd_upd = f"TS-{cmd.split('-')[0]}-{table_name}-{cmd.split('-')[1]}"
                comandos.append("-" + cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
        <TR>
            <TD CELLPADDING="4"><FONT COLOR="black">{table_name}: Redirige a:</FONT></TD>
        </TR>
        <TR>
            <TD CELLPADDING="4"><FONT COLOR="blue">{text}.</FONT></TD>
        </TR>
    </TABLE>>];\n\n'''

            elif command.startswith("VIE3-"):
                texts = command[5:].split('-')
                if len(texts) != 3:
                    print("El formato del comando VIE3- debe tener tres partes de texto separadas por '-'.")
                    continue
                table_name = three_digit_key + f"{table_counter:02}"
                summary.append(f"{table_name}-VIE3-{texts[0]}-{texts[1]}-{texts[2]}")
                comandos.append(table_name + "-" + command)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
                    <TR>
                        <TD CELLPADDING="4">{table_name}: Viene de:</TD>
                    </TR>
                    <TR>
                        <TD CELLPADDING="4"><FONT COLOR="orange">{texts[0]}.</FONT></TD>
                    </TR>
                    <TR>
                        <TD CELLPADDING="4"><FONT COLOR="orange">{texts[1]}.</FONT></TD>
                    </TR>
                    <TR>
                        <TD CELLPADDING="4"><FONT COLOR="orange">{texts[2]}.</FONT></TD>
                    </TR>
                </TABLE>>];\n\n'''
                file.write(table_content)

            elif command.startswith("VIE2-"):
                texts = command[5:].split('-')
                if len(texts) != 2:
                    print("El formato del comando VIE2- debe tener tres partes de texto separadas por '-'.")
                    continue
                table_name = three_digit_key + f"{table_counter:02}"
                summary.append(f"{table_name}-VIE2-{texts[0]}-{texts[1]}")
                comandos.append(table_name + "-" + command)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
                    <TR>
                        <TD CELLPADDING="4">{table_name}: Viene de:</TD>
                    </TR>
                    <TR>
                        <TD CELLPADDING="4"><FONT COLOR="orange">{texts[0]}.</FONT></TD>
                    </TR>
                    <TR>
                        <TD CELLPADDING="4"><FONT COLOR="orange">{texts[1]}.</FONT></TD>
                    </TR>
                </TABLE>>];\n\n'''
                file.write(table_content)

            elif command.startswith("VIE1-"):
                texts = command[5:].split('-')
                if len(texts) != 1:
                    print("El formato del comando VIE1- debe tener tres partes de texto separadas por '-'.")
                    continue
                table_name = three_digit_key + f"{table_counter:02}"
                summary.append(f"{table_name}-VIE1-{texts[0]}")
                cmd = (f"VIE1-{texts[0]}")
                cmd_upd = f"TS-{cmd.split('-')[0]}-{table_name}-{cmd.split('-')[1]}"
                comandos.append("-" + cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
                    <TR>
                        <TD CELLPADDING="4">{table_name}: Viene de:</TD>
                    </TR>
                    <TR>
                        <TD CELLPADDING="4"><FONT COLOR="orange">{texts[0]}.</FONT></TD>
                    </TR>
                </TABLE>>];\n\n'''
                file.write(table_content)

            elif command.startswith("TS-CLO-"):
                text = command[7:]
                table_name = three_digit_key + f"{table_counter:02}"

                summary.append(f"{table_name}-TS-CLO-{text}")
                cmd = (f"TS-CLO-{text}")
                cmd_upd = f"{cmd.split('-')[0]}-{cmd.split('-')[1]}-{table_name}-{cmd.split('-')[2]}"
                comandos.append("-" + cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
                <TR>
                    <TD CELLPADDING="4">{table_name}: <FONT COLOR="green">Sistema</FONT></TD>
                </TR>
                <TR>
                    <TD CELLPADDING="4"><FONT COLOR="blue">Cierra</FONT>: "{text}"</TD>
                </TR>
                </TABLE>>];\n\n'''
                file.write(table_content)

            elif command == "TS-WAI":
                table_name = three_digit_key + f"{table_counter:02}"
                summary.append(f"{table_name}-TS-WAI")
                cmd = (f"TS-WAI")
                cmd_upd = f"{cmd.split('-')[0]}-{cmd.split('-')[1]}-{table_name}"
                comandos.append("-" + cmd_upd)
                table_content = '''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="black">{table_name}: <FONT COLOR="green">Sistema</FONT></FONT>.</TD>
    </TR>
    <TR>
        <TD CELLPADDING="4"><FONT COLOR="blue">Espera acción de usuario.</FONT></TD>
    </TR>
</TABLE>>];\n\n'''.format(table_name=table_name)
                #print(table_content)
                file.write(table_content)


            elif command.startswith("TS-EJF-"):
                texts = command[7:].split('-')
                if len(texts) != 3:
                    print("El formato del comando TS-EJF debe tener tres partes de texto separadas por '-'.")
                    continue
                summary.append(f"{table_name}-TS-EJF-{texts[0]}-{texts[1]}-{texts[2]}")
                cmd = (f"TS-EJF-{texts[0]}-{texts[1]}-{texts[2]}")
                cmd_upd = f"{cmd.split('-')[0]}-{cmd.split('-')[1]}-{table_name}-{cmd.split('-')[2]}-{cmd.split('-')[3]}-{cmd.split('-')[4]}"
                comandos.append(cmd_upd)
                table_content = f'''{table_name} [label=<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
            <TR>
                <TD CELLPADDING="4"><FONT COLOR="black">{table_name}: <FONT COLOR="green">Sistema</FONT></FONT>.</TD>
            </TR>
            <TR>
                <TD CELLPADDING="4"><FONT COLOR="green">Ejecuta Flujo: </FONT>"{texts[0]}".</TD>
            </TR>
            <TR>
                <TD CELLPADDING="4"><FONT COLOR="red">Acción: </FONT>"{texts[1]}".</TD>
            </TR>
            <TR>
                <TD CELLPADDING="4"><FONT COLOR="orange">res_obj: </FONT>"{texts[2]}".</TD>
            </TR>
            </TABLE>>];\n\n'''


            elif command == "LS":
                for item in summary:
                    print(item)
                continue

            elif command.startswith("AR-"):
                parts = command.split('-')
                if len(parts) != 3:
                    print("Formato incorrecto para el comando AR-XX-YY.")
                    continue
                file.write(f"{three_digit_key}{parts[1]} -> {three_digit_key}{parts[2]};\n")

            elif command.startswith("ARG-"):
                parts = command.split('-')
                if len(parts) != 4:
                    print("Formato incorrecto para el comando ARG-[CODE]-XX-YY.")
                    continue
                file.write(f"{three_digit_key}{parts[2]} -> {three_digit_key}{parts[3]} [label=\"code: '{parts[1]}'\", color=\"green\"];\n")

            elif command.startswith("ARR-"):
                parts = command.split('-')
                if len(parts) != 4:
                    print("Formato incorrecto para el comando ARR-[CODE]-XX-YY.")
                    continue
                file.write(f"{three_digit_key}{parts[2]} -> {three_digit_key}{parts[3]} [label=\"code: '{parts[1]}'\", color=\"red\"];\n")

            elif command.startswith("ARW-"):
                parts = command.split('-')
                if len(parts) != 5:
                    print("Formato incorrecto para el comando ARW-[TEXT]-[COLOR]-XX-YY.")
                    continue
                file.write(f"{three_digit_key}{parts[3]} -> {three_digit_key}{parts[4]} [label=\"{parts[1]}\", color=\"{parts[2]}\"];\n")

            else:
                print("Comando no reconocido. Intente nuevamente o ingrese 'EXIT' para salir.")
                continue

            if not command.startswith(("AR-", "ARG-", "ARR-", "ARW-")):
                file.write(table_content)
                table_counter += 1

            # Registra el comando y su clave asignada solo si no es un comando de tipo flecha
            if not command.startswith(("AR-", "ARG-", "ARR-", "ARW-")):
                command_key_mapping[command] = table_key
                #print(command_key_mapping)
            
        file.write("}\n")

    comandos.append("")
    comandos.append("")
    comandos.append("WR")
    comandos.append("// TERMINA > " + three_digit_key + " : " + diagram_name)
    comandos.append("")
    comandos.append("")
    print(f"Archivo {filename} creado exitosamente!")
    return comandos

def main():    

    with open("comandos_dot.txt", 'r') as f:
        commands = [line.strip() for line in f.readlines() if line.strip() and not line.strip().startswith('//')]

    diagrams = process_commands(commands)

    for diagram_commands in diagrams:
        comandos.append(process_diagram(diagram_commands))

    with open("comandos_con_claves_dot.txt", 'w') as f_out, open("comandos_dot.txt", 'r') as f_in:

        for cmd_list in comandos:

            for line in cmd_list:
                f_out.write(line + '\n')
        
    print("Comandos registrados en comandos_con_claves_dot.txt.")

if __name__ == "__main__":
    main()