def obtem_nome_validado(solicitacao: str) -> str:
    while True:
        nome = input(solicitacao).strip()
        if not nome:
            continue

        if not nome[0].isupper():
            print("Nome inválido. Primeira letra deve ser maiúscula\n")
        elif not nome.replace(" ", "").isalpha():
            print("Nome inválido. Use apenas letras e espaços\n")
        else:
            return nome
