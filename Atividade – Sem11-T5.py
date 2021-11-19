n = 0
while n < 999:
    entrada = float(input(""))
    n = n + 1
    if entrada < 0 or entrada > 10:
        print("Nota inválida.")
    elif entrada >= 8.5:
        print("A")
        break
    elif entrada >= 7.0:
        print("B")
        break
    elif entrada >= 5.0:
        print("C")
        break
    elif entrada >= 4.0:
        print("D")
        break
    elif entrada >= 0.0:
        print("E")
        break
    
    
