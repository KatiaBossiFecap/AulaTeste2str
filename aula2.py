import speech_recognition as sr
import streamlit as st

def ouvir_numero():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Diga um número:")
        audio = recognizer.listen(source, timeout=10)

    try:
        numero_falado = recognizer.recognize_google(audio, language="pt-BR")
        st.success(f"Número reconhecido: {numero_falado}")
        numero = interpretar_numero(numero_falado)
        return numero
    except sr.UnknownValueError:
        st.error("Não foi possível entender o número.")
        return None
    except sr.RequestError as e:
        st.error(f"Erro na requisição para o serviço de reconhecimento de voz; {e}")
        return None

def interpretar_numero(numero_falado):
    numeros_texto_para_numero = {
        "zero": 0, "um": 1, "dois": 2, "três": 3, "quatro": 4,
        "cinco": 5, "seis": 6, "sete": 7, "oito": 8, "nove": 9
    }

    # Tentar converter a palavra para número
    return numeros_texto_para_numero.get(numero_falado.lower(), None)

def gerar_tabuada(numero):
    if numero is None:
        return []

    tabuada = []
    for i in range(1, 11):
        resultado = numero * i
        tabuada.append(f"{numero} x {i} = {resultado}")
    return tabuada

def main():
    st.title("Tabuada Generator")
    numero = ouvir_numero()

    if numero is not None:
        st.subheader(f"Tabuada do {numero}")
        tabuada = gerar_tabuada(numero)
        for item in tabuada:
            st.write(item)

if __name__ == "__main__":
    main()
