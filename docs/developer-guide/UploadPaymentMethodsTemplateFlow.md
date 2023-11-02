### Detalle de caso de uso:
# PMUTF : Upload Payment Methods Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Upload Payment Methods Template

![PMUTF : Upload Payment Methods Template ](../diagrams/uc/uc_png/FL_ADMIN_PMUTF.png)


## FLUJO BÁSICO: Upload Payment Methods Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PMUTF01-MPF128
-TS-MUE-PMUTF02-UploadFileModal('Payment Methods')
-TA-SEL-PMUTF03-Cargar Archivo ['paymentmethods.csv']
-TS-EJE-PMUTF04-Upload File('paymentmethods.csv')
-TS-RED-PMUTF09-MPF42
-TS-MUE-PMUTF10-MessageModal[dis_msg, type]
-TA-SEL-PMUTF11-MessageModal : Yes
-TA-SEL-PMUTF12-MessageModal : No
-TS-CLO-PMUTF13-MessageModal
-TS-RED-PMUTF14-PMUTF04
-TS-CLO-PMUTF15-MessageModal
-TS-RED-PMUTF16-MPF42
