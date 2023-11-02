### Detalle de caso de uso:
# LAF : Login Admin
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Login Admin

![LAF : Login Admin ](../diagrams/uc/uc_png/FL_ADMIN_LAF.png)


## FLUJO BÁSICO: Login Admin
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-LAF01-MPF01
-TA-ING-LAF02-B_User.username, B_User.password
-TS-EJE-LAF03-Login Pin[B_User.username, B_User.password]
-TS-RED-LAF07-MPF03
-TS-MUE-LAF08-MessageBanner[dis_msg, type]
-TS-EJE-LAF09-Logout
-TS-RED-LAF10-MPF01
