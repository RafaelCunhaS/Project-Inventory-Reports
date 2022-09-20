import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __init__(self):
        pass

    @staticmethod
    def import_data(path, type):
        with open(path) as file:
            reader = csv.DictReader(file)
            data = []
            for row in reader:
                data.append(row)

            if type == "simples":
                return SimpleReport.generate(data)
            else:
                return CompleteReport.generate(data)
