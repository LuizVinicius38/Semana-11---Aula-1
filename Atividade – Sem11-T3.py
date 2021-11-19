n = 0
while n < 999:
    print("""OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM""")
    entrada = int(input(""))
    n = n + 1
    if entrada == 1:
        print("1 - Olá. Como vai?")
    if entrada == 2:
        print("2 - Vamos estudar mais.")
    if entrada == 3:
        print("3 - Meus Parabéns!")
    if entrada < 0:
        print("Opção inválida.")
    if entrada > 3:
        print("Opção inválida.")
    if entrada == 0:
        print("0 - Fim de serviço.")
        break
