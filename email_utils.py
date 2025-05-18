
def validar_email(email: str) -> bool:
    if ' ' in email:
        return False

    if email.count('@') != 1:
        return False

    usuario, dominio = email.split('@')

    if not usuario or not dominio:
        return False

    if '.' not in dominio:
        return False

    if dominio.startswith('.') or dominio.endswith('.'):
        return False

    return True

def pedir_email(solicitacao: str) -> str:
    while True:
        try:
            email = input(solicitacao).strip()
        except ValueError:
            print('Erro: Digite caracteres válidos para o email\n')
            continue
        
        if validar_email(email):
            return email
        else:
            print("Email inválido. Tente novamente\n")
