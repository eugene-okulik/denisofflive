import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("path_folder", help="Задайте путь к папке с лог-файлами")
parser.add_argument("--text", help="Введите текст поиска")
args = parser.parse_args()

files = os.listdir(args.path)

for file in files:
    with open(os.path.join(args.path, file)) as logs:
        for i, line in enumerate(logs):
            if args.value in line:
                words = line.split()
                idx = words.index(args.value)
                start_idx = max(idx - 5, 0)
                end_idx = min(idx + 5, len(words))
                context = " ".join(words[start_idx:end_idx])
                print(f"Файл: {file}, в строке {i}: {context}")
