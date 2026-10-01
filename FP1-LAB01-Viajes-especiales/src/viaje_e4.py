

distancia = 225000000

for velocidad in range(10000,50001,10000):
  tiempo_dias = (distancia / velocidad) / 24
  tiempo_semanas = tiempo_dias // 7
  tiempo_dias%=7
  print(f"Velocidad : {velocidad} Tiempo : {tiempo_semanas} semanas y {tiempo_dias} dias")

