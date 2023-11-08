### Caso de uso: Visualización de Lista de Usuarios.

| Caso de uso: | Visualización de Lista de Usuarios |
|---|---|
| Requerimientos relacionados | RF1.1 |
| Objetivo en contexto | Permitir al administrador la visualización eficiente y correcta de todos los usuarios, tanto activos como inactivos, dentro del sistema de gestión Dasha / Users. |
| Precondiciones | El administrador debe estar autenticado y autorizado dentro del sistema. El sistema debe estar operativo y contar con los datos actualizados de los usuarios. |
| Final exitoso | El administrador visualiza la lista completa de usuarios activos e inactivos sin errores y en el tiempo de respuesta esperado. |
| Actores principales | Administrador |
| Actores secundarios | BaseData (que provee la información de los usuarios) |
| Evento de inicio | El administrador solicita ver la lista de usuarios a través de la interfaz de usuario del Dashboard. |
| Flujo principal |1. El Administrador inicia sesión en el sistema Dasha / Users con sus credenciales.<br><br>2. Una vez dentro del dashboard, el Administrador selecciona la opción “Gestión de Usuarios”. <br><br>3. El sistema (Backend) solicita a la BaseData la lista de usuarios. <br><br>4. BaseData procesa la solicitud y envía la lista de usuarios activos e inactivos al Backend. <br><br>5. El Backend envía la información al Frontend para su visualización. <br><br>6. El Administrador recibe la lista y visualiza en el Frontend todos los usuarios con sus respectivos estados (activo/inactivo). <br><br>7. El Administrador puede interactuar con la lista, realizando acciones como ordenar, filtrar o buscar usuarios específicos, según sea necesario. <br><br>8. Si el Administrador selecciona un usuario específico, puede ver detalles adicionales o realizar otras acciones proporcionadas por el sistema. |

### Caso de uso: Creación de Usuarios en Dasha

| Caso de uso: | Creación de Usuarios en Dasha |
|---|---|
| Requerimientos relacionado | RF1.2 |
| Objetivo en contexto | Permitir que el Administrador registre nuevos usuarios en el sistema Dasha, asegurándose de que toda la información requerida sea validada y almacenada correctamente. |
| Precondiciones | - El Administrador debe estar autenticado en el sistema Dasha.<br><br>- El Administrador debe tener permisos para la gestión de usuarios. |
| Final exitoso | Un nuevo usuario es creado en el sistema con todos los datos necesarios validados y almacenados. |
| Actores principales | Administrador |
| Actores secundarios | BaseData (para la persistencia de los datos del usuario) |
| Evento de inicio | El Administrador selecciona la opción de crear un nuevo usuario. |
| Flujo principal | 1. El Administrador elige la opción de crear un nuevo usuario desde la interfaz de gestión de usuarios.<br><br>2. El sistema presenta un formulario para introducir la información del usuario (Nombre, Apellido, Correo electrónico, Rol, Estado, Icono, PIN de 4POS, Nombre de usuario, Contraseña).<br><br>3. El Administrador ingresa los datos requeridos del nuevo usuario.<br><br>4. El sistema valida cada campo según las especificaciones dadas (caracteres permitidos, formato de correo electrónico, selección de rol, entre otros).<br><br>5. El sistema valida que no exista un nombre de usuario o correo electrónico duplicado.<br><br>6. El sistema solicita confirmación al Administrador para crear el nuevo usuario.<br><br>7. El Administrador confirma la creación del usuario.<br><br>8. El sistema registra al nuevo usuario en la BaseData, asignando un identificador único y guardando la información de auditoría/log correspondiente.<br><br>9. El sistema notifica al Administrador que el usuario fue creado exitosamente.<br><br>10. El sistema redirige al Administrador a la lista de usuarios actualizada. |

### Caso de uso: Edición de Información de Usuarios

| Caso de uso: | Edición de Información de Usuarios |
|---|---|
| Requerimientos relacionados | RF1.3 |
| Objetivo en contexto | Permitir a los administradores editar la información de los usuarios del sistema **Dasha** para el software **4POS**, asegurando que se realicen validaciones específicas por campo para mantener la integridad de los datos. |
| Precondiciones | El Administrador debe estar autenticado y tener los permisos necesarios para editar usuarios. Los datos de usuario existentes deben estar accesibles. |
| Final exitoso | La información del usuario se actualiza correctamente en la base de datos con todas las validaciones de campo cumplidas y los registros de auditoría adecuados. |
| Actores principales | Administrador |
| Actores secundarios | BaseData (sistema de gestión de bases de datos) |
| Evento de inicio | El Administrador selecciona la opción de editar un usuario en la interfaz de gestión de usuarios. |
| Flujo principal | 1. El Administrador navega a la sección de gestión de usuarios en el Dashboard Administrativo (**Dasha**).<br><br>2. El Administrador elige un usuario de la lista y selecciona la opción "Editar".<br><br>3. Se presenta el formulario de edición con los campos actuales del usuario seleccionado.<br><br>4. El Administrador realiza los cambios necesarios, con las validaciones de campo activas para cada entrada (e.g., formato de correo electrónico, validación de PIN de 4POS, etc.).<br><br>5. Una vez completada la edición, el Administrador envía el formulario.<br><br>6. El sistema **Backend** verifica las validaciones de los campos editados.<br><br>7. Si alguna validación falla, se notifica al Administrador y se solicita la corrección.<br><br>8. Si todas las validaciones son correctas, el **Backend** envía los cambios a la **BaseData**.<br><br>9. **BaseData** actualiza la información en la base de datos y genera los registros de auditoría/log correspondientes.<br><br>10. El sistema confirma al Administrador que los datos se han actualizado correctamente.<br><br>11. El usuario editado refleja los cambios cuando se accede a su información en futuras sesiones. |

### Caso de uso: Eliminación de Usuarios en Dasha

| Caso de uso: | Eliminación de Usuarios en Dasha |
|---|---|
| Requerimientos relacionados | RF1.4 |
| Objetivo en contexto | Permitir al Administrador eliminar usuarios de manera lógica en el sistema Dasha, garantizando que los datos del usuario se mantengan para propósitos de auditoría. |
| Precondiciones | - El Administrador debe estar autenticado y tener permisos para gestionar usuarios. <br><br> - El usuario a eliminar debe existir en la base de datos. |
| Final exitoso | El usuario seleccionado se marca con un status de eliminado y no se muestra en la lista de usuarios activos. |
| Actores principales | Administrador |
| Actores secundarios | BaseData (sistema de base de datos) |
| Evento de inicio | El Administrador selecciona la opción de eliminar en la interfaz de gestión de usuarios. |
| Flujo principal | 1. El Administrador ingresa a la sección de gestión de usuarios dentro del Dasha.<br><br> 2. El Administrador busca y selecciona el usuario a eliminar y presiona el botón "Eliminar".<br><br> 3. El sistema muestra un cuadro de confirmación para evitar eliminaciones accidentales.<br><br> 4. El Administrador confirma la eliminación del usuario.<br><br> 5. El sistema envía la solicitud de eliminación al Backend.<br><br> 6. El Backend procesa la solicitud y cambia el status del usuario a "eliminado" en la BaseData.<br><br> 7. La BaseData confirma que el status se ha actualizado correctamente.<br><br> 8. El sistema informa al Administrador que el usuario ha sido eliminado.<br><br> 9. El sistema actualiza la lista de usuarios, removiendo al usuario eliminado de la vista activa. |

### Caso de uso: Importación Masiva de Usuarios

| Caso de uso: | Importación Masiva de Usuarios |
|---|---|
| Requerimientos relacionado | RF1.5 |
| Objetivo en contexto | Facilitar al Administrador la carga de múltiples usuarios al sistema Dasha de forma eficiente y segura a través de un archivo CSV. |
| Precondiciones | - El Administrador debe estar autenticado en el sistema Dasha con los permisos necesarios para gestionar usuarios. <br><br> - Debe existir una plantilla CSV estándar para la importación de usuarios. <br><br> - El archivo CSV debe cumplir con el formato y las validaciones especificadas en la guía de instrucciones. El Administrador debe de ubicarse en Dasha/Users |
| Final exitoso | Los usuarios son importados al sistema y se muestran en la lista de todos los usuarios. |
| Actores principales | Administrador |
| Actores secundarios | Frontend, Backend, BaseData |
| Evento de inicio | El Administrador selecciona la opción para importar usuarios a través de un archivo CSV en Dasha. |
| Flujo principal | 1. El Administrador selecciona "Descargar plantilla" desde Dasha/Users. <br><br> 2. El Frontend realiza la solicitud al Backend de los datos necesarios para generar el archivo CSV.<br><br> 3. El Backend realiza la solicitud de a la BaseData de los datos a escribir el archivo CSV.<br><br> 4. La BaseData recupera los datos solicitados y se los proporciona al Backend.<br><br> 6. El Backend responde al Frontend con la información solicitada.<br><br> 7. El Frontend recibe los datos requeridos para generar el archivo CSV, los procesa e inicia la descarga.<br><br> 8. El Administrador recibe la plantilla CSV y la rellena con los datos de los nuevosusuariossiguiendolas validaciones especificadas. <br><br> 9. El Administrador selecciona "Cargar Usuarios(CSV)" desde Dasha/Users. <br><br> 10. El Frontend valida el formato del archivo y muestra un resumen de la informaciónaimportaroloserrores encontrados. <br><br> 11. El Administrador revisa y confirma la información del resumen. <br><br> 12. El Frontend envía el archivo al Backend. <br><br> 13. El Backend realiza las validaciones de seguridad y de negocio sobre los datos del archivo CSV. <br><br> 14. El Backend procesa la importación y solicita el almacenamiento de los datos de los nuevos usuarios a la BaseData. <br><br> 15. La BaseData recibe la solicitud, la procesa y retorna una respuesta.16. El Backend envía una confirmación de la importación exitosa al Frontend. <br><br> 17. El Frontend notifica al Administrador sobre el éxito de la operación. <br><br> 18. El Administrador puede ver los nuevos usuarios en la lista de usuarios dentro del sistema. |

