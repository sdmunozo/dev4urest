## Formulario de Levantamiento de Requerimientos para Gestión de Usuarios

- Fecha de llenado: 05/ 11/ 2023
- Elaborado por: Daniel Muñoz

### Información General del Proyecto

**1. Nombre del Proyecto:** 

- Dasha / Users

**2. Descripción del Proyecto:**

- **Dasha** es el Dashboard administrativo de 4uRest, donde los usuarios Administradores del Restaurante podrán gestionar, hacer ajustes y configuraciones del sistema de todos los registros necesarios para que el software de **4POS** de operación que sera utilizado por Gerentes, Cajeros, Meseros, Cocineros y personal de asistencia puedan ejecutar desarrollar su trabajo correctamente, como el poder registrar una orden/mesa/pedido capturarle productos con sus modificadores, bloquear la orden y poder completar el proceso de cierre/pago de la misma. 

**3. Objetivos del Dashboard Administrativo en cuanto a gestión de usuarios:**
     
- Gestionar las entidades relacionadas con la administración del restaurate con el objetivo de tener actualizado todo lo relacionado con la gestión de usuarios, los roles y sus permisos. 
- Algunas de las funciones que podra desarrollar el administrador son: 
- Ver los usuarios en una lista en el sistema. 
- Seleccionar un usuario de la lista y poder actualizar su información o eliminarlo. 
- Crear un nuevo usuario y capturar su información. 
- Importar una lista de usuarios a partir de un archivo CSV para la alta en el sistema. 

### Gestión de Usuarios 

**4. Creación de Usuarios:**

*¿Cuáles son los roles de usuario requeridos?*

- Administrador: Es el usuario con los permisos autorizados para efectuar acciones de gestión y mantenimineto en el sistema. Incluye todos los permisos de un Gerente. 

- Gerente: Es el usuario con los permisos de autorización en operaciones que requieren autorización en el sistema 4POS, operaciones que detienen la operación. Tambien es capaz de supervisar a través de reporten en tiempo real datos como ventas, cancelaciones etc. Incluye todos los permisos de un Cajero. 

- Cajero: Tiene la capacidad de abrir un turno y gestionar todas las ordenes activas en el sistema, asi como procesar el pago de las mismas. Incluye todos los permisos de un Mesero. 

- Mesero: Es uno de los usuarios que utilizan el software operativo de 4POS, puede crear nuevas ordenes, gestionar sus productos, bloquear sus órdenes creadas para que no se puedan seguir ingresando productos. 

*¿Qué información se necesita para registrar un nuevo usuario?* 

- Datos de Usuario: Nombre, Apellido, Correo electrónico, Rol, Estado, Icono, PIN de 4POS, Nombre de usuario, Contraseña. 

- Datos de Sistema: Identificador de usuario, Identificador de sus credenciales, campos de auditoria/log. 

*¿Existen validaciones específicas para cada campo de la información del usuario (e.g., formato de email)?* 

- Nombre, Apellido: Sin caracteres especiales fuera de abecedario local. 

- Correo electrónico: Validación de correo electronico 

- Rol: Que se seleccione un Rol obligatoriamente 

- Estado: Por defecto es activo. 

- Icono: Validación de formato para carga de imagenes. 

- PIN de 4POS: Validación de seguridad para creación de pines. 

- Nombre de usuario: Validación de seguridad para creación de nombre de usuario. 

- Contraseña: Validación de seguridad para creación de contraseñas. 

**5. Edición de Usuarios:**

*¿Qué campos se pueden editar después de la creación del usuario?* 

- Edición por parte de usuario: Nombre, Apellido, Correo electrónico, Rol, Estado, Icono, PIN de 4POS, Nombre de usuario, Contraseña. 

- Edición por parte de Sistema: Campos de auditoria/log. 

*¿Existen campos que requieren validaciones especiales al editar?* 

- Nombre, Apellido: Sin caracteres especiales fuera de abecedario local. 

- Correo electrónico: Validación de correo electrónico 

- Rol: Que se seleccione un Rol obligatoriamente 

- Estado: Por defecto es activo. 

- Icono: Validación de formato para carga de imágenes. 

- PIN de 4POS: Validación de seguridad para creación de pines. 

- Nombre de usuario: Validación de seguridad para creación de nombre de usuario. 

- Contraseña: Validación de seguridad para creación de contraseñas. 

**6. Eliminación de Usuarios:**

*Describa el proceso de eliminación de usuarios.*

1. El Administrador entra a la parte de Usuarios, en ella se listan los usuarios con status inactivo y activo, en cada usuario se muestran 2 botones, “Editar” y “Eliminar”. 
2. El Administrador hace clic en el botón de “Eliminar” del usuario deseado. 
3. El sistema muestra un cuadro de confirmación. 
4. El Administrador selecciona Confirmar. 
5. El Sistema registra el usuario con status de eliminado, por lo que ya no se mostrará en el futuro en la lista de usuarios disponibles. 

*¿Cómo se manejarán los usuarios eliminados en la base de datos (borrado lógico o físico)?* 

- El borrado es lógico, a través del *“Status”* del usuario. 

**7. Roles y Permisos:**

*Describa los roles de usuario.*

- Administrador: 
    - Acceso Completo al Sistema. 
    - Gestión Avanzada de Usuarios. 
    - Mantenimiento del Sistema. 
    - Gestión Financiera. 
    - Reportes y Análisis de Datos. 
    - Incluye todos los permisos de un Gerente. 

- Gerente:
    - Autorizar operaciones de autorización. 
    - Gestión de Turnos. 
    - Control de Flujo de Efectivo. 
    - Reportes de Ventas. 
    - Incluye todos los permisos de un Cajero. 

 - Cajero:
    - Todo lo que puede hacer el Mesero pero para todas las órdenes activas en el sistema, no solo para las de él. 
    - Apertura de turnos de caja. 
    - Registro de gastos e ingresos en su turno. 
    - Procesamiento de cierre completo de ordenes con pago. 
    - Solicitar descuento en orden, cierre sin pago. 

- Mesero: 
    - Acceso a plataforma operativa 4POS. 
    - Creación de ordenes en el sistema. 
    - Solicitar cancelación de producto. 

*¿Cómo se asignan los permisos a cada rol?* 

1. El Administrador entra a la parte de Roles, en ella se listan los Roles con status inactivo y activo, en cada Rol se muestran 2 botones, “Editar” y “Eliminar”. 
2. El Administrador hace clic en el botón de “Editar” del Rol deseado. 
3. El sistema muestra una ventana con el detalle del rol y una lista de los permisos permisos disponibles asignados seguida de los no asignados, esto con una palomita de selección si lo tiene asignado. 
4. El Administrador edita los campos relacionados con el rol y/o sus permisos asignados. 
5. El Administrador selecciona guardar cambios. 
6. El Sistema registra registra los cambios realizados en el Rol correspondiente. 
7. El sistema redirige a la parte de Roles. 

**8. Autenticación de Usuarios:**

*Describa los mecanismos de autenticación requeridos (e.g., PIN POS, contraseña).*

- Para ingresar al Dasha se requiere que el usuario ingrese Nombre de usuario y  Contraseña, con estos datos después el usuario hace clic en iniciar sesión el sistema ejecuta las funciones necesarias para validar las credenciales del usuario que debe de tener Rol de Administrador y así permitir acceso al sistema administrativo. 

*¿Hay requisitos especiales de seguridad para la creación de contraseñas?* 

- Contraseña: Validación de seguridad para creación de contraseñas.
- PIN de 4POS: Validación de seguridad para creación de pines. 

**9. Registro de Actividades:**

*¿Qué actividades de los usuarios deben ser registradas (e.g., último inicio de sesión)?* 

- Se debe de registrar cuando un registro es creado. 
- Se debe de registrar cuandoun registro es actualizado. 
- Se debe de registrar cualquier movimiento en cualquier entidad/configuración que se modifique. 

*¿Cómo se visualizarán estas actividades en el dashboard?* 

- En un panel de auditoría, que aún no se pretende planear en este punto. 

**10. Estado y Gestión de Sesiones:**

*Describa cómo se manejará el estado del usuario (activo, inactivo, eliminado).*

- Status activo: Aparece en la lista de registros, se puede, actualizar y eliminar. 
- Status inactivo: Aparece en la lista de registros, se puede, actualizar y eliminar, pero deja de tener acceso al sistema con su cuenta mientras este en este estado. 
- Status eliminado: El usuario sigue registrado, pero se deja de mostrar en la lista de registros, una vez su estado cambia a eliminado, se deja de mostrar, pero sigue apareciendo en todos los registros realizados cuando estuvo activo. 

*¿Cómo se gestionan las sesiones de usuarios (e.g., tiempo de expiración de la sesión)?* 

- La sesión de administrador expira después de un tiempo, que aún no se pretende planear en este punto. 

**11. Interfaz de Usuario:**

*¿Qué operaciones debe soportar la interfaz de usuario relacionadas con la gestión de usuarios?* 

- Poder visualizar la lista de usuarios registrados en una “Pagina principal”.
- Poder descargar una plantilla con el formato adecuado.
- Poder cargar una plantilla con la lista de usuarios que se darán de alta y darlos de alta.
- Poder editar los datos de un usuario seleccionado.
- Poder eliminar un usuario seleccionado.
- Poder crear un nuevo usuario.

Describa los requerimientos visuales y de usabilidad para la gestión de usuarios. 

- Debe de haber una ventana principal para la gestion de los usuarios, desde esta ventana se debe de poder hacer lo siguiente: 

- Descargar plantilla. 
- Cargar Plantilla. 
- Enviar Plantilla para alta de usuarios. 
- Ver la lista de usuarios con estado “Activo” o “Inactivo”, y en cada registro un botón de eliminar o editar. 
- Seleccionar un usuario a un usuario para ver sus detalles. 
- Debe de existir una ventana donde se desglocen los campos para crear/editar un usuario. 
- Debe de existir una ventana donde se puedan desplegar los mensajes de confirmación. 
- Debe de existir un modal para desplegar mensajes sencillos y temporales para visualización de mensajes. 

**12. Integración y Extensibilidad:**

*Describa si la gestión de usuarios debe integrarse con otros sistemas o servicios.*

- La gestión de usuarios se hace desde el Dasha, con esto los usuarios que tengan rol de Gerente, Cajero, Mesero podrán ingresar al sistema con su PIN 4POS 

*¿Es necesario considerar la extensibilidad para futuros roles o permisos?* 

- Sí, después se podrán crear roles y permisos personalizados. 

### Requerimientos No Funcionales 

**13. Seguridad:**

*Describa los requerimientos de seguridad relacionados con la gestión de usuarios.*

- La gestión de usuarios solo se puede hacer por un Rol Administrador que tenga asignado el permiso de Gestión de Usuarios. 

*¿Qué medidas se tomarán para proteger la información de los usuarios?* 

- Solo podrán ser editados por usuarios autorizados (Administrador) y todos los cambios efectuados serán registrados como auditoria. 

**14. Rendimiento:**

*¿Existen expectativas de rendimiento para la carga y gestión de usuarios (e.g., tiempo de respuesta del sistema)?* 

- Prácticamente instantánea, milisegundos en gestión de un solo usuario. 
- En carga masiva puede tardar unos segundos. 

**15. Disponibilidad:**

*¿Cuál es el nivel de disponibilidad requerido para la gestión de usuarios en el dashboard?* 

- Debe de estar siempre disponible, siempre y cuando sea un administrador. 

### Otros Requerimientos 

**16. Legales y de Cumplimiento:**

*¿Existen requerimientos legales o de cumplimiento que afecten la gestión de usuarios?* 

- Sí, de privacidad de datos. 

**17. Comentarios Adicionales:**

- El objetivo es poder tener una gestión completa de los usuarios, pero se comenzará con lo necesario para la carga masiva. Después se irá sobre los otros puntos de la gestión. Se menciona esto con el fin de darle prioridad en el desarrollo.