from models.servico import Servico
from tags.combo import ComboBox
from tags.cards import Card, CardDialog


class CardServico():
    def __init__(self):
        self.servico = Servico()

    def get_cb_servico(self):
        cb = ComboBox(name_id="cb_servico", label_text="Escolha um Serviço:")
        cb.add_option("0", "--- Selecione um Serviço ---")
        lista = self.servico.read_all()
        for servico in lista:
            cb.add_option(str(servico.idt_servico), servico.nme_servico)
        return cb.make_html()

    def get_card(self, idt_servico):
        serv = self.servico.read_by_idt(idt_servico)
        card = Card(title='Dados de Serviço', width='500px')
        card.add_data_pair('Identificador:', serv.idt_servico)
        card.add_data_pair('Setor:', serv.tt_setor.sgl_setor + "-" + serv.tt_setor.nme_setor)
        card.add_data_pair('Nome do Serviço:', serv.nme_servico)
        card.add_data_pair('Dias de Serviço:', serv.num_dias_servico)
        card.add_data_pair('Valor do Serviço:', serv.vlr_servico)
        card.add_data_pair('Texto Modelo:', serv.txt_modelo_servico)
        card.add_data_pair('Status do Registro:', ('Ativo' if serv.sts_servico == 'A' else 'Inativo'))
        return card.make_html()

    def get_cardDialog(self, idt_servico):
        serv = self.servico.read_by_idt(idt_servico)
        card = CardDialog('Dados de Serviço')
        card.add_data_pair('Identificador:', serv.idt_servico)
        card.add_data_pair('Setor:', serv.tt_setor.sgl_setor + "-" + serv.tt_setor.nme_setor)
        card.add_data_pair('Nome do Serviço:', serv.nme_servico)
        card.add_data_pair('Dias de Serviço:', serv.num_dias_servico)
        card.add_data_pair('Valor do Serviço:', serv.vlr_servico)
        card.add_data_pair('Texto Modelo:', serv.txt_modelo_servico)
        card.add_data_pair('Status do Registro:', ('Ativo' if serv.sts_servico == 'A' else 'Inativo'))
        return card.make_html()
