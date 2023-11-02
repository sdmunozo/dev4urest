### Detalle de caso de uso
# TAUTF : Upload Taxes Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Upload Taxes Template

![TAUTF : Upload Taxes Template ](../developer)


## FLUJO BÁSICO: Upload Taxes Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-TAUTF01-MPF128
-TS-MUE-TAUTF02-UploadFileModal('Taxes')
-TA-SEL-TAUTF03-Cargar Archivo ['taxes.csv']
-TS-EJE-TAUTF04-Upload File('taxes.csv')
-TS-RED-TAUTF09-MPF68
-TS-MUE-TAUTF10-MessageModal[dis_msg, type]
-TA-SEL-TAUTF11-MessageModal : Yes
-TA-SEL-TAUTF12-MessageModal : No
-TS-CLO-TAUTF13-MessageModal
-TS-RED-TAUTF14-TAUTF04
-TS-CLO-TAUTF15-MessageModal
-TS-RED-TAUTF16-MPF68


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="/developer-guide/diagrams/fl/fl_svg/FL_ADMIN_TAUTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

