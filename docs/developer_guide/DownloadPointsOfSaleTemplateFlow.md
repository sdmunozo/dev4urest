### Detalle de caso de uso
# PSDTF : Download Points Of Sale Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Download Points Of Sale Template

![PSDTF : Download Points Of Sale Template ](../developer_guide/diagrams/uc/uc_png/FL_ADMIN_PSDTF.png)


## FLUJO BÁSICO: Download Points Of Sale Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PSDTF01-MPF23
-TS-EJE-PSDTF02-Download Template(Points of Sale)
-TS-RED-PSDTF06-MPF100
-TS-MUE-PSDTF07-MessageModal[dis_msg, type]
-TA-SEL-PSDTF08-MessageModal : Yes
-TA-SEL-PSDTF09-MessageModal : No
-TS-CLO-PSDTF10-MessageModal
-TS-RED-PSDTF11-MPF94
-TS-CLO-PSDTF12-MessageModal
-TS-RED-PSDTF13-PSDTF02


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="https://sdmunozo.github.io/dev4urest/developer-guide/diagrams/fl/fl_svg/FL_ADMIN_PSDTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

