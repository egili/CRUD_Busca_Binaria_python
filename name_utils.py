
def obtem_nome_validado(solicitacao: str) -> str:
    nome = input(solicitacao).strip()

    while True:
        if nome.replace(" ", "").isalpha():
            return nome
        elif not nome[0].isupper():
            print("Nome inválido. Primeira letra deve ser maiúscula\n")
        else:
            print("Nome inválido. Use apenas letras e espaços\n")