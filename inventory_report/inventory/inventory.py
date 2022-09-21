import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __init__(self):
        pass

    @staticmethod
    def import_data(path, type):
        if path.endswith('.csv'):
            with open(path) as file:
                reader = csv.DictReader(file)
                data = []
                for row in reader:
                    data.append(row)

                if type == "simples":
                    return SimpleReport.generate(data)
                else:
                    return CompleteReport.generate(data)

        elif path.endswith('.json'):
            with open(path) as file:
                data = json.loads(file.read())

                if type == "simples":
                    return SimpleReport.generate(data)
                else:
                    return CompleteReport.generate(data)

        else:
            with open(path) as file:
                tree = ET.parse(file)
                root = tree.getroot()
                data = []

                product = {}
                for child in root.iter():
                    if '\n' not in child.text:
                        product[child.tag] = child.text
                    if child.tag == 'instrucoes_de_armazenamento':
                        data.append(product)
                        product = {}

                if type == "simples":
                    return SimpleReport.generate(data)
                else:
                    return CompleteReport.generate(data)
