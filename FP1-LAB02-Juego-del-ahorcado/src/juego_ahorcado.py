import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)

def normalizar(cadena):

    cadena = cadena.lower()
    cadena = cadena.strip()

    for letra in cadena :
        if letra == "í":
            cadena = cadena.replace(letra,'i')
        elif letra == 'á':
            cadena = cadena.replace(letra,'a')
        elif letra == 'é':
            cadena = cadena.replace(letra,'e')
        elif letra == 'ó':
            cadena = cadena.replace(letra,'o')
        elif letra == 'ú':
            cadena = cadena.replace(letra,'u')

    return cadena

def enmascarar(palabra_secreta, letras_usadas=""):
    cadena_devuelto = ""     
    n = 0
    for letra in palabra_secreta :
        if letra in letras_usadas:
            cadena_devuelto+=letra
        else:
            cadena_devuelto+="_" 
        n+=1

    return cadena_devuelto

def ha_ganado(palabra_enmascarada):

    for letra in palabra_enmascarada:
        if letra == "_":
            return False
    return True
    
def mostrar_estado(palabra_enmascarada,letras_usadas,numero_intentos):
    print(">>ESTADO DEL JUGADOR<<")
    show_palabra_enmascarada = " ".join(palabra_enmascarada)
    print(">>Estado de la palabra : ",show_palabra_enmascarada)
    if len(letras_usadas) == 0 :
        print(">>Letras usados : ninguna")
    else:
        print(">>Letras usados : ",letras_usadas)
    print(">>Numero de intentos : ",numero_intentos)

def pedir_letra(letras_usadas):
    letra_res = ""
    while letra_res == "":
        letra = input(">>Entre una letra :")
        if len(letra) != 1 : 
            print(">>Debes introducir una única letra")
            continue
        elif letra in letras_usadas:
            print(">>Esa letra ya la has usado anteriormente")
            continue
        elif letra in "1234567890/-=+%^&*!?":
            print(">>Debes introducir una letra")
            continue
        else : 
            letra_res = letra
    return letra_res

def jugar(palabra_secreta,max_intentos=6) : 
    if palabra_secreta == "":
        print(">>no hay una palabra secreta!")
        return

    letras_usadas = ""
    palabra_secreta = normalizar(palabra_secreta)
    palabra_enmascarado = enmascarar(palabra_secreta,letras_usadas)
    intentos = max_intentos


    while intentos<=max_intentos :
        mostrar_estado(palabra_enmascarado,letras_usadas,intentos)
        letras_usadas+=pedir_letra(letras_usadas)
        palabra_enmascarado = enmascarar(palabra_secreta,letras_usadas)
        if ha_ganado(palabra_enmascarado) :
            print(">>El jugador ha ganado!")
            print(">>La palabra era : ",palabra_secreta)
            break
        else :
            print(">>El jugador todavia no ha ganado!")
            intentos+=1

jugar(elige_palabra("palabras.txt"))
