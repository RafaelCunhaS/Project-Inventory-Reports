import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith('.xml'):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            tree = ET.parse(file)
            root = tree.getroot()
            data = []

            product = {}
            for child in root.iter():
                if "\n" not in child.text:
                    product[child.tag] = child.text
                if child.tag == "instrucoes_de_armazenamento":
                    data.append(product)
                    product = {}

            return data
