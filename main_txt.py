arquivo = "dadostrabalho.csv"
arquivo_open = open(arquivo, 'r')
cabecalho = arquivo_open.readline()
frotas = arquivo_open.readlines()

# [2, 3, 4, 6, 8, 11, 12, 15, 16, 27, 99]
horas = {"00": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "01": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "02": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "03": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "04": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "05": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "06": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "07": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "08": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "09": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "10": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "11": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "12": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "13": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "14": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "15": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "16": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "17": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "18": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "19": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "20": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "21": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         "22": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "23": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}

for frota_line in frotas:
    aux = frota_line.split(';')

    if aux[4] == "2":
        lista_de_cartoes_da_hora = horas[aux[3][11:13]]
        lista_de_cartoes_da_hora[0] = lista_de_cartoes_da_hora[0] + 1
    elif aux[4] == "3":
        lista_de_cartoes_da_hora = horas[aux[3][11:13]]
        lista_de_cartoes_da_hora[1] = lista_de_cartoes_da_hora[1] + 1
    elif aux[4] == "4":
        lista_de_cartoes_da_hora = horas[aux[3][11:13]]
        lista_de_cartoes_da_hora[2] = lista_de_cartoes_da_hora[2] + 1
    elif aux[4] == "6":
        lista_de_cartoes_da_hora = horas[aux[3][11:13]]
        lista_de_cartoes_da_hora[3] = lista_de_cartoes_da_hora[3] + 1
    elif aux[4] == "8":
        lista_de_cartoes_da_hora = horas[aux[3][11:13]]
        lista_de_cartoes_da_hora[4] = lista_de_cartoes_da_hora[4] + 1
    elif aux[4] == "11":
        lista_de_cartoes_da_hora = horas[aux[3][11:13]]
        lista_de_cartoes_da_hora[5] = lista_de_cartoes_da_hora[5] + 1
    elif aux[4] == "12":
        lista_de_cartoes_da_hora = horas[aux[3][11:13]]
        lista_de_cartoes_da_hora[6] = lista_de_cartoes_da_hora[6] + 1
    elif aux[4] == "15":
        lista_de_cartoes_da_hora = horas[aux[3][11:13]]
        lista_de_cartoes_da_hora[7] = lista_de_cartoes_da_hora[7] + 1
    elif aux[4] == "16":
        lista_de_cartoes_da_hora = horas[aux[3][11:13]]
        lista_de_cartoes_da_hora[8] = lista_de_cartoes_da_hora[8] + 1
    elif aux[4] == "27":
        lista_de_cartoes_da_hora = horas[aux[3][11:13]]
        lista_de_cartoes_da_hora[9] = lista_de_cartoes_da_hora[9] + 1
    else:
        lista_de_cartoes_da_hora = horas[aux[3][11:13]]
        lista_de_cartoes_da_hora[10] = lista_de_cartoes_da_hora[10] + 1

text_file = open("dados_trabalho.txt", "w")
text_file.write(
    "Hora   Cartao 2   Cartao 3   Cartao 4   Cartao 6   Cartao 8   Cartao 12   Cartao 15   Cartao 16   Cartao 27   Cartao 99 \n")

ordem_de_cartoes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for hora in sorted(horas):
    cartoes = horas[hora]
    text_file.write(' ' + str(hora) + '     ' + str(cartoes[0]) + '     ' + str(cartoes[1]) + '     ' + str(cartoes[2]) +
                    '     ' + str(cartoes[3]) + '     ' + str(cartoes[4]) + '     ' + str(cartoes[5]) + '     ' +
                    str(cartoes[6]) + '     ' + str(cartoes[7]) + '     ' + str(cartoes[8]) + '     ' + str(cartoes[9]) +
                    '     ' + str(cartoes[10]) + ' \n')
    ordem_de_cartoes = [
        ordem_de_cartoes[0] + cartoes[0], ordem_de_cartoes[1] + cartoes[1], ordem_de_cartoes[2] + cartoes[2],
        ordem_de_cartoes[3] + cartoes[3], ordem_de_cartoes[4] + cartoes[4], ordem_de_cartoes[5] + cartoes[5],
        ordem_de_cartoes[6] + cartoes[6], ordem_de_cartoes[7] + cartoes[7], ordem_de_cartoes[8] + cartoes[8],
        ordem_de_cartoes[9] + cartoes[9], ordem_de_cartoes[10] + cartoes[10]
    ]

text_file.write('TOTAL   ' + str(ordem_de_cartoes[0]) + '   ' + str(ordem_de_cartoes[1]) + '   ' +
                str(ordem_de_cartoes[2]) + '   ' + str(ordem_de_cartoes[3]) + '   ' + str(ordem_de_cartoes[4])
                + '   ' + str(ordem_de_cartoes[5]) + '   ' + str(ordem_de_cartoes[6]) + '   ' + str(ordem_de_cartoes[7])
                + '   ' + str(ordem_de_cartoes[8]) + '   ' + str(ordem_de_cartoes[9]) + '   ' + str(ordem_de_cartoes[10]))

text_file.close()
arquivo_open.close()
