class Tag:
    def __init__(self, tag, attrs=None, name_id=None, content=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.content = content

        if name_id is not None:
            self.add_attr("name", name_id)
            self.add_attr("id", name_id)

    def add_attr(self, key, value):
        self.attrs[key] = value

    def add_class(self, class_name):
        if "class" in self.attrs:
            self.attrs["class"] += f" {class_name}"
        else:
            self.attrs["class"] = class_name

    def add_content(self, content):
        if self.content is None:
            self.content = content
        else:
            self.content += content

    def make_html(self):
        attrs_str = " ".join(f"{key}='{value}'" for key, value in self.attrs.items())
        if self.content is not None:
            return f"<{self.tag} {attrs_str}>{self.content}</{self.tag}>"
        else:
            return f"<{self.tag} {attrs_str}>"

if __name__ == "__main__":
    inp = Tag(tag='input', name_id='nome')
    inp.add_attr('style', 'border: 5px solid orange')
    inp.add_attr('size', '50')
    print(inp.make_html())

    btn = Tag(tag='button')
    btn.add_content('Mostrar Valor da Caixa de Texto')
    btn.add_attr('onclick', 'mostrar()')
    btn.add_class('btn btn-primary')
    print(btn.make_html())