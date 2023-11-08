### Detalle de caso de uso
# USDTF : Download User Template
## DEFINICIÓN

- **Actores:** Administrador.

- **Descripción:** El usuario Administrador es capaz de descargar una plantilla en formato csv con el fin de tener la base para dar de alta masivamente a usuarios en el sistema.

- **Pre condiciones:** Haber ingresado con usuario y clave de Administrador.

- **Post condiciones:** Archivo "UserTemplate.csv" descargado correctamente.

- **Fecha de creación:** 1 de Noviembre 2023.

- **Fecha de actualización:** 3 de Noviembre 2023.


## DIAGRAMA: Download User Template

![USDTF : Download User Template ](../developer_guide/diagrams/uc/uc_png/FL_ADMIN_USDTF.png)


## FLUJO BÁSICO: Download User Template
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
|   |   | 1 | «USDTF01» Viene de: MPF127 : SEL "Descargar Plantilla" |  |
|   |   | 2 | «USDTF02» Ejecuta: downloadUserTemplate() | 200 404 E1 |


### Códigos : downloadUserTemplate()
| Código | Tipo | Mensaje | Descripción |
|:---:|:---:|:---:|:---|
| 200 | success | Success | Descarga UserTemplate.csv |
| 404 | error | Record not found | Hay un problema con el servidor. |
| E1 | error | Database not available | No hay conexión con la base de datos. |


### FLUJO downloadUserTemplate() : 200
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
|   |   | 1 | «USDTF06» Redirige a: MPF126 : Esperar acción de usuario |  |


### FLUJO downloadUserTemplate() : 404 E1
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
|   |   | 1 | «USDTF07» Muestra: showMessageModal(dis_msg, type) |  |


### FLUJO downloadUserTemplate() : 404 E1 : Yes
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
| 1 | «USDTF08» Selecciona: MessageModal : Yes  | 2 | «USDTF10» Cierra: MessageModal |  |
|   |   | 3 | «USDTF11» Redirige a: MPF120 : Muestra MainUsersListPage |  |


### FLUJO downloadUserTemplate() : 404 E1 : No
| # | ACTOR | # | SISTEMA | CÓDIGO |
|:---:|:---|:---:|:---|:---:|
| 1 | «USDTF09» Selecciona: MessageModal : No  | 2 | «USDTF12» Cierra: MessageModal |  |
|   |   | 3 | «USDTF13» Redirige a: USDTF02 |  |


## Diagrama de Flujo

<div style="border: 1px solid black; width: 800px; height: 600px; overflow: hidden;">
    <object data="https://sdmunozo.github.io/dev4urest/developer_guide/diagrams/fl/fl_svg/FL_ADMIN_USDTF.svg" type="image/svg+xml" id="diagramaSvg" width="100%" height="100%"></object>
</div>

<a href="https://sdmunozo.github.io/dev4urest/developer_guide/diagrams/fl/fl_svg/FL_ADMIN_USDTF.svg" target="_blank">Abrir diagrama de flujo FL_ADMIN_USDTF en nueva pestaña</a>
<script>
window.addEventListener("load", function() {
    var svgElement = document.querySelector('#diagramaSvg').contentDocument.documentElement;
    svgPanZoom(svgElement, {
        zoomEnabled: true,
        controlIconsEnabled: true
    });
});

</script>

## Diagrama de Secuencia

```mermaid
sequenceDiagram
    participant AdminUser as Administrador
    participant FrontendUI as Frontend
    participant BackendService as Backend
    participant Database as Data Base
    AdminUser->>FrontendUI: Selecciona: "Descargar Plantilla"
    FrontendUI->>BackendService: Solicita: downloadUserTemplate()
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

```mermaid
flowchart TD
    Start((Inicio))
    SeleccionarPlantilla["Selecciona: 'Descargar Plantilla'"]
    SolicitaTemplate["Solicita: downloadUserTemplate()"]
    ConsultaPlantilla["Consulta Plantilla por User(user_id)"]
    DevuelveTemplate["Devuelve Contenido del User Template"]
    GenerarCSV{"Genera archivo CSV con el contenido?"}
    IniciarDescarga["Inicia la descarga del archivo CSV"]
    RedirigeMPF126["Redirige a MPF126"]
    Error404["Error (404)"]
    MuestraError404["Muestra MessageModal[dis_msg, type]"]
    SeleccionarYesNo404{Selecciona Yes/No en MessageModal}
    CerrarModal404["Cierra ventana MessageModal"]
    RedirigeUDTF02_404["Redirige a UDTF02"]
    RedirigeMPF120_404["Redirige a MPF120"]
    ErrorDB["Error E1"]
    MuestraErrorDB["Muestra MessageModal[dis_msg, type]"]
    SeleccionarYesNoDB{Selecciona Yes/No en MessageModal}
    CerrarModalDB["Cierra ventana MessageModal"]
    ReconectarRedirigeUDTF02["Intenta reconectar o redirige a UDTF02"]
    RedirigeMPF120_DB["Redirige a MPF120"]
    End((Fin))

    Start --> SeleccionarPlantilla --> SolicitaTemplate --> ConsultaPlantilla
    ConsultaPlantilla --> DevuelveTemplate
    DevuelveTemplate --> GenerarCSV
    GenerarCSV -- Sí, éxito (código 200) --> IniciarDescarga --> RedirigeMPF126 --> End
    GenerarCSV -- No, no encontrado (código 404) --> Error404
    GenerarCSV -- No, error base de datos (código E1) --> ErrorDB
    Error404 --> MuestraError404 --> SeleccionarYesNo404
    SeleccionarYesNo404 -- Sí --> CerrarModal404 --> RedirigeUDTF02_404 --> End
    SeleccionarYesNo404 -- No --> CerrarModal404 --> RedirigeMPF120_404 --> End
    ErrorDB --> MuestraErrorDB --> SeleccionarYesNoDB
    SeleccionarYesNoDB -- Sí --> CerrarModalDB --> ReconectarRedirigeUDTF02 --> End
    SeleccionarYesNoDB -- No --> CerrarModalDB --> RedirigeMPF120_DB --> End
```