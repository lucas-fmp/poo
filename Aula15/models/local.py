# Classe Model para a entidade "tb_local"
from models.model import Model
class Local(Model):
   def __init__(self):
       super().__init__("tb_local", "idt_local")
