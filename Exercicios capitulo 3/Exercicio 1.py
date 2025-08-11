listaTimes = ['Team Liquid', 'Loud', 'Barcelona', 'Karmine Corp', 'Vitality']

print("Top 3 ", listaTimes[0:3])
print("Ultimos 2 colocados ", listaTimes[-2:])

listaTimesOrdenada = listaTimes.sort()
print("Times Ordenados alfabeticamente: ", listaTimes)

print("Posicao Barça ", listaTimes.index('Barcelona'))