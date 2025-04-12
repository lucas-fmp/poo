import speech_recognition as sr

# Cria um objeto Recognizer
reconhecedor = sr.Recognizer()

# Abre o microfone
with sr.Microphone() as fonte:
    print("Fale alguma coisa...")
    audio = reconhecedor.listen(fonte)

# Transcreve o áudio em texto
try:
    texto = reconhecedor.recognize_google(audio, language="pt-BR")
    print("Você disse: " + texto)
except sr.UnknownValueError:
    print("Não foi possível entender o áudio")
except sr.RequestError as e:
    print("Erro ao conectar com a API: " + str(e))
