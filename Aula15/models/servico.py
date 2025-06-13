# Classe Model para a entidade "tb_servico"
from models.model import Model
class Servico(Model):
   def __init__(self):
       super().__init__("tb_servico", "idt_servico")
