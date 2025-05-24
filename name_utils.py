
def obtem_nome_validado(solicitacao: str) -> str:
    nome = input(solicitacao).strip()

    while True:
        if nome.replace(" ", "").isalpha():
            return nome
        else:
            print("Nome inválido. Use apenas letras e espaços\n")