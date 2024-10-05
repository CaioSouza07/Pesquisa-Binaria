V = []

for i in range(10):
    V.append(i)

busca = int(input("Buscar: "))

inicio = 0
final = len(V) - 1
achou = False

#print(final)
while inicio <= final and not achou:
    meio = (final + inicio) //2
    if V[meio] == busca:
        achou = True
    elif V[meio] > busca:
        final = meio - 1
    else:
        inicio = meio + 1

print(meio)