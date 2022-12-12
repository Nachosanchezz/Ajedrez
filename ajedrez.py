def partida_ajedrez(numero_fichero):
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero = []
    for i in range('\n' in tablero_inicial'):
        tablero.append(tablero_inicial.split('\t')[8*i:8*(i+1)])
        f = open(nombre_fichero, 'w')
        f.write(tablero)
        f.close()
        return tablero
    movimientos = 0
    while True:
        print('Turno del jugador blanco')
        print(tablero)
        movimiento = input('Introduzca el movimiento: ')
        if movimiento == '0-0':
            tablero[7][4] = '\t'
            tablero[7][6] = '♔'
            tablero[7][7] = '\t'
            tablero[7][5] = '♖'
        elif movimiento == '0-0-0':
            tablero[7][4] = '\t'
            tablero[7][2] = '♔'
            tablero[7][0] = '\t'
            tablero[7][3] = '♖'
        else:
            tablero[int(movimiento[1])-1][ord(movimiento[0])-97] = '\t'
            tablero[int(movimiento[3])-1][ord(movimiento[2])-97] = '♔'
        movimientos += 1
        print('Turno del jugador negro')
        print(tablero)
        movimiento = input('Introduzca el movimiento: ')
        if movimiento == '0-0':
            tablero[0][4] = '\t'
            tablero[0][6] = '♚'
            tablero[0][7] = '\t'
            tablero[0][5] = '♜'
        elif movimiento == '0-0-0':
            tablero[0][4] = '\t'
            tablero[0][2] = '♚'
            tablero[0][0] = '\t'
            tablero[0][3] = '♜'
        else:
            
