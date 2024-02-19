import os

main_file_path = "D:/..."
file_name = "example.txt"
street_file_path = "D:/exampleFile.txt"

if not os.path.exists(main_file_path):
    os.makedirs(main_file_path)

with open(os.path.join(main_file_path, file_name), "r", encoding="utf-8") as file:
    for line in file:
        klasor_adi = line.strip()
        file_path = os.path.join(main_file_path, klasor_adi)
        os.makedirs(file_path, exist_ok=True)

        with open(street_file_path, "r", encoding="utf-8") as dosyalama:
            for street_line in dosyalama:
                lower_file_name = street_line.strip()
                lower_file_path = os.path.join(file_path, lower_file_name)
                os.makedirs(lower_file_path, exist_ok=True)

print("Operation  succesfully completed.")