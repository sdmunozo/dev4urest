### Detalle de caso de uso
# PSUTF : Upload Points Of Sale Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Upload Points Of Sale Template

![PSUTF : Upload Points Of Sale Template ](../developer)


## FLUJO BÁSICO: Upload Points Of Sale Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PSUTF01-MPF128
-TS-MUE-PSUTF02-UploadFileModal('Points of Sale')
-TA-SEL-PSUTF03-Cargar Archivo ['pointsofsale.csv']
-TS-EJE-PSUTF04-Upload File('pointsofsale.csv')
-TS-RED-PSUTF09-MPF94
-TS-MUE-PSUTF10-MessageModal[dis_msg, type]
-TA-SEL-PSUTF11-MessageModal : Yes
-TA-SEL-PSUTF12-MessageModal : No
-TS-CLO-PSUTF13-MessageModal
-TS-RED-PSUTF14-PSUTF04
-TS-CLO-PSUTF15-MessageModal
-TS-RED-PSUTF16-MPF94


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="/developer-guide/diagrams/fl/fl_svg/FL_ADMIN_PSUTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

