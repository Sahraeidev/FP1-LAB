from collections import namedtuple

EstacionSevici = namedtuple("EstacionSevici", 
    "nombre, direccion, latitud, longitud, capacidad, puestos_libres, bicicletas_disponibles")

def selecciona_color(estacion:EstacionSevici) -> str:

    if estacion.capacidad == 0 :
        return "gray"

    disponibilidad = estacion.bicicletas_disponibles / estacion.capacidad

    if disponibilidad >= (2/3):
        return "green"
    elif disponibilidad >= (1/3) and disponibilidad < (2/3):
        return "orange"
    elif disponibilidad < (1/3):
        return "red"
def calcula_estadisticas(estaciones: list[EstacionSevici]) -> tuple[int, int, float, int]:

    bicicletas_libres_total = 0
    capacidad_total = 0
    porcentaje_de_ocupacion = 0.0
    total_de_estaciones= len(estaciones)
    for i in  range(total_de_estaciones):
        bicicletas_libres_total+=estaciones[i].bicicletas_disponibles
        capacidad_total+=estaciones[i].capacidad

    porcentaje_de_ocupacion = (1 - (bicicletas_libres_total/capacidad_total))* 100
    return (bicicletas_libres_total, capacidad_total, porcentaje_de_ocupacion, total_de_estaciones)
def busca_estaciones_direccion(estaciones: list[EstacionSevici], direccion_parcial: str) -> list[EstacionSevici]:
    
    estaciones_cercas = []
    direccion_parcial = direccion_parcial.lower()
    for i in range(len(estaciones)):
        direccion1 = estaciones[i].direccion
        direccion1 = direccion1.lower()
        if  direccion_parcial in direccion1:
            estaciones_cercas.append(estaciones[i])

    return estaciones_cercas
def busca_estaciones_con_disponibilidad(estaciones:list[EstacionSevici], min_disponibilidad: float = 0.5) -> list[EstacionSevici]:
   
    estaciones_aprovados = []

    for i in range(len(estaciones)):
        if estaciones[i].capacidad == 0:
            continue
        procentaje_de_disponibilidad = estaciones[i].bicicletas_disponibles / estaciones[i].capacidad
        if procentaje_de_disponibilidad > min_disponibilidad :
            estaciones_aprovados.append(estaciones[i]) 
    return estaciones_aprovados



def calcula_distancia(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    distancia = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(0.5)
    return distancia

def busca_estacion_mas_cercana(estaciones:list[EstacionSevici], punto:tuple[float, float]) -> EstacionSevici | None:
    distancia_min = 10000
    estacian_mas_cerca = estaciones[0]
    for i in range(len(estaciones)):
        dist = calcula_distancia((estaciones[i].latitud,estaciones[i].longitud),punto)
        if distancia_min > dist and estaciones[i].bicicletas_disponibles >= 1:
            distancia_min = dist
            estacian_mas_cerca = estaciones[i]
    return estacian_mas_cerca


def calcula_ruta(estaciones:list[EstacionSevici], origen:tuple[float, float], destino:tuple[float, float]) -> tuple[EstacionSevici | None, EstacionSevici | None]   :
    estacion_cerca_de_origen = busca_estacion_mas_cercana(estaciones,origen)
    estacion_cerca_de_destino = busca_estacion_mas_cercana(estaciones,destino)
    return (estacion_cerca_de_origen,estacion_cerca_de_destino)

