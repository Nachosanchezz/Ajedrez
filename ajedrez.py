def partida_ajedrez(nombre_fichero):
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero = []
    for i in range(8):
        tablero.append(tablero_inicial.split('\t'))
    print(tablero)
    movimientos = 0
    while True:
        movimiento = input('Quiere hacer otro movimiento: (Si/No)')
        if movimiento != 'Si':
            break
    
        else:
            fila_inicial = int(input('Introduzca la fila inicial: '))
            columna_inicial = int(input('Introduzca la columna inicial: '))
            fila_final = int(input('Introduzca la fila final: '))
            columna_final = int(input('Introduzca la columna final: '))
            tablero[fila_final-1][columna_final-1] = tablero [fila_inicial-1][columna_inicial-1]
            tablero[fila_inicial-1][columna_inicial-1] = '\t'
            movimientos += 1
            f = open(nombre_fichero, 'a')
            f.write('Movimiento ' + str(movimiento) + '\n')

            for i in tablero:
                f.write('\t'.join(i) + '\n')
            f.close()
    return 

partida_ajedrez('partida-ajedrez.txt')



           
        