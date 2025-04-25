from tags.tag import Tag


class Table(Tag):
    def __init__(self, headers=None, attrs=None, name_id=None):
        super().__init__("table", attrs, name_id)
        self.add_class("table")
        self.headers = headers or []
        self.rows = []
        self._thead = Tag("thead")
        self._tbody = Tag("tbody")
        self._thead_html = ""  # Armazena o HTML do thead como string
        self._tbody_html = ""  # Armazena o HTML do tbody como string

        self._update_thead()
        self._update_tbody()

    def add_header(self, header_text):
        self.headers.append(header_text)
        self._update_thead()

    def set_headers(self, headers):
        self.headers = headers
        self._update_thead()

    def _update_thead(self):
        self._thead_html = ""  # Reinicializa a string
        header_row_content = ""
        for header in self.headers:
            th = Tag("th", content=header)
            header_row_content += th.make_html()
        self._thead_html = f"<thead{' ' + ' '.join(f'{key}=\'{value}\'' for key, value in self._thead.attrs.items()) if self._thead.attrs else ''}><tr>{header_row_content}</tr></thead>"
        super().add_content(self._thead_html)

    def add_row(self, row_data):
        self.rows.append(row_data)
        self._update_tbody()

    def set_rows(self, rows):
        self.rows = rows
        self._update_tbody()

    def _update_tbody(self):
        self._tbody_html = ""
        tbody_content = ""
        for row_data in self.rows:
            row_content = ""
            for cell_data in row_data:
                td = Tag("td", content=str(cell_data))
                row_content += td.make_html()
            tbody_content += f"<tr>{row_content}</tr>"
        self._tbody_html = f"<tbody{' ' + ' '.join(f'{key}=\'{value}\'' for key, value in self._tbody.attrs.items()) if self._tbody.attrs else ''}>{tbody_content}</tbody>"
        super().add_content(self._tbody_html)

    def make_html(self):
        attrs_str = " ".join(f"{key}='{value}'" for key, value in self.attrs.items())
        return f"<{self.tag} {attrs_str}>{self._thead_html}{self._tbody_html}</{self.tag}>"


class StripedTable(Table):
    def __init__(self, headers=None, attrs=None, name_id=None):
        super().__init__(headers, attrs, name_id)
        self.add_class("table-striped")


class BorderedTable(Table):
    def __init__(self, headers=None, attrs=None, name_id=None):
        super().__init__(headers, attrs, name_id)
        self.add_class("table-bordered")


class HoverableTable(Table):
    def __init__(self, headers=None, attrs=None, name_id=None):
        super().__init__(headers, attrs, name_id)
        self.add_class("table-hover")


class DarkTable(Table):
    def __init__(self, headers=None, attrs=None, name_id=None):
        super().__init__(headers, attrs, name_id)
        self.add_class("table-dark")


class ResponsiveTable(Table):
    def __init__(self, table, attrs=None, name_id=None):
        super().__init__("div", attrs, name_id)
        self.add_class("table-responsive")
        self._table_html = table.make_html()  # Armazena o HTML da tabela como string
        super().add_content(self._table_html)

    def make_html(self):
        attrs_str = " ".join(f"{key}='{value}'" for key, value in self.attrs.items())
        return f"<{self.tag} {attrs_str}>{self._table_html}</{self.tag}>"


# Exemplo de uso (deve funcionar com a sua classe Tag original)
if __name__ == "__main__":
    # Tabela básica
    table_basica = Table(headers=["Nome", "Idade", "Profissão"])
    table_basica.add_class("shadow")
    table_basica.add_row(["Ana", 25, "Engenheira"])
    table_basica.add_row(["Pedro", 32, "Analista"])
    print("Tabela Básica:")
    print(table_basica.make_html())
    print("-" * 30)

    # Tabela com linhas tracejadas
    table_tracejada = StripedTable(headers=["Produto", "Preço"])
    table_tracejada.add_class("shadow")
    table_tracejada.add_row(["Camiseta", "R$ 29,90"])
    table_tracejada.add_row(["Calça Jeans", "R$ 89,50"])
    table_tracejada.add_row(["Meia", "R$ 9,50"])
    print("Tabela Tracejada:")
    print(table_tracejada.make_html())
    print("-" * 30)

    # Tabela com bordas
    table_bordas = BorderedTable(headers=["Serviço", "Valor"])
    table_bordas.add_class("shadow")
    table_bordas.add_row(["Consultoria", "R$ 500,00"])
    table_bordas.add_row(["Treinamento", "R$ 800,00"])
    print("Tabela com Bordas:")
    print(table_bordas.make_html())
    print("-" * 30)

    # Tabela com efeito hover
    table_hover = HoverableTable(headers=["Item", "Quantidade"])
    table_hover.add_class("shadow")
    table_hover.add_row(["Maçã", 5])
    table_hover.add_row(["Banana", 10])
    print("Tabela com Hover:")
    print(table_hover.make_html())
    print("-" * 30)

    # Tabela escura
    table_dark = DarkTable(headers=["Mês", "Faturamento"])
    table_dark.add_class("shadow")
    table_dark.add_row(["Janeiro", "R$ 10.000,00"])
    table_dark.add_row(["Fevereiro", "R$ 12.500,00"])
    print("Tabela Escura:")
    print(table_dark.make_html())
    print("-" * 30)

    # Tabela responsiva
    tabela_para_tornar_responsiva = Table(
        headers=["Nome Completo", "Endereço", "Telefone", "Email", "Data de Cadastro"])
    tabela_para_tornar_responsiva.add_class("shadow")
    tabela_para_tornar_responsiva.add_row(
        ["Carlos Alberto Silva", "Rua das Flores, 123", "(11) 9999-8888", "carlos.silva@email.com", "2024-01-15"])
    tabela_para_tornar_responsiva.add_row(
        ["Mariana Oliveira Souza", "Avenida Brasil, 456", "(21) 8888-7777", "mariana.souza@email.com", "2024-02-20"])
    tabela_responsiva = ResponsiveTable(tabela_para_tornar_responsiva)
    print("Tabela Responsiva:")
    print(tabela_responsiva.make_html())
    print("-" * 30)
