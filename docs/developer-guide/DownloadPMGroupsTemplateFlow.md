### Detalle de caso de uso
# PGDTF : Download PMGroups Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Download PMGroups Template

![PGDTF : Download PMGroups Template ](../diagrams/uc/uc_png/FL_ADMIN_PGDTF.png)


## FLUJO BÁSICO: Download PMGroups Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PGDTF01-MPF23
-TS-EJE-PGDTF02-Download Template(PMGroups)
-TS-RED-PGDTF06-MPF61
-TS-MUE-PGDTF07-MessageModal[dis_msg, type]
-TA-SEL-PGDTF08-MessageModal : Yes
-TA-SEL-PGDTF09-MessageModal : No
-TS-CLO-PGDTF10-MessageModal
-TS-RED-PGDTF11-MPF55
-TS-CLO-PGDTF12-MessageModal
-TS-RED-PGDTF13-PGDTF02


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="../../../diagrams/fl/fl_svg/FL_ADMIN_PGDTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

