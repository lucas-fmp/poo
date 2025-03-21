from setor import Setor
from prestador import Prestador

setor = Setor()
prestador = Prestador()

ger = setor.new_object()
ger.sgl_setor = 'GER'
ger.nme_setor = 'Gerência Geral'
ger.eml_setor = 'ger_geral@gmail.com'
ger.sts_setor = 'A'

setor.insert(ger)
print(ger.idt_setor)

adm = prestador.new_object()
adm.mat_prestador = '1'
adm.nme_prestador = 'Administrador'
adm.eml_prestador = 'administrador@gmail.com'
adm.sts_prestador = 'A'
adm.pwd_prestador = '40bd001563085fc35165329ea1ff5c5ecbdbbeef'  # SHA('123')
adm.cod_setor = 5
prestador.insert(adm)
print(adm.idt_prestador)
