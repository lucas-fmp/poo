from models.setor import Setor


def main():
    setor = Setor()

    s = setor.new_object()
    s.sgl_setor = 'RH'
    s.nme_setor = 'Recursos Humanos'
    s.eml_setor = 'rh@empresa.com'
    s.sts_setor = 'A'
    setor.insert(s)

    s = setor.new_object()
    s.sgl_setor = 'FIN'
    s.nme_setor = 'Financeiro'
    s.eml_setor = 'fin@empresa.com'
    s.sts_setor = 'A'
    setor.insert(s)

    s = setor.new_object()
    s.sgl_setor = 'TI'
    s.nme_setor = 'Tecnologia da Informação'
    s.eml_setor = 'ti@empresa.com'
    s.sts_setor = 'A'
    setor.insert(s)

    print("3 setores criados")


if __name__ == '__main__':
    main()
