'''
Implementar a opções do menu, sempre cuidando de validar os inputs do
usuário.
Usar, sempre que cabível, as funções prontas no código.

Fazer o trabalho em duplas e entregar duas semanas, ou seja, NÃO na
próxima aula, na seguinte.
Substituir, na função apresenteSe, o texto:
"Profs André Carvalho & J.G.Pícolo"
por um texto contendo os nomes e RAs dos alunos da dupla.
Também substituir o texto:
"Versão 1.0 de 12/maio/2025"
por
"Versão 2.0 de dd/mm/aaaa"
sendo dd/mm/aaaa a data que que a dupla concluiu seu trabalho.

A entrega será na forma de demonstração ao professor; os dois da dupla
deverão estar presentes na entrega e serão questionados pelo professor
sobre o programa que apresentam.
IMPORTANTE: este questionamento poderá resultar em notas diferentes para
os alunos da dupla, ou até em uma nota bem baixa para um programa que
funciona perfeitamente (basta estar perdido na demonstração).
'''




def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Brenda Maia Bergamasco                                      |')
    print('| Eliseu Pereira Gili - 25009281                              |')
    print('| Pietra Façanha Bortolato -                                  |')
    print('|                                                             |')
    print('| Versão 2.0 de /maio/2025                                    |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

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
def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    # continue a implementação que, entre outras coisas, deverá
    # calcular o meio, conforme segue:
    meio=(inicio+final)//2
        
    # a função deverá retornar a lista [True,meio] quando encontrar o
    # nome procurado ou então a lista [False,inicio], quando não
    # encontrar o nome procurado.




def cadastrar (agd):
    print('Opção não implementada!')
    # Ficar solicitando a digitação de um nome a ser excluido da agenda,
    # até que um nome NÃO CADASTRADO seja digitado.
    # Solicitar então a digitação do aniversario, do endereao, do
    # telefone (fixo), do celular e do e_mail da pessoa, cujo nome foi
    # digitado.
    # Gerar então uma lista conforme abaixo:
    # contato=[nome,aniversario,endereco,telefone,celular,email]
    # incluindo essa listinha chamada contato na listona chamada agd,
    # lembrando que agd é parâmetro formal desta função; o parâmetro
    # real que é fornecido no programa ao chamar esta função se chama
    # agenda.
    # Na listona, as listinhas deverão estar em ordem alfabética de
    # nome e o local apropriadoa para a inserção deverá ser obtido
    # usando a função ondeEsta, que realiza uma busca binária.
    # O usuário poderá desistir de cadastrar, escrevendo "cancela" no
    # momento de digitar o nome a ser cadastrado.
    # A função deverá terminar com uma mensagem informando cadastro
    # realizado com sucesso ou cadastro não realizado.

def procurar (agd):
    print('Opção não implementada!')
    # Ficar pedindo para digitar um nome até digitar um nome que existe
    # cadastrado;
    # mostrar então na tela TODOS os demais dados encontrados 
    # sobre aquela pessoa.
    # O usuário poderá desistir de procurar, escrevendo "cancela" no
    # momento de digitar o nome a ser procurado.

def atualizar (agd):
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

def listar (agd):
    print('Opção não implementada!')
    # implementar aqui a listagem de todos os dados de todos
    # os contatos cadastrados
    # printar aviso de que não há contatos cadastrados se
    # esse for o caso

def excluir (agd):
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
    
    
    
# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa
# (nosso CRUD, C=create(cadastrar), R=read(recuperar),
# U=update(atualizar), D=delete(remover,apagar)




apresenteSe()

agenda=[] # essa é a listona que deverá conter listinhas

menu=['Cadastrar Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

deseja_terminar_o_programa=False
while not deseja_terminar_o_programa:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        cadastrar(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
    else: # opcao==6
        deseja_terminar_o_programa=True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')