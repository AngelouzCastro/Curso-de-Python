import speach_recognition as sr

escuchar = sr.Recognizer()

with sr.Microphone() as micro:
    print('escuchando...')
    sonido = escuchar.listen(micro)
    texto = escuchar.recognize_google(sonido, language="es_ES")
    print(texto)
