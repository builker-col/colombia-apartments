# Colombia Apartments

[![ko-fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white)](https://ko-fi.com/U6U0K5UNW)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@erik172) 
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/builker-col/colombia-apartments)
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/erik172/)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/datasets/erik172/)

![Colombia Apartments](/.github/colombia-apartments.png)
__Image generated with [dall-e](https://openai.com/blog/dall-e/)__

La última fecha de scrapeo fue: **24 September 2023**

Ultima version de los datos: **V0.1.0 SEPTEMBER.2 2023**

Ultima version del scraper: **V0.1.0**

## Table of Contents
- [Descripción](#descripción)
- [Configuración](#configuración)
- [Data Source](#data-source)
- [Datos](#datos)
    - [Raw Data](#raw-data)
    - [Apartamentos](#apartamentos)
    - [Imagenes](#imagenes)
- [Actualización de los datos](#actualización-de-los-datos)
- [MongoDB Dashboard](#mongodb-dashboard)
- [Como Contribuir](#como-contribuir)
- [Mantenimiento](#mantenimiento)
- [Licencia](#licencia)
- [Versiones](releases.md)
- [Projectos Relacionados](#projectos-relacionados)
  - [Bogota Apartments](#bogota-apartments)
- [Creditos](#creditos)

## Descripción
Colombia Apartments es una extension del proyecto [Bogota Apartments](https://github.com/builker-col/bogota-apartments) donde se busca incluir datos de apartamentos de otras ciudades de Colombia aparte de Bogotá.

Este proyecto es una iniciativa de código abierto que tiene como objetivo recopilar y analizar datos sobre el mercado inmobiliario de apartamentos en Colombia.

## Configuración

## Data Source
> ⚠️ Es importante destacar que durante el proceso de web scraping se respetaron las políticas y condiciones de uso establecidas por cada sitio web.

Los datos del proyecto fueron extraídos mediante web scraping de los siguientes sitios web:

- [Metrocuadrado](https://www.metrocuadrado.com/)
<!-- - [Habi](https://www.habi.co/) -->

Se implemento un scraper creado con la librería [Scrapy](https://scrapy.org/) y en caso de que el sitio web este creado con JavaScript [Scrapy](https://scrapy.org/) se conbinara con [Selenium](https://www.selenium.dev/).

## Datos
### Raw Data
### Apartamentos

file: [apartments.csv](data/processed/apartments.csv)

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

file: [images.csv](data/processed/images.csv)

| Columna      | Descripción                                      |
|--------------|--------------------------------------------------|
| codigo       | Código único que identifica cada apartamento.    |
| url_imagen   | Enlace URL de la imagen asociada al apartamento. |

## Actualización de los datos
Los datos extraídos mediante web scraping serán actualizados regularmente para mantenerlos al día. A continuación se detallan los aspectos clave de la actualización:

- Los datos serán actualizados al menos cada 3 semanas, con una frecuencia mínima de actualización mensual. Esto asegurará que los datos reflejen la información más reciente disponible en las fuentes de origen.
- Durante el proceso de actualización, se revisarán y recopilarán los nuevos datos disponibles, así como se verificará la consistencia y calidad de los datos existentes.
- Se implementará un proceso automatizado para la actualización de los datos, utilizando herramientas y scripts específicos para realizar el web scraping de las fuentes de origen de manera eficiente y precisa.
- Después de cada actualización, se realizará un análisis y verificación de los datos para garantizar su integridad y confiabilidad.
- Se publicará la fecha de la última actualización en este README para que los usuarios puedan verificar la frescura de los datos.

## MongoDB Dashboard

[MonogoDB Dashboard](https://charts.mongodb.com/charts-project-0-vjiwc/public/dashboards/c0144208-93e3-46b2-b665-e2e8033373a8)

## Como Contribuir
El proyecto es de código abierto y se anima a cualquier persona interesada en contribuir a hacerlo. Para contribuir al proyecto, por favor sigue estos pasos:

1. Haz un fork de este repositorio y clona el repositorio en tu máquina local.

1. Crea una nueva rama (`git checkout -b nombre-rama`) y realiza tus cambios en esa rama.

1. Haz commit a tus cambios (`git commit -m "Descripción de los cambios"`) y haz push a la rama (`git push origin nombre-rama`).

1. Abre un pull request en este repositorio y describe los cambios que has realizado.

1. Por favor, asegúrate de seguir las pautas de contribución antes de hacer un pull request.

## Mantenimiento
El conjunto de datos se actualizará regularmente para asegurarse de que se mantenga relevante y útil para la comunidad. Si encuentras algún error o tienes alguna sugerencia para mejorar el proyecto, por favor abre un issue en este repositorio.

## Licencia
El software aquí proporcionado se distribuye bajo los términos de la Licencia de Software de [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) (CC BY-NC-SA 4.0). Esto significa que los usuarios tienen el derecho de utilizar, modificar y distribuir el código fuente del scraper con la condición de que no se utilice con fines comerciales sin el permiso explícito del autor y que las obras derivadas se distribuyan bajo la misma licencia CC BY-NC-SA 4.0. Sin embargo, es importante tener en cuenta que esta licencia se aplica únicamente al software en sí, no a los datos que el scraper recopila o procesa. Los datos obtenidos por medio del scraper pueden estar sujetos a sus propias licencias o restricciones, dependiendo de su origen y de los términos establecidos por los propietarios de dichos datos

Para más información sobre la licencia, por favor lee el archivo [LICENSE](LICENSE).

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
## Projectos Relacionados

### Bogota Apartments
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/builker-col/bogota-apartments)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/datasets/erik172/bogota-apartments)

El Proyecto Bogotá Apartments es una iniciativa de código abierto que tiene como objetivo recopilar y analizar datos sobre el mercado inmobiliario de apartamentos en la ciudad de Bogotá, Colombia.

**url:** [https://github.com/builker-col/bogota-apartments](https://github.com/builker-col/bogota-apartments)

## Creditos
- [**@erik172**](https://github.com/Erik172) - Creador del proyecto y mantenedor principal.

Hecho con ❤️ por **@erik172**. 