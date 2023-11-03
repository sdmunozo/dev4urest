### Detalle de caso de uso
# PMDTF : Download Payment Methods Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Download Payment Methods Template

![PMDTF : Download Payment Methods Template ](../developer_guide/diagrams/uc/uc_png/FL_ADMIN_PMDTF.png)


## FLUJO BÁSICO: Download Payment Methods Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PMDTF01-MPF23
-TS-EJE-PMDTF02-Download Template(Payment Methods)
-TS-RED-PMDTF06-MPF48
-TS-MUE-PMDTF07-MessageModal[dis_msg, type]
-TA-SEL-PMDTF08-MessageModal : Yes
-TA-SEL-PMDTF09-MessageModal : No
-TS-CLO-PMDTF10-MessageModal
-TS-RED-PMDTF11-MPF42
-TS-CLO-PMDTF12-MessageModal
-TS-RED-PMDTF13-PMDTF02


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="https://sdmunozo.github.io/dev4urest/developer_guide/diagrams/fl/fl_svg/FL_ADMIN_PMDTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

