from reconhecimento_voz import RecVoz

if __name__ == '__main__':
    rv = RecVoz()
    rv.listar_dispositivos()
    print('-' * 30)
    disp = int(input('Qual dispositivo vai usar? '))
    tempo = int(input('Quantos segundos vai gravar? '))
    print('-' * 30)
    texto = rv.ouvir_comando(dispositivo=disp, duracao=tempo)
    print('Texto reconhecido: {}'.format(texto))
    print('-' * 30)
