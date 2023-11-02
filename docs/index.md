# Bienvenido a la Documentación de Mi Sistema

## Ejemplo de Markdown

Aquí puedes escribir texto en formato Markdown.

## Diagrama de Mermaid

```mermaid
sequenceDiagram
    participant AdminUser as Administrador
    participant FrontendUI as Sistema (Frontend)
    participant BackendService as Sistema (Backend)
    participant Database as Base de Datos

    AdminUser->>FrontendUI: Selecciona: "Descargar Plantilla"
    FrontendUI->>BackendService: Solicita Descargar Plantilla

    BackendService->>Database: Consulta Plantilla por User(user_id)
    Database-->>BackendService: Devuelve Contenido del User Template

    alt éxito (código 200)
        BackendService-->>FrontendUI: Envía Datos de la Plantilla
        FrontendUI->>FrontendUI: Genera archivo CSV con el contenido
        FrontendUI->>AdminUser: Inicia la descarga del archivo CSV
        FrontendUI->>FrontendUI: Redirige a MPF126
    else no encontrado (código 404)
        BackendService-->>FrontendUI: Error (404)
        FrontendUI->>AdminUser: Muestra MessageModal[dis_msg, type]
        alt Yes
            AdminUser->>FrontendUI: Selecciona MessageModal: Yes
            FrontendUI->>FrontendUI: Cierra ventana MessageModal
            FrontendUI->>FrontendUI: Redirige a UDTF02
        else No
            AdminUser->>FrontendUI: Selecciona MessageModal: No
            FrontendUI->>FrontendUI: Cierra ventana MessageModal
            FrontendUI->>FrontendUI: Redirige a MPF120
        end
    else error base de datos (código E1)
        BackendService-->>FrontendUI: Error E1
        FrontendUI->>AdminUser: Muestra MessageModal[dis_msg, type]
        alt Yes
            AdminUser->>FrontendUI: Selecciona MessageModal: Yes
            FrontendUI->>FrontendUI: Cierra ventana MessageModal
            FrontendUI->>FrontendUI: Intenta reconectar o redirige a UDTF02
        else No
            AdminUser->>FrontendUI: Selecciona MessageModal: No
            FrontendUI->>FrontendUI: Cierra ventana MessageModal
            FrontendUI->>FrontendUI: Redirige a MPF120
        end
    end

```

```
digraph {
    A -> B;
    B -> C;
    A -> C;
    C -> D;
}
```

```plantuml
@startuml
Alice -> Bob: Hello
Bob -> Alice: Hi!
@enduml



## Visualización Interactiva del SVG

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="./diagrams/fl/fl_svg/FL-ADMIN-CADTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
</div>

<script>
window.addEventListener("load", function() {
    var svgElement = document.querySelector('#diagramaSvg').contentDocument.documentElement;
    svgPanZoom(svgElement, {
        zoomEnabled: true,
        controlIconsEnabled: true
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var plantUmlElements = document.querySelectorAll('code.language-plantuml');

    plantUmlElements.forEach(function(element) {
        var plantUMLText = element.innerText;
        var encodedPlantUML = plantumlEncoder.encode(plantUMLText);
        var img = document.createElement('img');
        img.src = 'http://www.plantuml.com/plantuml/png/' + encodedPlantUML;
        element.parentElement.replaceWith(img);
    });
});
</script>
