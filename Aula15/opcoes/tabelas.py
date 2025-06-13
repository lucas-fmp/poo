from models.servico import Servico
from tags.tables import Table, StripedTable, HoverableTable


class TabelaServico():
    def __init__(self):
        self.servico = Servico()

    def get_table_basic(self):
        tab = Table(headers=['Identificador', 'Setor', 'Serviço', 'Tempo (dias)', 'Valor (R$)'])
        servicos = self.servico.read_all()
        for serv in servicos:
            tab.add_row(
                [serv.idt_servico, serv.tt_setor.nme_setor, serv.nme_servico, serv.num_dias_servico, serv.vlr_servico])
        return tab.make_html()

    def get_table_striped(self):
        tab = StripedTable(headers=['Identificador', 'Setor', 'Serviço', 'Tempo (dias)', 'Valor (R$)'])
        servicos = self.servico.read_all()
        for serv in servicos:
            tab.add_row(
                [serv.idt_servico, serv.tt_setor.nme_setor, serv.nme_servico, serv.num_dias_servico, serv.vlr_servico])
        return tab.make_html()

    def get_table_hover(self):
        tab = HoverableTable(headers=['Identificador', 'Setor', 'Serviço', 'Tempo (dias)', 'Valor (R$)'])
        servicos = self.servico.read_all()
        for serv in servicos:
            tab.add_row(
                [serv.idt_servico, serv.tt_setor.nme_setor, serv.nme_servico, serv.num_dias_servico, serv.vlr_servico])
        return tab.make_html()
