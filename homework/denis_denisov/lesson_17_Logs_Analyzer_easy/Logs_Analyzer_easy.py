import os


def find_text_in_files(folder_path, text_to_find):
    files = os.listdir(folder_path)

    for file_name in files:
        with open(os.path.join(folder_path, file_name)) as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines):
                if text_to_find in line:
                    start = max(line.index(text_to_find) - 5, 0)
                    end = min(line.index(text_to_find) + len(text_to_find) + 5, len(line))
                    print(f"Найден '{text_to_find}' в файле {file_name} на строке {line_number + 1}: {line[start:end]}")


# Пример вызова функции с указанием пути к папке с логами и текстом для поиска
path = r'D:\denisofflive\homework\eugene_okulik\data\logs'
text = "Sql exception for geometry"
find_text_in_files(path, text)
