### Detalle de caso de uso
# PEDTF : Download Permissions Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Download Permissions Template

![PEDTF : Download Permissions Template ](../diagrams/uc/uc_png/FL_ADMIN_PEDTF.png)


## FLUJO BÁSICO: Download Permissions Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PEDTF01-MPF23
-TS-EJE-PEDTF02-Download Template(Permissions)
-TS-RED-PEDTF06-MPF152
-TS-MUE-PEDTF07-MessageModal[dis_msg, type]
-TA-SEL-PEDTF08-MessageModal : Yes
-TA-SEL-PEDTF09-MessageModal : No
-TS-CLO-PEDTF10-MessageModal
-TS-RED-PEDTF11-MPF146
-TS-CLO-PEDTF12-MessageModal
-TS-RED-PEDTF13-PEDTF02


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="../../../diagrams/fl/fl_svg/FL_ADMIN_PEDTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

