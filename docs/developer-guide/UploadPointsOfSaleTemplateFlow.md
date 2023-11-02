### Detalle de caso de uso:
# PSUTF : Upload Points Of Sale Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Upload Points Of Sale Template

![PSUTF : Upload Points Of Sale Template ](../diagrams/uc/uc_png/FL_ADMIN_PSUTF.png)


## FLUJO BÁSICO: Upload Points Of Sale Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PSUTF01-MPF128
-TS-MUE-PSUTF02-UploadFileModal('Points of Sale')
-TA-SEL-PSUTF03-Cargar Archivo ['pointsofsale.csv']
-TS-EJE-PSUTF04-Upload File('pointsofsale.csv')
-TS-RED-PSUTF09-MPF94
-TS-MUE-PSUTF10-MessageModal[dis_msg, type]
-TA-SEL-PSUTF11-MessageModal : Yes
-TA-SEL-PSUTF12-MessageModal : No
-TS-CLO-PSUTF13-MessageModal
-TS-RED-PSUTF14-PSUTF04
-TS-CLO-PSUTF15-MessageModal
-TS-RED-PSUTF16-MPF94
