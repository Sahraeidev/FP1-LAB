from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    if len(cadena) != 5 :
            return False
    
    for i in cadena:
            if i.isalpha() == False :
                return False
     
    return True

def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    segundos_totales = int((fin - inicio).total_seconds())
    minutes = segundos_totales // 60
    second = segundos_totales % 60
    
    return (minutes,second)

def quitar_letra(cadena : str, charecter : str) -> str:
    return cadena.replace(charecter,"",1)

def marcar_verdes(palabra_secreta : str , intento : str)-> tuple:
    verdes = ""
    restantes = ""
    for i in range(0,5):
        if palabra_secreta[i] == intento[i]:
            verdes+="V"
        else:
            restantes+=palabra_secreta[i]
            verdes+="_"

    return (verdes,restantes)

def marcar_amarillos(intento : str,verdes : str,restantes : str) -> str:
    colores = ""
    for i in range(0,5):
        if verdes[i] == "V":
            colores+="V"
        elif verdes[i] == "_":
            if intento[i] in restantes :
                colores+="A"
                restantes.replace(intento[i],"")
            else:
                 colores+="_"

    return colores

def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    verdes = marcar_verdes(palabra_secreta,intento)[0]
    restantes = marcar_verdes(palabra_secreta,intento)[1]
    return marcar_amarillos(intento,verdes,restantes)
