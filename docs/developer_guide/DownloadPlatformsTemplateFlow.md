### Detalle de caso de uso
# PLDTF : Download Platforms Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Download Platforms Template

![PLDTF : Download Platforms Template ](../developer_guide/diagrams/uc/uc_png/FL_ADMIN_PLDTF.png)


## FLUJO BÁSICO: Download Platforms Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PLDTF01-MPF23
-TS-EJE-PLDTF02-Download Template(Platforms)
-TS-RED-PLDTF06-MPF87
-TS-MUE-PLDTF07-MessageModal[dis_msg, type]
-TA-SEL-PLDTF08-MessageModal : Yes
-TA-SEL-PLDTF09-MessageModal : No
-TS-CLO-PLDTF10-MessageModal
-TS-RED-PLDTF11-MPF81
-TS-CLO-PLDTF12-MessageModal
-TS-RED-PLDTF13-PLDTF02


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="https://sdmunozo.github.io/dev4urest/developer-guide/diagrams/fl/fl_svg/FL_ADMIN_PLDTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

