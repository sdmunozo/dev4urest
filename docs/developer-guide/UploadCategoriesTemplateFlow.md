### Detalle de caso de uso:
# CAUTF : Upload Categories Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Upload Categories Template

![CAUTF : Upload Categories Template ](../diagrams/uc/uc_png/FL_ADMIN_CAUTF.png)


## FLUJO BÁSICO: Upload Categories Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-CAUTF01-MPF128
-TS-MUE-CAUTF02-UploadFileModal('Categories')
-TA-SEL-CAUTF03-Cargar Archivo ['categories.csv']
-TS-EJE-CAUTF04-Upload File('categories.csv')
-TS-RED-CAUTF09-MPF29
-TS-MUE-CAUTF10-MessageModal[dis_msg, type]
-TA-SEL-CAUTF11-MessageModal : Yes
-TA-SEL-CAUTF12-MessageModal : No
-TS-CLO-CAUTF13-MessageModal
-TS-RED-CAUTF14-CAUTF04
-TS-CLO-CAUTF15-MessageModal
-TS-RED-CAUTF16-MPF29
