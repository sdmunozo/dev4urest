### Detalle de caso de uso:
# TADTF : Download Taxes Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Download Taxes Template

![TADTF : Download Taxes Template ](../diagrams/uc/uc_png/FL_ADMIN_TADTF.png)


## FLUJO BÁSICO: Download Taxes Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-TADTF01-MPF23
-TS-EJE-TADTF02-Download Template(Taxes)
-TS-RED-TADTF06-MPF74
-TS-MUE-TADTF07-MessageModal[dis_msg, type]
-TA-SEL-TADTF08-MessageModal : Yes
-TA-SEL-TADTF09-MessageModal : No
-TS-CLO-TADTF10-MessageModal
-TS-RED-TADTF11-MPF68
-TS-CLO-TADTF12-MessageModal
-TS-RED-TADTF13-TADTF02
