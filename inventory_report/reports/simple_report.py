from datetime import date


class SimpleReport:
    def __init__(self):
        pass

    @staticmethod
    def generate(data):
        min_year = min([product["data_de_fabricacao"] for product in data])

        closest_expiration = date.max
        for year in [product["data_de_validade"] for product in data]:
            formatted_year = date.fromisoformat(year)
            if (
                formatted_year >= date.today()
                and formatted_year < closest_expiration
            ):
                closest_expiration = formatted_year

        companies = [product["nome_da_empresa"] for product in data]
        most_products = max(set(companies), key=companies.count)

        return (
            f"Data de fabricação mais antiga: {min_year}\n"
            f"Data de validade mais próxima: {closest_expiration}\n"
            f"Empresa com mais produtos: {most_products}"
        )
