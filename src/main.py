import requests
import xml.etree.ElementTree as ET
import csv
from dilve_api import get_book_data
from data_parsers import parse_onix_xml
from export_utils import export_to_csv

def main():
    """
    Punto de entrada principal para la aplicación DILVE Data Transformer.
    """
    # Credenciales para la API de DILVE
    user = "tu_usuario"
    password = "tu_contrase\u00f1a"

    # ISBN de ejemplo
    isbn = "9788496479685"

    try:
        # Paso 1: Obtener datos desde la API
        print("Obteniendo datos desde DILVE...")
        xml_data = get_book_data(user, password, isbn)
        print("Datos obtenidos correctamente.")

        # Paso 2: Procesar los datos
        print("Procesando los datos...")
        books = parse_onix_xml(xml_data)
        print("Datos procesados:", books)

        # Paso 3: Exportar los datos a CSV
        print("Exportando los datos a CSV...")
        export_to_csv(books, "libros.csv")
        print("Datos exportados a 'libros.csv'.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()

