### Detalle de caso de uso
# PMUTF : Upload Payment Methods Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Upload Payment Methods Template

![PMUTF : Upload Payment Methods Template ](../diagrams/uc/uc_png/FL_ADMIN_PMUTF.png)


## FLUJO BÁSICO: Upload Payment Methods Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PMUTF01-MPF128
-TS-MUE-PMUTF02-UploadFileModal('Payment Methods')
-TA-SEL-PMUTF03-Cargar Archivo ['paymentmethods.csv']
-TS-EJE-PMUTF04-Upload File('paymentmethods.csv')
-TS-RED-PMUTF09-MPF42
-TS-MUE-PMUTF10-MessageModal[dis_msg, type]
-TA-SEL-PMUTF11-MessageModal : Yes
-TA-SEL-PMUTF12-MessageModal : No
-TS-CLO-PMUTF13-MessageModal
-TS-RED-PMUTF14-PMUTF04
-TS-CLO-PMUTF15-MessageModal
-TS-RED-PMUTF16-MPF42


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="../../../diagrams/fl/fl_svg/FL_ADMIN_PMUTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

