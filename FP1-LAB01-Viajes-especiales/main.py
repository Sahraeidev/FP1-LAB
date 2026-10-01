print(2 + 3 * 4 ** 2 // 5 - 1)   # prediction: 4
print(20 // 6 * 6 + 20 % 6)      # prediction: 20
print(-15 // 4, -15 % 4)         # prediction: -4 2
print(9 / 3, 9 // 3)             # prediction: 3.0 3
print("5" * 3, 5 * 3)            # prediction: 555 15

days = 100
weeks = days//7
days = days % 7
print(weeks , " weeks and " , days , " days")


segundos = 7384
minutos = 7384 // 60
segundos = segundos % 60
horas = minutos // 60
minutos = minutos % 60

print(horas , " horas ", minutos , " minutos " , segundos, "segundos")

print( (2 ** 100) % 10 , (2 ** 100) % 100)

print((1234 % 3) == 0)
print((2026 % 2) == 0)

C = 36.6

F = 36.6 * (9 / 5) + 32

print(round(F,2))

print("Resultado:", 7 * 3)
print("Total: " , 15)
print("Hola mundo")
print((2 + 3) * 4)

print(-2 ** 2 + 2 ** -1)
# based on the priroties it first runs 2 ** 2 and with - it becomes -4 after that it runs 2 ** -1 which is 1/2 and sums them