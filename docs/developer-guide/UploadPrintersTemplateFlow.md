### Detalle de caso de uso:
# PRUTF : Upload Printers Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Upload Printers Template

![PRUTF : Upload Printers Template ](../diagrams/uc/uc_png/FL_ADMIN_PRUTF.png)


## FLUJO BÁSICO: Upload Printers Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PRUTF01-MPF128
-TS-MUE-PRUTF02-UploadFileModal('Printers')
-TA-SEL-PRUTF03-Cargar Archivo ['printers.csv']
-TS-EJE-PRUTF04-Upload File('printers.csv')
-TS-RED-PRUTF09-MPF107
-TS-MUE-PRUTF10-MessageModal[dis_msg, type]
-TA-SEL-PRUTF11-MessageModal : Yes
-TA-SEL-PRUTF12-MessageModal : No
-TS-CLO-PRUTF13-MessageModal
-TS-RED-PRUTF14-PRUTF04
-TS-CLO-PRUTF15-MessageModal
-TS-RED-PRUTF16-MPF107
