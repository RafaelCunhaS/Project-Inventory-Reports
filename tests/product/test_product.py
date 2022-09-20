from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        "randomID",
        "Produto Genérico",
        "Empresa Genérica",
        2022,
        2025,
        "123456789",
        "temperatura ambiente",
    )

    assert new_product.id == "randomID"
    assert new_product.nome_do_produto == "Produto Genérico"
    assert new_product.nome_da_empresa == "Empresa Genérica"
    assert new_product.data_de_fabricacao == "2022"
    assert new_product.data_de_validade == "2025"
    assert new_product.numero_de_serie == "123456789"
    assert new_product.instrucoes_de_armazenamento == "temperatura ambiente"
