from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    def __init__(self):
        pass

    @staticmethod
    def import_data(path, type):
        if path.endswith(".csv"):
            data = CsvImporter.import_data(path)

            return (
                SimpleReport.generate(data)
                if type == "simples"
                else CompleteReport.generate(data)
            )

        elif path.endswith(".json"):
            data = JsonImporter.import_data(path)

            return (
                SimpleReport.generate(data)
                if type == "simples"
                else CompleteReport.generate(data)
            )

        else:
            data = XmlImporter.import_data(path)

            return (
                SimpleReport.generate(data)
                if type == "simples"
                else CompleteReport.generate(data)
            )
