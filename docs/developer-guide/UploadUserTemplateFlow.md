### Detalle de caso de uso:
# UDUTF : Upload User Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Upload User Template

![UDUTF : Upload User Template ](../diagrams/uc/uc_png/FL_ADMIN_UDUTF.png)


## FLUJO BÁSICO: Upload User Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-UDUTF01-MPF128
-TS-MUE-UDUTF02-UploadFileModal('User')
-TA-SEL-UDUTF03-Cargar Archivo ['users.csv']
-TS-EJE-UDUTF04-Upload File('users.csv')
-TS-RED-UDUTF09-MPF120
-TS-MUE-UDUTF10-MessageModal[dis_msg, type]
-TA-SEL-UDUTF11-MessageModal : Yes
-TA-SEL-UDUTF12-MessageModal : No
-TS-CLO-UDUTF13-MessageModal
-TS-RED-UDUTF14-UDUTF04
-TS-CLO-UDUTF15-MessageModal
-TS-RED-UDUTF16-MPF120
