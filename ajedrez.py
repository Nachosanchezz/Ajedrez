def partida_ajedrez(nombre_fichero):
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero = []                      # Representación del tablero
    for i in tablero_inicial.split('\n'):                          # Separamos las filas
        tablero.append(tablero_inicial.split('\t'))              
    print(tablero)
    movimientos = 0
    while True:                                      # Bucle infinito

        movimiento = input('Quiere hacer otro movimiento: (Si/No)')       # Preguntamos si quiere hacer otro movimiento
        if movimiento != 'Si':                                       # Si no quiere hacer otro movimiento, salimos del bucle
            break                                               # Salimos del bucle
      
        else:                           # Si quiere hacer otro movimiento, preguntamos por las coordenadas
            fila_inicial = int(input('Introduzca la fila inicial: '))           # Preguntamos por la fila inicial
            columna_inicial = int(input('Introduzca la columna inicial: '))          # Preguntamos por la columna inicial
            fila_final = int(input('Introduzca la fila final: '))                       # Preguntamos por la fila final
            columna_final = int(input('Introduzca la columna final: '))                # Preguntamos por la columna final
            tablero[fila_final-1][columna_final-1] = tablero [fila_inicial-1][columna_inicial-1]       # Movemos la pieza
            tablero[fila_inicial-1][columna_inicial-1] = '\t'               # Borramos la pieza de la posición inicial 
            movimientos += 1               # Aumentamos el número de movimientos
            f = open(nombre_fichero, 'a')
            f.write('Movimiento ' + str(movimiento) + '\n')      # Escribimos el número de movimiento
  
            for i in tablero:                      # Escribimos el tablero
                f.write('\t'.join(i) + '\n')          
            f.close()               # Cerramos el fichero
    return  movimientos

partida_ajedrez('partida-ajedrez.txt')



           
        