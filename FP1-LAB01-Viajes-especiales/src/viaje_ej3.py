


edad = int(input("Entra tu edad :"))

while edad < 18:
  if edad < 18 : 
      print("Debe ser mayor de edad")
      edad = int(input("Entra tu edad :"))
  

nivelFisico = -1
nivelFisico = int(input("Entra tu nivel fisico :"))

while nivelFisico > 10 or nivelFisico < 5  :
  if nivelFisico < 0 or nivelFisico > 10:
    print("Debe estar entre 0 y 10")
  elif nivelFisico < 5 :
    print("Debe estar en forma")
  nivelFisico = int(input("Entra tu nivel fisico :"))








