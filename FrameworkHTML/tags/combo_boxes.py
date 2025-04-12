from tags.tag import Tag


class ComboBox(Tag):
    def __init__(self, name_id, label_text=None, options=None, attrs=None):
        super().__init__("select", attrs, name_id)
        self.options = options or {}
        self.label_text = label_text
        self.add_class('form-select')

    def add_option(self, key, text, selected=False):
        self.options[key] = {"text": text, "selected": selected}

    def remove_option(self, key):
        if key in self.options:
            del self.options[key]

    def clear_options(self):
        self.options.clear()

    def get_option_count(self):
        return len(self.options)

    def add_optgroup(self, label, options):
        optgroup_html = f'<optgroup label="{label}">\n'
        for key, text in options.items():
            optgroup_html += f'    <option value="{key}">{text}</option>\n'
        optgroup_html += '</optgroup>\n'
        return optgroup_html

    def get_attrs_str(self):
        return " ".join(f'{key}="{value}"' for key, value in self.attrs.items())

    def make_html(self):
        options_html = ""
        for key, option_data in self.options.items():
            selected_attr = ' selected' if option_data.get('selected') else ''
            options_html += f'    <option value="{key}"{selected_attr}>{option_data["text"]}</option>\n'

        select_html = f'<select {self.get_attrs_str()}>\n{options_html}</select>'

        if self.label_text:
            return f'<label for="{self.attrs["id"]}">{self.label_text}</label>\n{select_html}'
        else:
            return select_html


class OpenComboBox(ComboBox):
    def __init__(self, name_id, label_text=None, options=None, attrs=None):
        super().__init__(name_id, label_text, options, attrs)
        self.add_attr("multiple", "multiple")

if __name__ == "__main__":
    cb = ComboBox(name_id="cb", label_text="Unidade da Federação")
    cb.add_option('RJ', 'Rio de Janeiro')
    cb.add_option('DF', 'Distrito Federal')
    cb.add_option('SP', 'São Paulo')
    print(cb.make_html())

    ocb = OpenComboBox(name_id="ocb", label_text="Unidade da Federação")
    ocb.add_option('RJ', 'Rio de Janeiro')
    ocb.add_option('DF', 'Distrito Federal')
    ocb.add_option('SP', 'São Paulo')
    print(ocb.make_html())