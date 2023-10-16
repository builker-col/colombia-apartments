# Datos Procesados

> ⚠️ Es importante destacar que durante el proceso de web scraping se respetaron las políticas y condiciones de uso establecidas por cada sitio web.

En esta carpeta se encuentran los datos procesados, es decir, los datos que han sido limpiados y transformados para su posterior análisis.

## Significado de las columnas

### Apartamentos

**File:** [apartments.csv](apartments.csv)

| Columna                              | Descripción                                               |
|--------------------------------------|-----------------------------------------------------------|
| codigo                               | Código único que identifica cada apartamento              |
| ciudad                               | Ciudad en la que se encuentra el apartamento              |
| tipo_propiedad                       | Tipo de propiedad (apartamento, casa, etc.)               |
| tipo_operacion                       | Tipo de operación (venta, arriendo, etc.)                 |
| precio_venta                         | Precio de venta del apartamento COP                       |
| precio_arriendo                      | Precio de arriendo del apartamento COP                    |
| area                                 | Área del apartamento en metros cuadrados                  |
| habitaciones                         | Número de habitaciones del apartamento                    |
| banos                                | Número de baños del apartamento                           |
| administracion                       | Valor de la cuota de administración del apartamento       |
| parqueaderos                         | Número de parqueaderos disponibles                        |
| sector                               | Sector o zona en la que se encuentra el apartamento       |
| sector_comun                         | Sector o zona común en la que se encuentra el apartamento |
| estrato                              | Estrato socioeconómico del apartamento                    |
| antiguedad                           | Antigüedad del apartamento en años                        |
| estado                               | Estado del apartamento (nuevo, usado)                     |
| longitud                             | Longitud geográfica del apartamento                       |
| latitud                              | Latitud geográfica del apartamento                        |
| descripcion                          | Descripción detallada del apartamento                     |
| datetime                             | Fecha y hora de extracción de los datos                   |
| jacuzzi                              | Indica si el apartamento cuenta con jacuzzi               |
| piso                                 | Número de piso en el que se encuentra el apartamento      |
| closets                              | Número de closets en el apartamento                       |
| chimenea                             | Indica si el apartamento cuenta con chimenea              |
| permite_mascotas                     | Indica si se permiten mascotas en el apartamento          |
| gimnasio                             | Indica si el apartamento cuenta con gimnasio              |
| ascensor                             | Indica si el edificio cuenta con ascensor                 |
| conjunto_cerrado                     | Indica si el apartamento se encuentra en conjunto cerrado |
| website                              | Sitio web relacionado a la propiedad                      |
| compañia                             | Compañía o agencia responsable de la propiedad            |
| fecha_actualizacion_precio_venta     | Fecha de actualización del precio de venta (scrapeado)    |
| precio_venta_anterior                | Precio de venta anterior de la propiedad COP              |
| fecha_actualizacion_precio_arriendo  | Fecha de actualización del precio de arriendo (scrapeado) |
| precio_arriendo_anterior             | Precio de arriendo anterior de la propiedad COP           |
| last_viewed                          | Ultima fecha en la que el scraper visito la propiedad     |

### Imagenes

**File:** [images.csv](images.csv)

| Columna      | Descripción                                      |
|--------------|--------------------------------------------------|
| codigo       | Código único que identifica cada apartamento.    |
| url_imagen   | Enlace URL de la imagen asociada al apartamento. |