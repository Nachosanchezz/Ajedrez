def tablero(nombre_fichero, n):
    f = open(nombre_fichero, 'w')
    tableros = f.read().split('\n')
    for i in tableros[n*8:(n+1)*8]: 
       print(i)
    return
tablero('partida-ajedrez.txt', 2)
