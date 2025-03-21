from model import Model


class Empregado(Model):
    def __init__(self):
        super().__init__("tb_empregado", "idt_empregado")
