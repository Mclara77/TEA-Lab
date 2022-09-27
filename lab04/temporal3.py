contador = 0
total = 0
while True:
    input_str = input("ingrese un número: ")
    try:
        if(input_str == "done"):
            break
        else:
            total = total + int(input_str)
            contador = contador + 1
            average = total / contador
    except:
        print("valor no es válido")
        continue
print("total: ", total)
print("contador: ", contador)
print("promedio: ", average)
    