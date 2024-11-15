# TODO импортировать необходимые молули
import csv
import json
INPUT = "input.csv"
OUTPUT = "output.json"
# TODO считать содержимое csv файла
def task() -> None:
    with open(INPUT) as f:
        lines = [line for line in csv.DictReader(f)]
# TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT, "w") as f:
        json.dump(lines, f, indent=4)
if __name__ == '__main__':
    task()
    with open(OUTPUT) as output_f:
        for line in output_f:
            print(line, end="")