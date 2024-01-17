import speech_recognition as sr
def transcrever_audio():
    recognizer = sr.Recognizer()
    with sr.AudioFile("tempo.wav") as source:
        print("Processando áudio...")
        audio = recognizer.record(source)  # Captura o áudio do arquivo "audio.wav"
    try:
        texto_transcrito = recognizer.recognize_google(audio, language="pt-BR")
        print("Texto transcrito:", texto_transcrito)

        # Salvar o texto transcrito em um arquivo
        with open("transcricao.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(texto_transcrito)

        print("Transcrição salva em 'transcricao.txt'.")
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro na requisição para o serviço de reconhecimento de voz; {e}")
transcrever_audio()
