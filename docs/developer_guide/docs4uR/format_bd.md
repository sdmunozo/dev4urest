Reglas de estandarización para el diseño y formato de la Base de Datos en Mermaid:

### Convenciones Generales
1. **Nomenclatura de Tablas:**
   - Utilizar notación PascalCase (también conocida como UpperCamelCase) y nombres descriptivos para las tablas.
   - El prefijo "B_" puede ser usado para tablas base y "R_" para tablas de relación, asegurando que este prefijo se mantenga consistente en toda la base de datos.

2. **Nomenclatura de Columnas:**
   - Usar snake_case para los nombres de las columnas.
   - Los nombres deben ser descriptivos y reflejar claramente el contenido de la columna.

3. **Tipos de Datos:**
   - Definir y estandarizar el uso de tipos de datos para ciertos tipos de información, como `DATETIME` para fechas y `INT` para identificadores.
   - Utilizar `ENUM` para campos con un conjunto limitado de valores posibles, definiendo claramente los valores permitidos.

4. **Claves Primarias (PK):**
   - Nombrar las claves primarias como `nombreTabla_id` en snake_case.
   - Utilizar el tipo `int` para las claves primarias, y considerar si se requiere que sean autoincrementales.

5. **Claves Foráneas (FK):**
   - Nombrar las claves foráneas con el formato `nombreReferencia_id` en snake_case.
   - Incluir la referencia exacta en la declaración de la clave foránea, utilizando la sintaxis `[ref: > NombreTablaReferenciada.nombreColumnaReferenciada]`.

### Reglas Específicas
6. **ENUMs:**
   - Definir claramente los valores `ENUM` al inicio del diseño de la base de datos y mantener la consistencia en las tablas.
   - Considerar el uso de tablas de referencia para estados en lugar de ENUMs si se espera que la lista de estados crezca o cambie con el tiempo.

7. **Campos Booleanos:**
   - Utilizar nombres que indiquen claramente que la columna es de tipo booleano, como `is_service`, `is_price_change_allowed`, etc.
   - Asegurarse de que los campos booleanos no contengan otros valores aparte de TRUE/FALSE o equivalentes numéricos.

8. **Campos de Estado:**
   - Usar campos `ENUM` para los estados con un conjunto limitado y conocido de valores, por ejemplo, `status ENUM('1-active', '2-inactive', '3-deleted')`.

9. **Campos de Fecha:**
   - Utilizar `DATETIME` para todas las columnas que almacenen fechas y horas.
   - Nombrar las columnas relacionadas con fechas de manera consistente, por ejemplo, `date_created` y `date_updated`.

10. **Consistencia en Campos Relacionados:**
    - Asegurarse de que los campos relacionados a través de claves foráneas tengan el mismo tipo de dato y restricciones en ambas tablas.

### Convenciones de Documentación
11. **Comentarios y Documentación:**
    - Documentar cada tabla y columna con comentarios que expliquen su propósito y cualquier regla de negocio asociada.
    - Incluir restricciones y reglas de negocio como comentarios en las definiciones de tabla cuando sea apropiado.

Al aplicar estas reglas, se garantiza una mayor coherencia, legibilidad y mantenibilidad en el diseño de la base de datos. Además, se facilita el entendimiento y colaboración entre diferentes desarrolladores y analistas de datos que trabajen con la base de datos.