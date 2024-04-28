populacaoa = 80000
crescimento = 0.03
populacaob = 200000
crescimentob = 1.05
anos = 0

while populacaoa < populacaob:
    populacaoa *= 1 + crescimento
    populacaob *= 1 + crescimentob
    anos += 1

print("vai demorar ", anos, "anos para ingualar ou ultrapassar")
