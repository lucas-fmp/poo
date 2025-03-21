from model import Model


class Prestador(Model):
    def __init__(self):
        super().__init__("tb_prestador", "idt_prestador")
