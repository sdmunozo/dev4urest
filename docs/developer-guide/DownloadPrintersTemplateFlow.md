### Detalle de caso de uso:
# PIDTF : Download Printers Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Download Printers Template

![PIDTF : Download Printers Template ](../diagrams/uc/uc_png/FL_ADMIN_PIDTF.png)


## FLUJO BÁSICO: Download Printers Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PIDTF01-MPF23
-TS-EJE-PIDTF02-Download Template(Printers)
-TS-RED-PIDTF06-MPF113
-TS-MUE-PIDTF07-MessageModal[dis_msg, type]
-TA-SEL-PIDTF08-MessageModal : Yes
-TA-SEL-PIDTF09-MessageModal : No
-TS-CLO-PIDTF10-MessageModal
-TS-RED-PIDTF11-MPF107
-TS-CLO-PIDTF12-MessageModal
-TS-RED-PIDTF13-PIDTF02
