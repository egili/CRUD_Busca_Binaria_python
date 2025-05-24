
def definir_ddd_padrao(tel_cel) -> str:
    return '19' + tel_cel
    
def pedir_telefone(solicitacao: str) -> str:
    while True:
        telefone = input(solicitacao).strip()

        if not telefone.isdigit():
            print("Erro: Digite apenas números")
            continue

        if len(telefone) == 8:
            telefone = definir_ddd_padrao(telefone)
        
        if len(telefone) != 10 and len(telefone) != 8:
            print("Erro: O telefone deve ter 8 (sem DDD) ou 10 (com DDD) dígitos")
            continue

        return telefone

def pedir_celular(solicitacao: str) -> str:
    while True:
        celular = input(solicitacao).strip()

        if not celular.isdigit():
            print("Erro: Digite apenas números\n")
            continue

        if not celular.startswith('9') and len(celular) == 9:
            print("Erro: Números de celular devem começar com 9")
            continue

        if len(celular) == 9:
            celular =  definir_ddd_padrao(celular)

        if len(celular) != 11 and len(celular) != 9:
            print("Erro: Celular deve ter 9 (sem DDD) ou 11 (com DDD) dígitos")
            continue

        return celular
