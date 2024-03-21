import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("path_folder", help="Путь к папке с логами")
parser.add_argument("--text", help="Текст поиска в логе")
args = parser.parse_args()

files = os.listdir(args.path)

for file in files:
    with open(os.path.join(args.path, file)) as logs:
        for i, line in enumerate(logs):
            if args.value in line:
                print(f"Файл: {file}, строка {i}: {line}")
