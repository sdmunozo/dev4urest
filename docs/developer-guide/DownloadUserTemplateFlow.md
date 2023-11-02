### Detalle de caso de uso:
# UDTF : Download User Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Download User Template

![UDTF : Download User Template ](../diagrams/uc/uc_png/FL_ADMIN_UDTF.png)


## FLUJO BÁSICO: Download User Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-UDTF01-MPF23
-TS-EJE-UDTF02-Download Template(User)
-TS-RED-UDTF06-MPF126
-TS-MUE-UDTF07-MessageModal[dis_msg, type]
-TA-SEL-UDTF08-MessageModal : Yes
-TA-SEL-UDTF09-MessageModal : No
-TS-CLO-UDTF10-MessageModal
-TS-RED-UDTF11-MPF120
-TS-CLO-UDTF12-MessageModal
-TS-RED-UDTF13-UDTF02
