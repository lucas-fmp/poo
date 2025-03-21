from local import Local

# Criando o Entity
local = Local()

# Inserindo literalmente os três locais


obj = local.new_object()
obj.nme_local = 'Bloco 1'
obj.lat_local = -15.7693515
obj.lgt_local = -47.8917583
obj.sts_local = 'A'
local.insert(obj)
print(obj.idt_local)

obj = local.new_object()
obj.nme_local = 'Bloco 7'
obj.lat_local = -15.7661688
obj.lgt_local = -47.89388
obj.sts_local = 'A'
local.insert(obj)
print(obj.idt_local)

obj = local.new_object()
obj.nme_local = 'Bloco 10'
obj.lat_local = -15.7653195
obj.lgt_local = -47.8943279
obj.sts_local = 'A'
local.insert(obj)
print(obj.idt_local)

# Fazendo algumas consultas ao banco de dados:


bloco1 = local.read_by_idt(12)
print(bloco1.nme_local)

todos = local.read_all()
for bl in todos:
    print(bl.idt_local, bl.nme_local, bl.lat_local, bl.lgt_local, bl.sts_local)

print(local.count())
