import requests

API_BASE_URL = "https://www.dilve.es/dilve/dilve/accion.do"

def get_book_data(user, password, isbn, metadataformat="ONIX"):
    params = {
        "user": user,
        "password": password,
        "accion": "getRecordsX",
        "identifier": isbn,
        "metadataformat": metadataformat,
    }
    response = requests.get(API_BASE_URL, params=params)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

