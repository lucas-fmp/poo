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


class ResponsiveTable(Tag):
    def __init__(self, table, attrs=None, name_id=None):
        super().__init__("div", attrs, name_id)
        self.add_class("table-responsive")
        self._table_html = table.make_html()  # Armazena o HTML da tabela como string
        super().add_content(self._table_html)

    def make_html(self):
        attrs_str = " ".join(f"{key}='{value}'" for key, value in self.attrs.items())
        return f"<{self.tag} {attrs_str}>{self._table_html}</{self.tag}>"
