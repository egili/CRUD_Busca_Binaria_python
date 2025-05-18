from date_utils    import pedir_data
from name_utils    import obtem_nome_validado
from email_utils   import pedir_email
from address_utils import pedir_endereco
from phone_utils   import pedir_telefone, pedir_celular

def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Brenda Maia Bergamasco -                                    |')
    print('| Eliseu Pereira Gili - 25009281                              |')
    print('| Pietra Façanha Bortolato -                                  |')
    print('|                                                             |')
    print('| Versão 2.0 de XX/maio/2025                                  |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto(solicitacao, mensagem, valido):
    digitouDireito = False
    while not digitouDireito:
        txt = input(solicitacao)

        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito = True

    return txt

def opcaoEscolhida (mnu):
    print()

    opcoesValidas = []
    posicao = 0
    while posicao < len(mnu):
        print (posicao + 1,') ',mnu[posicao], sep='')
        opcoesValidas.append(str(posicao + 1))
        posicao += 1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

'''
procura nom em agd e, se achou, retorna:
uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna:
uma lista contendo False e a posição onde inserir,
aquilo que foi buscado, mas nao foi encontrado,
mantendo a ordenação da lista.
'''
def ondeEsta(nom, agd):
    inicio = 0
    final = len(agd) - 1
    
    # continue a implementação que, entre outras coisas, deverá
    # calcular o meio, conforme segue:
    meio = (inicio + final) // 2
        
    # a função deverá retornar a lista [True,meio] quando encontrar o
    # nome procurado ou então a lista [False,inicio], quando não
    # encontrar o nome procurado.
    
    inicio = 0
    final = len(agd) - 1
    nom_lower = nom.lower()

##############################################
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
        nome = obtem_nome_validado("Digite o nome: ")

        achou, pos = ondeEsta(nome, agd)

        if achou:
            print("Este nome já está cadastrado. Tente outro")
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
    print('Opção não implementada!')
    # Ficar pedindo para digitar um nome até digitar um nome que existe
    # cadastrado;
    # mostrar então na tela TODOS os demais dados encontrados 
    # sobre aquela pessoa.
    # O usuário poderá desistir de procurar, escrevendo "cancela" no
    # momento de digitar o nome a ser procurado.

def atualizar(agd):
    print('Opção não implementada!')
    # Ficar solicitando a digitação de um nome a ser excluido da agenda,
    # até que um nome cadastrado seja digitado.
    # Ficar mostrando então um SUBMENU oferecendo as opções de atualizar
    # aniversário, ou endereco, ou telefone, ou celular, ou email, ou
    # finalizar as atualizações; ficar pedindo para digitar a opção até
    # digitar uma opção válida; realizar a atulização solicitada; tudo
    # isso até ser escolhida a opção de finalizar as atualizações.
    # REPARE que não foi prevista uma opção de atualizar o nome!
    # USAR A FUNÇÃO opcaoEscolhida, JÁ IMPLEMENTADA, PARA FAZER O MENU.
    # O usuário poderá desistir de atualizar, escrevendo "cancela" no
    # momento de digitar o nome a ser atualizado, ou, até mesmo, no
    # momento de digitar o aniversário ou o endereço ou o telefone (fixo)
    # ou o celular ou ainda o e_mail (caso o usuário tenha optado por
    # uma dessas atualizações, naturalmente).

def listar(agd):
    print('Opção não implementada!')
    # implementar aqui a listagem de todos os dados de todos
    # os contatos cadastrados
    # printar aviso de que não há contatos cadastrados se
    # esse for o caso

def excluir(agd):
    print('Opção não implementada!')
    # Ficar solicitando a digitação de um nome a ser excluido da agenda,
    # até que um nome cadastrado seja digitado.
    # Os dados encontrados deveriam então ser mostrados e a exclusão
    # deveria ser confirmada.
    # Sendo confirmada, a exclusão deveria ser realizada e uma mensagem
    # de exclusão bem sucedida deveria ser mostrada. Não sendo confirmada,
    # uma mensagem de exclusão não realizada deveria ser mostrada.
    # O usuário poderá desistir de excluir, escrevendo "cancela" no
    # momento de digitar o nome a ser excluído.
    
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