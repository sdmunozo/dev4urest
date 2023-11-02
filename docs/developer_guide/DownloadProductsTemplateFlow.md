### Detalle de caso de uso
# PIDTF : Download Products Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Download Products Template

![PIDTF : Download Products Template ](../developer_guide/diagrams/uc/uc_png/FL_ADMIN_PIDTF.png)


## FLUJO BÁSICO: Download Products Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PIDTF01-MPF23
-TS-EJE-PIDTF02-Download Template(Products)
-TS-RED-PIDTF06-MPF22
-TS-MUE-PIDTF07-MessageModal[dis_msg, type]
-TA-SEL-PIDTF08-MessageModal : Yes
-TA-SEL-PIDTF09-MessageModal : No
-TS-CLO-PIDTF10-MessageModal
-TS-RED-PIDTF11-MPF16
-TS-CLO-PIDTF12-MessageModal
-TS-RED-PIDTF13-PDDTF02


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="/developer_guide/diagrams/fl/fl_svg/FL_ADMIN_PIDTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

