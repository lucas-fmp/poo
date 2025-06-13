from models.setor import Setor
from models.local import Local
from tags.combo import ComboBox, OpenComboBox


class ComboSetor():
    def __init__(self):
        self.setor = Setor()

    def get_cb_all(self):
        cb = ComboBox(name_id="cb_setor", label_text="Escolha um Setor:")
        cb.add_option("0", "--- Selecione um Setor ---")
        lista = self.setor.read_all()
        for setor in lista:
            cb.add_option(str(setor.idt_setor), (setor.sgl_setor + " - " + setor.nme_setor) )
        return cb.make_html()

    def get_cb_filter(self, nme_setor):
        cb = ComboBox(name_id="cb_setor_filter", label_text="Escolha um Setor:")
        cb.add_option("0", "--- Selecione um Setor ---")
        lista = self.setor.read_by_like('nme_setor', nme_setor)
        for setor in lista:
            cb.add_option(str(setor.idt_setor), setor.sgl_setor + " - " + setor.nme_setor)
        return cb.make_html()


class ComboLocal():
    def __init__(self):
        self.local = Local()

    def get_cb_all(self):
        cb = OpenComboBox(name_id="cb_local", label_text="Escolha um Local:")
        cb.add_option("0", "--- Selecione um Local ---")
        lista = self.local.read_all()
        for local in lista:
            cb.add_option(str(local.idt_local), local.nme_local)
        return cb.make_html()

    def get_cb_filter(self, nme_local):
        cb = OpenComboBox(name_id="cb_local_filter", label_text="Escolha um local:")
        cb.add_option("0", "--- Selecione um local ---")
        lista = self.local.read_by_like('nme_local', nme_local)
        for local in lista:
            cb.add_option(str(local.idt_local), local.nme_local)
        return cb.make_html()
