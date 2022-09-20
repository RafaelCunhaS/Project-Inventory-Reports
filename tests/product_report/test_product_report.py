from inventory_report.inventory.product import Product


def test_relatorio_produto():
    sut_product = Product(
        "randomID",
        "Produto Genérico",
        "Empresa Genérica",
        2022,
        2025,
        "123456789",
        "em temperatura ambiente",
    )

    assert sut_product.__repr__() == (
        "O produto Produto Genérico"
        " fabricado em 2022"
        " por Empresa Genérica com validade"
        " até 2025"
        " precisa ser armazenado em temperatura ambiente."
    )
