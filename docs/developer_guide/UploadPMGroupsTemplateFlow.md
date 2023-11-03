### Detalle de caso de uso
# PGUTF : Upload PMGroups Template
## DEFINICIÓN

- **Actores:** Administrador

- **Descripción:** El usuario Administrador es capaz de

- **Pre condiciones:** PR

- **Post condiciones:** PO

- **Fecha de creación:** 1 de Noviembre 2023

- **Fecha de actualización:** 1 de Noviembre 2023


## DIAGRAMA: Upload PMGroups Template

![PGUTF : Upload PMGroups Template ](../developer_guide/diagrams/uc/uc_png/FL_ADMIN_PGUTF.png)


## FLUJO BÁSICO: Upload PMGroups Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
-TS-VIE1-PGUTF01-MPF128
-TS-MUE-PGUTF02-UploadFileModal('PMGroups')
-TA-SEL-PGUTF03-Cargar Archivo ['pmgroups.csv']
-TS-EJE-PGUTF04-Upload File('pmgroups.csv')
-TS-RED-PGUTF09-MPF55
-TS-MUE-PGUTF10-MessageModal[dis_msg, type]
-TA-SEL-PGUTF11-MessageModal : Yes
-TA-SEL-PGUTF12-MessageModal : No
-TS-CLO-PGUTF13-MessageModal
-TS-RED-PGUTF14-PGUTF04
-TS-CLO-PGUTF15-MessageModal
-TS-RED-PGUTF16-MPF55


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="https://sdmunozo.github.io/dev4urest/developer-guide/diagrams/fl/fl_svg/FL_ADMIN_PGUTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
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

