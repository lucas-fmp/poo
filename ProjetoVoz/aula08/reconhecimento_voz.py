import speech_recognition as sr
import sounddevice as sd
import numpy as np
import soundfile as sf
import os


class RecVoz:

    def listar_dispositivos(self):
        """Lista os dispositivos de áudio disponíveis."""
        dispositivos = sd.query_devices()
        for i, dispositivo in enumerate(dispositivos):
            print(f"[{i}] {dispositivo['name']}")
        return len(dispositivos)

    def ouvir_comando(self, taxa_amostragem=16000, dispositivo=None, duracao=10):
        """Grava o áudio por um tempo determinado e transcreve usando Whisper."""
        try:
            r = sr.Recognizer()

            print(f"Gravando por {duracao} segundos...")
            audio_data = sd.rec(int(duracao * taxa_amostragem), samplerate=taxa_amostragem, channels=1,
                                device=dispositivo)
            sd.wait()
            print("Gravação finalizada.")

            # Limpar arquivos temporários
            if os.path.exists("audio_gravado.wav"):
                os.remove("audio_gravado.wav")

            # Salvar o áudio completo em um arquivo WAV mono
            sf.write("audio_gravado.wav", np.squeeze(audio_data), taxa_amostragem)

            # Transcrever o áudio completo usando Whisper
            with sr.AudioFile("audio_gravado.wav") as source:
                audio = r.record(source)
            texto = r.recognize_whisper(audio, language="pt", model='medium')  # Ajuste o modelo conforme necessário

            # Salvar a transcrição em um arquivo
            with open("transcricao_microfone.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(texto)

            return texto


        except sr.UnknownValueError:
            print("Não foi possível entender o áudio.")
            return None
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")
            return None
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return None
