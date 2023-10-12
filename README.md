# VenEmergencia API Test

Esta API proporciona una serie de endpoints para interactuar con datos relacionados con automóviles. La API ofrece las siguientes funcionalidades:

1. **Obtener todos los autos**
   - Ruta: `/getAllCars/`
   - Descripción: Devuelve una lista de todos los autos disponibles.
   - Parámetros:
     - `skip` (opcional): Salta un número determinado de registros (por defecto 0).
     - `limit` (opcional): Limita la cantidad de registros devueltos (por defecto 100).

2. **Obtener las primeras cinco y últimas cinco líneas**
   - Ruta: `/getFirstFiveAndLastFive`
   - Descripción: Devuelve las primeras cinco y las últimas cinco líneas de los datos de los automóviles.

3. **Encontrar la compañía de automóviles más costosa**
   - Ruta: `/mostExpensiveCompany`
   - Descripción: Encuentra la compañía de automóviles con el precio total más alto de todos sus automóviles.

4. **Imprimir todos los detalles de los autos Toyota**
   - Ruta: `/detailsToyotaCars`
   - Descripción: Obtiene todos los estilos de automóviles de la compañía Toyota.

5. **Contar el número total de autos por compañía**
   - Ruta: `/countCarsByCompany`
   - Descripción: Permite contar el número total de automóviles por compañía.
   - Parámetros:
     - `company` (opcional): Selecciona una compañia en espesifica.

6. **Encontrar el precio más alto por cada compañía**
   - Ruta: `/maxPriceByCompany`
   - Descripción: Obtiene el precio más alto de un automóvil para cada compañía.
   - Parámetros:
     - `company` (opcional): Selecciona una compañia en espesifica.

7. **Encontrar el kilometraje promedio de cada compañía**
   - Ruta: `/averageMileageByCompany`
   - Descripción: Calcula el kilometraje promedio de los automóviles para cada compañía.
   - Parámetros:
     - `company` (opcional): Selecciona una compañia en espesifica.

8. **Ordenar todos los carros por la columna Precio**
   - Ruta: `/orderByPrice`
   - Descripción: Devuelve una lista de todos los automóviles ordenados por precio.

9. **Cargar datos de automóviles desde un archivo CSV**
   - Ruta: `/loadCars/`
   - Descripción: Carga datos de automóviles desde un archivo CSV proporcionado y almacena los datos en la base de datos.

## Requisitos

Asegúrate de instalar todas las dependencias necesarias para ejecutar este proyecto. Puedes encontrar una lista de dependencias en el archivo `requirements.txt`.

## Configuración de Postman

Para probar los endpoints de esta API, se proporciona una colección de Postman en el archivo `fastApiTest.postman_collection.json`. Importa esta colección en Postman y configura las variables de entorno según sea necesario.

## Instalación y Ejecución

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias del proyecto usando `pip install -r requirements.txt`.
3. Ejecuta la aplicación con el siguiente comando:

   ```shell
   uvicorn app.main:app --reload