from tags.tag import Tag


class Card:
    def __init__(self, title, width="auto"):
        self.title = title
        self.data_pairs = {}
        self.width = width

    def add_data_pair(self, label, value):
        self.data_pairs[label] = value

    def make_html(self):
        style = f"width: {self.width}; padding: 10px;"
        card = Tag("div", {"class": "card", "style": style})

        # Título do Card
        card_header = Tag("div", {"class": "card-header"}, content=self.title)
        card.add_content(card_header.make_html())

        # Corpo do Card
        card_body = Tag("div", {"class": "card-body"})

        # Construir os pares rótulo/valor
        for label, value in self.data_pairs.items():
            row = Tag("div", {"class": "row"})
            label_col = Tag("div", {"class": "col-sm-4"}, content=label)
            value_col = Tag("div", {"class": "col-sm-8"}, content=f"<strong>{str(value)}</strong>")
            row.add_content(label_col.make_html() + value_col.make_html())
            card_body.add_content(row.make_html())

        card.add_content(card_body.make_html())

        return card.make_html()


class CardDialog(Card):
    def make_html(self):
        conteudo = ""
        # Construir os pares rótulo/valor
        for label, value in self.data_pairs.items():
            row = Tag("div", {"class": "row"})
            label_col = Tag("div", {"class": "col-sm-4"}, content=label)
            value_col = Tag("div", {"class": "col-sm-8"}, content=f"<strong>{str(value)}</strong>")
            row.add_content(label_col.make_html() + value_col.make_html())
            conteudo += row.make_html()
        return conteudo


# Exemplo de uso
if __name__ == "__main__":
    card = Card("Detalhes do Usuário", width="300px")
    card.add_data_pair("Nome", "João da Silva")
    card.add_data_pair("Idade", 30)
    card.add_data_pair("Cidade", "São Paulo")
    card.add_data_pair("Profissão", "Desenvolvedor")

    print(card.make_html())
