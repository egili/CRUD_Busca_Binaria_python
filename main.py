from date_utils    import pedir_data
from name_utils    import obtem_nome_validado
from email_utils   import pedir_email
from address_utils import pedir_endereco
from phone_utils   import pedir_telefone, pedir_celular

def apresenteSe():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Brenda Maia Bergamasco   - 25010054                         |')
    print('| Eliseu Pereira Gili      - 25009281                         |')
    print('| Pietra Façanha Bortolato - 25002436                         |')
    print('|                                                             |')
    print('| Versão 2.0 de 24/maio/2025                                  |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto(solicitacao, mensagem, valido):
    
    digitou_direito = False
    
    while not digitou_direito:
        txt = input(solicitacao)

        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitou_direito = True

    return txt

def opcaoEscolhida(mnu):
    print()

    opcoesValidas = []
    posicao = 0
    while posicao < len(mnu):
        print (posicao + 1,') ',mnu[posicao], sep='')
        opcoesValidas.append(str(posicao + 1))
        posicao += 1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

def ondeEsta(nom, agd):
    
    inicio = 0
    final = len(agd) - 1
    nom_lower = nom.lower()

    while inicio <= final:
        
        meio = (inicio + final) // 2
        nome_meio = agd[meio][0].lower()
        
        if nom_lower == nome_meio:
            return [True, meio]
        elif nom_lower < nome_meio:
            final = meio - 1
        else:
            inicio = meio + 1

    return [False, inicio]

def cadastrar(agd):
    while True:
        nome = obtem_nome_validado("Digite o nome (ou 'cancela' para sair): ")

        if nome.lower() == 'cancela':
            print("Cadastro não realizado.")
            return

        achou, pos = ondeEsta(nome, agd)

        if achou:
            print("Este nome já está cadastrado. Tente novamente")
        else:
            break

    aniversario = pedir_data("Digite o aniversário: ")
    endereco    = pedir_endereco("Digite o endereço: ")
    telefone    = pedir_telefone("Digite o telefone fixo: ")
    celular     = pedir_celular("Digite o celular: ")
    email       = pedir_email("Digite o e-mail: ")

    contato = [ nome, aniversario, endereco, telefone, celular, email ]
    
    agd.insert(pos, contato)
    print("Contato cadastrado com sucesso!")

def procurar(agd):
    
    if agd == [] or len(agd) == 0:
        print('Não há contatos cadastrados!')
        return
    
    while True:
        nome = obtem_nome_validado("Digite o nome a ser procurado, ou 'cancelar' para desistir: ")
        
        if nome.lower() == 'cancelar':
            print("Busca cancelada pelo usuário.")
            return

        achou, pos = ondeEsta(nome, agd)

        if achou:
            contato = agd[pos]
            print('Nome: ', contato[0])
            print('Aniversário: ', contato[1])
            print('Endereço: ', contato[2])
            print('Telefone: ', contato[3])
            print('Celular: ', contato[4])
            print('E-mail: ', contato[5])
            print()
            return

        else:
            print("Nome não encontrado. Tente novamente ou digite 'cancelar' para sair.")

def atualizar(agd):
    while True:
        nome = obtem_nome_validado('Digite o nome para atualizar (ou "cancela" para sair): ')
        if nome.lower() == 'cancela':
            print('Atualização cancelada pelo usuário.')
            return
        achou, pos = ondeEsta(nome, agd)
        if not achou:
            print('Nome não encontrado. Tente novamente.')
            continue
        contato = agd[pos]
        submenu = [
            'Atualizar Aniversário',
            'Atualizar Endereço',
            'Atualizar Telefone',
            'Atualizar Celular',
            'Atualizar Email',
            'Finalizar Atualizações'
        ]
        while True:
            opc = int(opcaoEscolhida(submenu))
            if opc == len(submenu):
                print('Atualizações finalizadas.')
                return

            if opc == 1:
                nova_data = pedir_data('nova data ou cancela para sair: ')
                if nova_data.lower() == 'cancela':
                    print('Atualização cancelada pelo usuário.')
                    return
                contato[1] = nova_data
                print('Aniversário atualizado com sucesso!')
            elif opc == 2:
                novo_endereco = pedir_endereco('novo endereco ou cancela para sair: ')
                if novo_endereco.lower() == 'cancela':
                    print('Atualização cancelada pelo usuário.')
                    return
                contato[2] = novo_endereco
                print('Endereço atualizado com sucesso!')
            elif opc == 3:
                novo_telefone = pedir_telefone('novo telefone ou cancela para sair: ')
                if novo_telefone.lower() == 'cancela':
                    print('Atualização cancelada pelo usuário.')
                    return
                contato[3] = novo_telefone
                print('Telefone atualizado com sucesso!')
            elif opc == 4:
                novo_celular = pedir_celular('novo celular ou cancela para sair: ')
                if novo_celular.lower() == 'cancela':
                    print('Atualização cancelada pelo usuário.')
                    return
                contato[4] = novo_celular
                print('Celular atualizado com sucesso!')
            else:
                novo_email = pedir_email('novo email ou cancela para sair: ')
                if novo_email.lower() == 'cancela':
                    print('Atualização cancelada pelo usuário.')
                    return
                contato[5] = novo_email
                print('Email atualizado com sucesso!')   

def listar(agd):
    if agd == [] or len(agd) == 0:
        print('Não há contatos cadastrados!')
        return 
    
    for contato in agd:
        print('Nome: ' , contato[0])
        print('Aniversário: ' , contato[1])
        print('Endereço: ' , contato[2])
        print('Telefone: ' , contato[3])
        print('Celular: ' , contato[4])
        print('E-mail: ' , contato[5])
        print()

def excluir(agd):
    
    if agd == [] or len(agd) == 0:
        print('Não há contatos cadastrados!')
        return

    while True:
        
        nome = obtem_nome_validado("Digite o nome a ser excluído, ou 'cancelar' para desistir: ")
        
        if nome.lower() == 'cancelar':
            print("Exclusão cancelada.")
            break

        achou, pos = ondeEsta(nome, agd)

        if achou:
            contato = agd[pos]
            print('Nome: ',   contato[0])
            print('Aniversário: ', contato[1])
            print('Endereço: ', contato[2])
            print('Telefone: ', contato[3])
            print('Celular: ', contato[4])
            print('E-mail: ', contato[5])
            print()
        
            confirmacao = input("Deseja realmente excluir este contato? (sim/não): ").lower()
            
            if confirmacao == 'sim':
                del agd[pos]
                print("Contato excluído com sucesso.")
            else:
                print("Contato não excluído.")
            return
        
        else:
            print("Nome não encontrado. Tente novamente ou digite 'cancelar' para sair.")

apresenteSe()

agenda = []

menu = [
    'Cadastrar Contato',\
    'Procurar Contato',\
    'Atualizar Contato',\
    'Listar Contatos',\
    'Excluir Contato',\
    'Sair do Programa'
]

deseja_terminar_o_programa = False
while not deseja_terminar_o_programa:
    opcao = int(opcaoEscolhida(menu))

    if opcao == 1:
        cadastrar(agenda)
    elif opcao == 2:
        procurar(agenda)
    elif opcao == 3:
        atualizar(agenda)
    elif opcao == 4:
        listar(agenda)
    elif opcao == 5:
        excluir(agenda)
    else: 
        deseja_terminar_o_programa = True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')