distancia = int(input("Intrudoce la distancia total : "))
numerodeparadas = 0
for parada in range(0,distancia,150000):
  if parada == 0 :
    continue
  print(f"Parada en el km {parada}")
  numerodeparadas+=1

print(f"numero de paradas : {numerodeparadas}")