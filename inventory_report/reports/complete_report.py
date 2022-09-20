from abc import abstractmethod
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self):
        pass

    @abstractmethod
    def generate(data):
        products_quantity = {}
        quantity_report = ''

        for product in data:
            products_quantity[product["nome_da_empresa"]] = (
                products_quantity.get(product["nome_da_empresa"], 0) + 1
            )

        for company in products_quantity.items():
            quantity_report += f"- {company[0]}: {company[1]}\n"

        return (
            f"{SimpleReport.generate(data)}\n"
            "Produtos estocados por empresa:\n"
            f"{quantity_report}"
        )
