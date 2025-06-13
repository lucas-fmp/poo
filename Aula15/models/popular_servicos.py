from models.servico import Servico


def main():
    servico = Servico()

    s = servico.new_object()
    s.nme_servico = 'Férias'
    s.num_dias_servico = 3
    s.vlr_servico = 120
    s.txt_modelo_servico = '''
   Início: DD/MM/AAAA
   Término: DD/MM/AAAA
   Adiantamento de 13º: Sim/Não
   '''
    s.sts_servico = 'A'
    s.cod_setor = 1
    servico.insert(s)

    s = servico.new_object()
    s.nme_servico = 'Frequência'
    s.num_dias_servico = 1
    s.vlr_servico = 50
    s.txt_modelo_servico = '''
       Dia ocorrência: DD/MM/AAAA
       Ocorrência: XXXXXXXXXXXXXXXXX
       '''
    s.sts_servico = 'A'
    s.cod_setor = 1
    servico.insert(s)

    s = servico.new_object()
    s.nme_servico = 'Atestado Médico'
    s.num_dias_servico = 1
    s.vlr_servico = 50
    s.txt_modelo_servico = '''
       Início: DD/MM/AAAA
       Término: DD/MM/AAAA
       '''
    s.sts_servico = 'A'
    s.cod_setor = 1
    servico.insert(s)

    s = servico.new_object()
    s.nme_servico = 'Nota Fiscal'
    s.num_dias_servico = 1
    s.vlr_servico = 60
    s.txt_modelo_servico = '''
       Equipamento: XXXXXXXXXX
       Valor: 99999,99
       '''
    s.sts_servico = 'A'
    s.cod_setor = 2
    servico.insert(s)

    s = servico.new_object()
    s.nme_servico = 'Formatação de Desktop'
    s.num_dias_servico = 2
    s.vlr_servico = 200
    s.txt_modelo_servico = '''
       Patrimônio: XXXXXX
       Observações: XXXXXX
       '''
    s.sts_servico = 'A'
    s.cod_setor = 3
    servico.insert(s)

    s = servico.new_object()
    s.nme_servico = 'Instalação de Programa'
    s.num_dias_servico = 1
    s.vlr_servico = 50
    s.txt_modelo_servico = '''
           Patrimônio: XXXXXX
           Software: XXXXXX
           '''
    s.sts_servico = 'A'
    s.cod_setor = 3
    servico.insert(s)

    print("6 serviços criados")


if __name__ == '__main__':
    main()
