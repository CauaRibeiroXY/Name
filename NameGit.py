import datetime
import subprocess
 

def criar_matriz(letras_para_imprimir):
    # Definindo as dimensões da matriz
    linhas = 7
    colunas = 51

    # Inicializando a matriz com espaços em branco
    matriz = [[' ' for _ in range(colunas)] for _ in range(linhas)]

    # Mapeando as letras
    letras = {
    'A': [
        "  ##   ",
        " #  #  ",
        "#    # ",
        "###### ",
        "#    # ",
        "#    # ",
        "#    # "
    ],
    'B': [
        "#####  ",
        "#    # ",
        "#    # ",
        "#####  ",
        "#    # ",
        "#    # ",
        "#####  "
    ],
    'C': [
        " ##### ",
        "#      ",
        "#      ",
        "#      ",
        "#      ",
        "#      ",
        " ##### "
    ],
    'D': [
        "#####  ",
        "#    # ",
        "#    # ",
        "#    # ",
        "#    # ",
        "#    # ",
        "#####  "
    ],
    'E': [
        "###### ",
        "#      ",
        "#      ",
        "#####  ",
        "#      ",
        "#      ",
        "###### "
    ],
    'F': [
        "###### ",
        "#      ",
        "#      ",
        "#####  ",
        "#      ",
        "#      ",
        "#      "
    ],
    'G': [
        " ##### ",
        "#      ",
        "#      ",
        "#  ### ",
        "#    # ",
        "#    # ",
        " ##### "
    ],
    'H': [
        "#    # ",
        "#    # ",
        "#    # ",
        "###### ",
        "#    # ",
        "#    # ",
        "#    # "
    ],
    'I': [
        "##### ",
        "  #   ",
        "  #   ",
        "  #   ",
        "  #   ",
        "  #   ",
        "##### "
    ],
    'J': [
        "  ##### ",
        "     #  ",
        "     #  ",
        "     #  ",
        "#    #  ",
        "#    #  ",
        " ####   "
    ],
    'K': [
        "#   #  ",
        "#  #   ",
        "##     ",
        "##     ",
        "# #    ",
        "#  #   ",
        "#   #  ",
    ],
    'L': [
        "#      ",
        "#      ",
        "#      ",
        "#      ",
        "#      ",
        "#      ",
        "###### "
    ],
    'M': [
        "#    # ",
        "#    # ",
        "##  ## ",
        "# ## # ",
        "#    # ",
        "#    # ",
        "#    # "
    ],
    'N': [
        "#    # ",
        "##   # ",
        "# #  # ",
        "#  # # ",
        "#   ## ",
        "#    # ",
        "#    # "
    ],
    'O': [
        " ##### ",
        "#     #",
        "#     #",
        "#     #",
        "#     #",
        "#     #",
        " ##### "
    ],
    'P': [
        "#####  ",
        "#    # ",
        "#    # ",
        "#####  ",
        "#      ",
        "#      ",
        "#      "
    ],
    'Q': [
        " ##### ",
        "#     #",
        "#     #",
        "#     #",
        "#   # #",
        " ##### ",
        "     # "
    ],
    'R': [
        "#####  ",
        "#    # ",
        "#    # ",
        "#####  ",
        "#   #  ",
        "#    # ",
        "#    # "
    ],
    'S': [
        " ##### ",
        "#      ",
        "#      ",
        " ####  ",
        "     # ",
        "     # ",
        "#####  "
    ],
    'T': [
        "###### ",
        "  #    ",
        "  #    ",
        "  #    ",
        "  #    ",
        "  #    ",
        "  #    "
    ],
    'U': [
        "#    # ",
        "#    # ",
        "#    # ",
        "#    # ",
        "#    # ",
        "#    # ",
        " ####  "
    ],
    'V': [
        "#    # ",
        "#    # ",
        "#    # ",
        "#    # ",
        "#    # ",
        " #  #  ",
        "  ##   "
    ],
    'W': [
        "#    # ",
        "#    # ",
        "#    # ",
        "# ## # ",
        "##  ## ",
        "#    # ",
        "#    # "
    ],
    'X': [
        "#    # ",
        " #  #  ",
        "  ##   ",
        "  ##   ",
        " #  #  ",
        "#    # ",
        "#    # "
    ],
    'Y': [
        "#    # ",
        "#    # ",
        " #  #  ",
        "  ##   ",
        "  ##   ",
        "  ##   ",
        "  ##   "
    ],
    'Z': [
        " ##### ",
        "     # ",
        "    #  ",
        "   #   ",
        "  #    ",
        " #     ",
        " ##### "
    ],
    ' ': [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " "
    ],
    '!': [
        " # ",
        " # ",
        " # ",
        "   ",
        " # ",
        "   "
    ],
    '"': [
        "# # ",
        "# # ",
        "    ",
        "    ",
        "    ",
        "    "
    ],
    '#': [
        "# # # ",
        "##### ",
        "# # # ",
        "##### ",
        "# # # ",
        "##### "
    ],
    '$': [
        " ###  ",
        "#   # ",
        "####  ",
        "  #   ",
        "####  ",
        "#   # ",
        " ###  "
    ],
    '%': [
        "#   # ",
        "   #  ",
        "  #   ",
        " #    ",
        "#     ",
        " #    ",
        "   # #"
    ],
    '&': [
        " ##   ",
        "#  #  ",
        " ##   ",
        "# # # ",
        "##  # ",
        "#   # ",
        " ## # "
    ],
    '\'': [
        " # ",
        " # ",
        "   ",
        "   ",
        "   ",
        "   "
    ],
    '(': [
        "  # ",
        " #  ",
        "#   ",
        "#   ",
        " #  ",
        "  # "
    ],
    ')': [
        "#   ",
        " #  ",
        "  # ",
        "  # ",
        " #  ",
        "#   "
    ],
    '*': [
        "     ",
        " # # ",
        "  #  ",
        "#####",
        "  #  ",
        " # # ",
        "     "
    ],
    '+': [
        "     ",
        "  #  ",
        "  #  ",
        "#####",
        "  #  ",
        "  #  ",
        "     "
    ],
    ',': [
        "   ",
        "   ",
        "   ",
        "   ",
        " # ",
        "#  ",
        "   "
    ],
    '-': [
        "     ",
        "     ",
        "     ",
        "#####",
        "     ",
        "     ",
        "     "
    ],
    '.': [
        "   ",
        "   ",
        "   ",
        "   ",
        "   ",
        "#  ",
        "   "
    ],
    '/': [
        "     #",
        "    # ",
        "   #  ",
        "  #   ",
        " #    ",
        "#     ",
        "      "
    ],'0': [
        " ##### ",
        "#     #",
        "#  #  #",
        "# # # #",
        "#  #  #",
        "#     #",
        " ##### "
    ],
    '1': [
        "  ##  ",
        " # #  ",
        "   #  ",
        "   #  ",
        "   #  ",
        "   #  ",
        " #####"
    ],
    '2': [
        " ##### ",
        "#     #",
        "      #",
        " ##### ",
        "#      ",
        "#      ",
        "#######"
    ],
    '3': [
        " ##### ",
        "#     #",
        "      #",
        " ##### ",
        "      #",
        "#     #",
        " ##### "
    ],
    '4': [
        "#      ",
        "#    # ",
        "#    # ",
        "#######",
        "     # ",
        "     # ",
        "     # "
    ],
    '5': [
        "#######",
        "#      ",
        "#      ",
        " ######",
        "      #",
        "#     #",
        " ##### "
    ],
    '6': [
        " ##### ",
        "#     #",
        "#      ",
        " ####  ",
        "#    # ",
        "#    # ",
        " ####  "
    ],
    '7': [
        "#######",
        "#    # ",
        "    #  ",
        "   #   ",
        "  #    ",
        "  #    ",
        "  #    "
    ],
    '8': [
        " ##### ",
        "#     #",
        "#     #",
        " ##### ",
        "#     #",
        "#     #",
        " ##### "
    ],
    '9': [
        " ####  ",
        "#    # ",
        "#    # ",
        " ##### ",
        "     # ",
        "    #  ",
        " ###   "
    ]
}
     # Posicionando as letras 'C', 'A', 'U', 'A', 'X', 'Y' na matriz
    
    coluna_atual = 0
    for letra in letras_para_imprimir:
        representacao = letras[letra]
        for i in range(min(linhas, len(representacao))):
            for j in range(min(colunas - coluna_atual, len(representacao[i]))):
                matriz[i][coluna_atual + j] = representacao[i][j]
        coluna_atual += len(representacao[0]) + 2  # +2 para dar um espaço entre as letras

    return matriz

def gerar_matriz_datas(ano):
    """Gera uma matriz 7x51 preenchida com datas começando em 6/01."""
    linhas = 7
    colunas = 51

    # Inicializar matriz com espaços em branco
    matriz = [[' ' for _ in range(colunas)] for _ in range(linhas)]

    # Definir a data inicial como 6/01/2019
    data_atual = encontrar_primeiro_domingo(ano)

    # Preencher a matriz com datas, onde cada coluna representa uma semana
    for j in range(colunas):
        for i in range(linhas):
            # Formatar a data para dia/mês
            matriz[i][j] = data_atual.strftime('%d/%m/%y')
            # Avançar para o próximo dia (semana)
            data_atual += datetime.timedelta(days=1)

    # Determinar o último dia representado na matriz
    ultimo_dia = (data_atual - datetime.timedelta(days=1)).strftime('%d/%m/%y')

    return matriz, ultimo_dia

def imprimir_nome(matriz):
    """Imprime a matriz."""
    for linha in matriz:
        print(" ".join(linha))

def encontrar_primeiro_domingo(ano):
    """Encontra o primeiro domingo de um determinado ano."""
    data = datetime.date(ano, 1, 1)  # Começando em 1º de janeiro do ano fornecido
    while data.weekday() != 6:  # 6 representa domingo
        data += datetime.timedelta(days=1)  # Avançar um dia até encontrar um domingo
    print(data)
    return data

def mapear_datas_pelo_simbolo(matriz_letras, matriz_datas):
    """Mapeia as datas com base nas posições onde o símbolo '#' está presente na matriz de letras."""
    linhas = len(matriz_letras)
    colunas = len(matriz_letras[0])

    # Dicionário para armazenar o mapeamento de datas
    datas_mapeadas = {}

    for j in range(colunas):
        for i in range(linhas):
            if matriz_letras[i][j] == '#':
                datas_mapeadas[(i, j)] = matriz_datas[i][j]

    return datas_mapeadas
 
def fazer_commit_nos_dias(datas_mapeadas):
    """Faz um 'commit' apenas nos dias presentes na estrutura de mapeamento de datas."""
    for posicao, data in datas_mapeadas.items():
        # Formatar a data para o nome do arquivo e a mensagem do commit
        commit_date = datetime.datetime.strptime(data, '%d/%m/%y').strftime("%Y-%m-%d")
        
        # Criar um arquivo com a data como nome
        with open(commit_date, 'w') as f:
            f.write("Commit para a data: " + commit_date)
        
        # Fazer o commit usando o Git
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Commit para a data: " + commit_date, "--date", commit_date])


def main():
    letras_para_imprimir = input("Digite as letras que você deseja imprimir (sem espaços, ex: CAUAXY): ").upper()
    matriz = criar_matriz(letras_para_imprimir)
    imprimir_nome(matriz)

    ano = int(input("\nDigite o ano desejado a partir de 2015: "))
    matriz_datas, ultimo_dia = gerar_matriz_datas(ano)
    #print(f"\nÚltimo dia representado na matriz: {ultimo_dia}")

    datas_mapeadas = mapear_datas_pelo_simbolo(matriz, matriz_datas)
    #print("\nMapeamento de datas para as posições com '#':")
    #for posicao, data in datas_mapeadas.items():
    #    print(f"Posição {posicao}: {data}")

    resposta = input("\nDeseja fazer os commits da imagem? (s/n): ")
    if resposta.lower() == 's':
        fazer_commit_nos_dias(datas_mapeadas)
        print("\nOs commits foram feitos. Lembre-se de fazer o push para atualizar o repositório remoto.")
    else:
        print("\nNenhum commit foi realizado.")



if __name__ == "__main__":
    main()
