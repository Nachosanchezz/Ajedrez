def partida_ajedrez(numero_fichero):
    """Funcion que recibe un numero de fichero y devuelve la partida de ajedrez
    correspondiente a ese numero de fichero"""
    # Abrimos el fichero
    fichero = open("partidas.txt", "r")
    # Leemos el fichero
    texto = fichero.read()
    # Cerramos el fichero
    fichero.close()
    # Separamos el texto en partidas
    partidas = texto.split("