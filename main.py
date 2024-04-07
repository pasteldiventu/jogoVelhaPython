from jogo_da_velha import criarBoard, FazMovimento,getInputValido, printBoard, verificaMovimento, verificarGanhador

jogador = 0 # jogador = 1
board = criarBoard()
ganhador = verificarGanhador(board)


while(not ganhador):
    printBoard(board)
    i = getInputValido("Digite a linha: ")
    j = getInputValido("Digite a coluna: ")
    
    if(verificaMovimento(board, i, j)):
        FazMovimento(board, i, j, jogador)
        jogador = (jogador + 1) %2
    else:
        print("a posição informada ja esta ocupada")

    ganhador = verificarGanhador(board)


printBoard(board)
print("=============")
print("ganhador foi o: ", ganhador)
print("=============")