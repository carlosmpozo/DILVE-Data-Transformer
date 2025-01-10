import csv

def export_to_csv(data, filename="output.csv"):
    if not data:
        raise ValueError("No hay datos para exportar.")

    keys = data[0].keys()
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

