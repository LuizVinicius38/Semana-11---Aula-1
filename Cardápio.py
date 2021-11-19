print("(H) Para Hamburger Preço - R$5.50!")
print("(C) Para Cheeseburger Preço - R$6.80!")
print("(M) Para Misto Quente Preço - R$4.50!")
print("(A) Para Americano Preço - R$7.00!")
print("(Q) Para Queijo Prato Preço - R$4.00!")
print("(X) Para Total da conta!")

contH = 0
contC = 0
contM = 0
contA = 0
contQ = 0
totalH = 0.0
totalC = 0.0
totalM = 0.0
totalA = 0.0
totalQ = 0.0

while True:
    H = 5.50
    C = 6.80
    M = 4.50
    A = 7.00
    Q = 4.00
    entrada = str(input("Digite uma das opções! ")).upper()
    if entrada == "H":
        contH = contH + 1
        totalH = contH * 5.50 
    elif entrada == "C":
        contC = contC + 1
        totalC = contC * 6.80 
    elif entrada == "M":
        contM = contM + 1
        totalM = contM * 4.50 
    elif entrada == "A":
        contA = contA + 1
        totalA = contA * 7.00 
    elif entrada == "Q":
        contQ = contQ + 1
        totalQ = contQ * 4.00 
    elif entrada == "X":
        total = totalH + totalC + totalM + totalA + totalQ
        print("Total: R${}".format(total))
        break