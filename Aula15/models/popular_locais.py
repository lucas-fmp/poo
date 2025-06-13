from models.local import Local


def main():
    local = Local()

    l = local.new_object()
    l.nme_local = 'Bloco 1'
    l.lat_local = -15.768231
    l.lgt_local = -47.893483
    l.sts_local = 'A'
    local.insert(l)

    l = local.new_object()
    l.nme_local = 'Bloco 3'
    l.lat_local = -15.766582
    l.lgt_local = -47.8948107
    l.sts_local = 'A'
    local.insert(l)

    l = local.new_object()
    l.nme_local = 'Bloco 9'
    l.lat_local = -15.766089
    l.lgt_local = -47.8941911
    l.sts_local = 'A'
    local.insert(l)

    l = local.new_object()
    l.nme_local = 'Bloco 10'
    l.lat_local = -15.7651184
    l.lgt_local = -47.8944138
    l.sts_local = 'A'
    local.insert(l)

    print("4 locais criados")


if __name__ == '__main__':
    main()
