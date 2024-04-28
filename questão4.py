while True:
    populacaoa = float(input("digite a população A: "))
    crescimento = float(input("digite a taxa de crescimento de A: "))
    populacaob = float(input("digite a população B: "))
    crescimentob = float(input("digite a taxa de crescimento de B: "))
    anos = 0

    while populacaoa > populacaob:
        populacaoa *= 1 + crescimento
        populacaob *= 1 + crescimentob
        anos += 1

    print("vai demorar ", anos, "anos para ingualar ou ultrapassar")

    continuar = str(input("deseja continuar?"))

    if continuar != "S" and continuar != "s":
        break