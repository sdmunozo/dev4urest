### Detalle de caso de uso
# PRUTF : Upload Product Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Upload Product Template

![PRUTF : Upload Product Template ](../developer_guide/diagrams/uc/uc_png/FL_ADMIN_PRUTF.png)


## FLUJO BÁSICO: Upload Product Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PRUTF01-MPF128
-TS-MUE-PRUTF02-UploadFileModal('Product')
-TA-SEL-PRUTF03-Cargar Archivo ['products.csv']
-TS-EJE-PRUTF04-Upload File('products.csv')
-TS-RED-PRUTF09-MPF16
-TS-MUE-PRUTF10-MessageModal[dis_msg, type]
-TA-SEL-PRUTF11-MessageModal : Yes
-TA-SEL-PRUTF12-MessageModal : No
-TS-CLO-PRUTF13-MessageModal
-TS-RED-PRUTF14-PRUTF04
-TS-CLO-PRUTF15-MessageModal
-TS-RED-PRUTF16-MPF16


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="/diagrams/fl/fl_svg/FL_ADMIN_PRUTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

