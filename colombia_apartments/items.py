# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import numpy as np
from itemloaders.processors import TakeFirst, MapCompose
from unidecode import unidecode

def normalize_text_upper(text):
    # Normalizar el texto a mayusculas
    return unidecode(text.replace('\n', ' ')).upper().strip()

def normalize_text_lower(text):
    # Normalizar el texto a minusculas
    return unidecode(text.replace('\n', ' ')).lower().strip()

def replace_zero_with_nan(value):
    # Reemplazar 0 por NaN
    return None if value == 0 else value

def has_feature(value):
    return 1 if value else 0

def años_antiguedad_to_range(value):
    # verificar si es un numero
    if isinstance(value, int):
        if value < 5:
            return 'ENTRE 0 Y 5 ANOS'
        elif value < 10:
            return 'ENTRE 5 Y 10 ANOS'
        elif value < 20:
            return 'ENTRE 10 Y 20 ANOS'
        else:
            return 'MAS DE 20 ANOS'
        
    return value

class ApartmentsItem(scrapy.Item):
    """
    This class defines the structure of the items that will be scraped from the website.
    It contains the fields that will be scraped, along with their input and output processors.
    """
    codigo = scrapy.Field(output_processor = TakeFirst())

    ciudad = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    tipo_propiedad = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    tipo_operacion = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    precio_venta = scrapy.Field(
        input_processor = MapCompose(int, replace_zero_with_nan),
        output_processor = TakeFirst()
    )

    precio_arriendo = scrapy.Field(
        input_processor = MapCompose(int, replace_zero_with_nan),
        output_processor = TakeFirst()
    )

    area = scrapy.Field(
        input_processor = MapCompose(float),
        output_processor = TakeFirst()
    )

    habitaciones = scrapy.Field(
        input_processor = MapCompose(int),
        output_processor = TakeFirst()
    )

    banos = scrapy.Field(
        input_processor = MapCompose(int),
        output_processor = TakeFirst()
    )

    administracion = scrapy.Field(
        input_processor = MapCompose(int, replace_zero_with_nan),
        output_processor = TakeFirst()
    )

    parqueaderos = scrapy.Field(
        input_processor = MapCompose(int),
        output_processor = TakeFirst()
    )

    sector = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    sector_comun = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()  
    )

    estrato = scrapy.Field(
        input_processor = MapCompose(int),
        output_processor = TakeFirst()
    )

    estado = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    # antiguedad = scrapy.Field(
    #     input_processor = MapCompose(normalize_text_upper),
    #     output_processor = TakeFirst()
    # )

    antiguedad = scrapy.Field(
        input_processor = MapCompose(años_antiguedad_to_range, normalize_text_upper),
        output_processor = TakeFirst()
    )

    latitud = scrapy.Field(
        input_processor = MapCompose(float, replace_zero_with_nan),
        output_processor = TakeFirst()
    )

    longitud = scrapy.Field(
        input_processor = MapCompose(float, replace_zero_with_nan),
        output_processor = TakeFirst()
    )

    # dirrecion de la propiedad
    direccion = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    # lista de caracteristicas de la propiedad (interior)
    featured_interior = scrapy.Field(output_processor = MapCompose(normalize_text_upper))

    # lista de caracteristicas de la propiedad (exterior)
    featured_exterior = scrapy.Field(output_processor = MapCompose(normalize_text_upper))

    # lista de caracteristicas de la propiedad (zona comun)
    featured_zona_comun = scrapy.Field(output_processor = MapCompose(normalize_text_upper))

    # lista de caracteristicas de la propiedad (sector)
    featured_sector = scrapy.Field(output_processor = MapCompose(normalize_text_upper))

    descripcion = scrapy.Field(
        input_processor = MapCompose(normalize_text_lower),
        output_processor = TakeFirst()
    )

    compañia = scrapy.Field(
        input_processor = MapCompose(normalize_text_upper),
        output_processor = TakeFirst()
    )

    imagenes = scrapy.Field()

    website = scrapy.Field(output_processor = TakeFirst())

    last_view = scrapy.Field(output_processor = TakeFirst())

    datetime = scrapy.Field(output_processor = TakeFirst())

    def __str__(self) -> str:
        return f'{self["codigo"]} - {self["tipo_propiedad"]} - {self["tipo_operacion"]}'