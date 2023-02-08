import csv
import json

def main():
    csv_files = ['example.csv', 'example1.csv', 'example2.csv']
    color_data = []

    for csv_file in csv_files:
        with open(csv_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                color = row['color']
                hex_color = row['value']
                if len(hex_color) == 4:
                    hex_color = '#' + hex_color[1] + hex_color[1] + hex_color[2] + hex_color[2] + hex_color[3] + hex_color[3]
                try:
                    rgb = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
                except ValueError:
                    print(f"Invalid value in {csv_file}: {hex_color}")
                    continue
                color_data.append({
                    'color': color,
                    'hex': hex_color,
                    'rgb': rgb
                })

    with open('colors.json', 'w') as f:
        json.dump(color_data, f)
    return color_data

result = main()
print(result)