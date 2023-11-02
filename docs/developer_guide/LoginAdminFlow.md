### Detalle de caso de uso
# LAF : Login Admin
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Login Admin

![LAF : Login Admin ](../developer_guide/diagrams/uc/uc_png/FL_ADMIN_LAF.png)


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


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="../developer_guide/diagrams/fl/fl_svg/FL_ADMIN_LAF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
</div>

<script>
window.addEventListener("load", function() {
    var svgElement = document.querySelector('#diagramaSvg').contentDocument.documentElement;
    svgPanZoom(svgElement, {
        zoomEnabled: true,
        controlIconsEnabled: true
    });
});

</script>

