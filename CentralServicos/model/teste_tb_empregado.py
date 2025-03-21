from empregado import Empregado

# Criando o Entity
empregado = Empregado()

# Inserindo literalmente os três empregados


obj = empregado.new_object()
obj.eml_empregado = 'joaozinho@sempreceub.com'
obj.mat_empregado = '0123456789'
obj.nme_empregado = 'Joaozinho Sempre Ceub'
obj.sts_empregado = 'A'
obj.tel_empregado = '61999999999'
obj.rml_empregado = '123456'
obj.pwd_empregado = '0123456789'
empregado.insert(obj)
print(obj.idt_empregado)

obj = empregado.new_object()
obj.eml_empregado = 'mariazinha@sempreceub.com'
obj.mat_empregado = '9876543210'
obj.nme_empregado = 'Mariazinha Sempre Ceub'
obj.sts_empregado = 'A'
obj.tel_empregado = '61888888888'
obj.rml_empregado = '654321'
obj.pwd_empregado = '9876543210'
empregado.insert(obj)
print(obj.idt_empregado)

obj = empregado.new_object()
obj.eml_empregado = 'pedrinho@sempreceub.com'
obj.mat_empregado = '1234567890'
obj.nme_empregado = 'Pedrinho Sempre Ceub'
obj.sts_empregado = 'A'
obj.tel_empregado = '61977777777'
obj.rml_empregado = '456123'
obj.pwd_empregado = '1234567890'
empregado.insert(obj)
print(obj.idt_empregado)

# Fazendo algumas consultas ao banco de dados:


empregado1 = empregado.read_by_idt(1)
print(empregado1.nme_empregado)

todos = empregado.read_all()
for em in todos:
    print(em.idt_empregado, em.eml_empregado, em.mat_empregado, em.nme_empregado, em.sts_empregado, em.tel_empregado,
          em.rml_empregado, em.pwd_empregado)

print(empregado.count())
