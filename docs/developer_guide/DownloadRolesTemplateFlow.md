### Detalle de caso de uso
# RODTF : Download Roles Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Download Roles Template

![RODTF : Download Roles Template ](../developer_guide/diagrams/uc/uc_png/FL_ADMIN_RODTF.png)


## FLUJO BÁSICO: Download Roles Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-RODTF01-MPF23
-TS-EJE-RODTF02-Download Template(Roles)
-TS-RED-RODTF06-MPF139
-TS-MUE-RODTF07-MessageModal[dis_msg, type]
-TA-SEL-RODTF08-MessageModal : Yes
-TA-SEL-RODTF09-MessageModal : No
-TS-CLO-RODTF10-MessageModal
-TS-RED-RODTF11-MPF133
-TS-CLO-RODTF12-MessageModal
-TS-RED-RODTF13-RODTF02


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="https://sdmunozo.github.io/dev4urest/developer-guide/diagrams/fl/fl_svg/FL_ADMIN_RODTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

