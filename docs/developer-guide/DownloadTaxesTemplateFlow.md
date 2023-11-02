### Detalle de caso de uso
# TADTF : Download Taxes Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Download Taxes Template

![TADTF : Download Taxes Template ](../developer)


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


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="/developer-guide/diagrams/fl/fl_svg/FL_ADMIN_TADTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

