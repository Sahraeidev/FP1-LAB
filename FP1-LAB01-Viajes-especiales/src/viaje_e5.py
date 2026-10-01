
Sicontinua = True

while Sicontinua :
  distancia_km = int(input("Entra la distancia : "))  # distancia Tierra - Luna
  velocidad_kmh = int(input("Entra la velocidad : "))
  tiempo_horas = distancia_km // velocidad_kmh
  tiempo_dias = tiempo_horas // 24
  tiempo_semana = tiempo_dias // 7
  tiempo_dias%=7
  print(f"Tardarías {tiempo_semana} semanas y {tiempo_dias} días en llegar.")
  Sicontinua = bool(input("Quieres hacer otro calculo ? [1 : SÍ , 0 : NO]"))

