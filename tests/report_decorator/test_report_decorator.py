from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from unittest.mock import MagicMock


MockSimpleReport = SimpleReport()
MockSimpleReport.generate = MagicMock(
    return_value="""
Data de fabricação mais antiga: 10-05-2022
Data de validade mais próxima: 14-06-2021
Empresa com mais produtos: Farinini"""
)


def test_decorar_relatorio():
    lista = []
    sut = ColoredReport(MockSimpleReport).generate(lista)
    sut_splitted = sut.split("\n")
    sut_text, sut_date = (
        sut_splitted[1].split(":")[0],
        sut_splitted[1].split(":")[1],
    )
    sut_company = sut_splitted[-1]

    assert "\033[32m" in sut_text
    assert "\033[36m" in sut_date
    assert "\033[31m" in sut_company
    assert "\033[0m" in sut
