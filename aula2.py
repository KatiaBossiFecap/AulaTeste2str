import streamlit as st
import speech_recognition as sr

def transcrever_audio(arquivo_audio):
    recognizer = sr.Recognizer()
    
    # Usar o arquivo de áudio enviado pelo usuário
    with sr.AudioFile(arquivo_audio) as source:
        st.write("Processando áudio...")
        audio = recognizer.record(source)
    
    try:
        texto_transcrito = recognizer.recognize_google(audio, language="pt-BR")
        st.write("Texto transcrito:", texto_transcrito)

        # Salvar o texto transcrito em um arquivo
        nome_arquivo_saida = "transcricao.txt"
        with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto_transcrito)

        st.success(f"Transcrição salva em '{nome_arquivo_saida}'.")
    
    except sr.UnknownValueError:
        st.error("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        st.error(f"Erro na requisição para o serviço de reconhecimento de voz; {e}")

def main():
    st.title("Transcrição de Áudio usando Streamlit")

    uploaded_file = st.file_uploader("Faça upload do arquivo de áudio (formato suportado: WAV)", type=["wav"])

    if uploaded_file is not None:
        transcrever_audio(uploaded_file)

main()
