
def validar_endereco(endereco: str) -> str:
    if not endereco:
        return 'O endereço não pode estar vazio'

    tem_letra = any(c.isalpha() for c in endereco)
    tem_numero = any(c.isdigit() for c in endereco)

    if not tem_letra or not tem_numero:
        return 'O endereço deve conter letras (ex: nome da rua) e números (ex: número da casa)\n'

    if len(endereco) > 200:
        return 'O endereço deve ter no máximo 200 caracteres\n'

    return 'valido'

def pedir_endereco(solicitacao: str) -> str:
    
    is_endereco_valido = False
    
    while not is_endereco_valido:
        try:
            endereco = input(solicitacao).strip()
        except ValueError:
            print('Erro: Digite caracteres válidos para o endereço\n')
            continue

        if validar_endereco(endereco) == 'valido':
            is_endereco_valido = True
            return endereco
        else:
            print(validar_endereco(endereco))