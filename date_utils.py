from datetime import datetime

def is_ano_bissexto(ano: int) -> bool:
    if ano < 1583 and ano % 4 == 0:
        return True
    elif ano > 1583 and ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return True
    elif ano % 400 == 0:
        return True
    return False 

def is_data_valida(dia: int, mes: int, ano: int) -> str:
    if dia < 0 or mes < 0:
        return 'Erro: Não existe dia ou mês negativo!'
    elif ano == 0 or ano < -45:
        return 'Erro: Ano inválido!'
    elif 5 <= dia <= 14 and mes == 10 and ano == 1582:
        return 'Erro: Data inválida (transição do calendário Juliano para Gregoriano)!'
    elif mes > 12:
        return 'Erro: Mês inválido'
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 1) and dia > 30:
        return 'Erro: O mês informado tem apenas 30 dias!'
    elif dia > 31:
        return 'Erro: Dia inválido'
    elif is_ano_bissexto(ano) and mes == 2 and dia > 29:
        return 'Erro: Fevereiro em ano bissexto tem no máximo 29 dias!'
    elif not is_ano_bissexto(ano) and mes == 2 and dia > 28:
        return 'Erro: Fevereiro em ano comum tem no máximo 28 dias!'
    
    return 'valido'

def formatar_data(dia: int, mes: int, ano: int) -> str:

    if dia < 10:
        dia = '0' + str(dia)
    
    if mes < 10:
        mes = '0' + str(mes)
    
    return f"{dia}/{mes}/{ano}"

def pedir_dia() -> int:
    
    is_dia_valido = False

    while not is_dia_valido:
        try:
            while not is_dia_valido:
                try:
                    dia = int(input('Dia: '))
                    if 1 <= dia <= 31:
                        is_dia_valido = True
                        return dia
                    else:
                        print('Erro: Valor inválido! O dia deve estar entre 1 e 31. Tente novamente')
                except ValueError:
                    print('Erro: valor inválido! Digite apenas números inteiros')
        except ValueError:
            print('Erro: Digite apenas números para dia, mês e ano')
            continue 

def pedir_mes() -> int:
    
    is_mes_valido = False

    while not is_mes_valido:
        try:
            while not is_mes_valido:
                try:
                    mes = int(input('Mês: '))
                    if 1 <= mes <= 12:
                        is_mes_valido = True
                        return mes
                    else:
                        print('Erro: Valor inválido! O mês deve estar entre 1 e 12. Tente novamente.')
                except ValueError:
                    print('Erro: Entrada inválida! Digite apenas números inteiros.')
        except ValueError:
            print('Erro: Digite apenas números para dia, mês e ano.')
            continue

def pedir_ano() -> int:
    
    is_ano_valido = False
    ano_atual = datetime.now().year

    while not is_ano_valido:
        try:
            while not is_ano_valido:
                try:
                    ano = int(input('Ano: '))
                    if ano > ano_atual:
                        print(f'Erro: Valor inválido! O ano deve ser menor ou igual a {ano_atual}. Tente novamente.')
                    else:
                        is_ano_valido = True
                        return ano
                except ValueError:
                    print('Erro: Entrada inválida! Digite apenas números inteiros.')
        except ValueError:
            print('Erro: Digite apenas números para dia, mês e ano.')
            continue

def pedir_data(solicitacao: str) -> str:

    print(solicitacao)
    
    is_data_validada = False
    
    while not is_data_validada:
    
        dia = pedir_dia()
        mes = pedir_mes()
        ano = pedir_ano()
    
        if is_data_valida(dia, mes, ano) != 'valido':
            print('Tente Novamente\n')
        else:
            is_data_validada = True
    
    return formatar_data(dia, mes, ano)