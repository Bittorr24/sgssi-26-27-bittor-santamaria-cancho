from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException




def cifradoCesarFuerzaBruta(Frase): 
    for i in range(1,26):
        Frase2=""
        for j in range(len(Frase)):
            letra = Frase[j].lower()
            if 'a' <= letra <= 'z':
                letra= chr((ord(letra) - ord('a') + 1) % 26 + ord('a'))
            Frase2=Frase2 + letra
        Frase=Frase2
        try:
            idioma = detect(Frase)
            if idioma == "es":
                print (Frase)
                return Frase
        except LangDetectException:
            print("No se pudo detectar un idioma válido o el texto no tiene sentido.")
    
Frase ="Uunejvxb dw vdwmx wdnex jzdr, nw wdnbcaxb lxajixwnb"
cifradoCesarFuerzaBruta(Frase)