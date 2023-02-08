import csv
import json
import io
import os


def lambda_handler(event, context):
    os.environ['SERVICES_API_BASE_URL'] = 'http://localhost:4566'
    # Pobieranie danych z mockowanego S3 Bucket
    csv_file_content = event['data']
    file = io.StringIO(csv_file_content)
    
    reader = csv.DictReader(file)
    color_data = []

    for row in reader:
        color = row['color']
        hex_color = row['value']
        if len(hex_color) == 4:
            hex_color = '#' + hex_color[1] + hex_color[1] + hex_color[2] + hex_color[2] + hex_color[3] + hex_color[3]
        try:
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
        except ValueError:
            print(f"Invalid value: {hex_color}")
            continue
        color_data.append({
            'color': color,
            'hex': hex_color,
            'rgb': rgb
        })
    
    # Zwróć wynik jako wyjście funkcji
    return {
        'data': color_data
    }