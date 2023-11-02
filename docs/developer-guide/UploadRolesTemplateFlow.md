### Detalle de caso de uso:
# ROUTF : Upload Roles Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Upload Roles Template

![ROUTF : Upload Roles Template ](../diagrams/uc/uc_png/FL_ADMIN_ROUTF.png)


## FLUJO BÁSICO: Upload Roles Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-ROUTF01-MPF128
-TS-MUE-ROUTF02-UploadFileModal('Roles')
-TA-SEL-ROUTF03-Cargar Archivo ['roles.csv']
-TS-EJE-ROUTF04-Upload File('roles.csv')
-TS-RED-ROUTF09-MPF133
-TS-MUE-ROUTF10-MessageModal[dis_msg, type]
-TA-SEL-ROUTF11-MessageModal : Yes
-TA-SEL-ROUTF12-MessageModal : No
-TS-CLO-ROUTF13-MessageModal
-TS-RED-ROUTF14-ROUTF04
-TS-CLO-ROUTF15-MessageModal
-TS-RED-ROUTF16-MPF133
