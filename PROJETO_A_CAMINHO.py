AGENDA = {}

def mostrar_contatos():

    if AGENDA:

        for contato in AGENDA:
            print("==========================")
            buscar_contato(contato)

    else:
        print('>>>>>>>>>> A agenda esta vazia')

def buscar_contato (contato):

    try:
         print ('Nome', contato)
         print ('telefone:', AGENDA[contato]['telefone'])
         print('endereco:', AGENDA[contato]['endereco'])
         print ('e-mail:', AGENDA[contato]['e-mail'])
         print ('==========================')


    except:
        print('usuario {} não existe!!!'.format(contato))

def ler_detalhes_contato():

    telefone = input('digite o telefone: ')
    endereco = input('digite o endereço: ')
    email = input('digite o e-mail: ')
    return telefone, endereco, email

def adicionar_editar_contato(contato, telefone, endereco, email ):

    AGENDA[contato]= {
        'telefone': telefone,
        'e-mail': email,
        'endereco': endereco,
    }
    salvar()
    print('contato {} adicionado/editado com sucesso'.format(contato,))


def excluir_contato (contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print('contato {} excluido com sucesso'.format(contato, ))
    except KeyError:
        print('>>>>>>> contato inexistente')
    except Exception as error:
        print('>>>>>>>> um erro inesperado aconteceu')
        print(error)


def exportar_contato(contatos):

    try:
        with open(contatos, 'w') as arquivo:
            for contato in AGENDA:
                telefone=(AGENDA[contato]['telefone'])
                endereco=(AGENDA[contato]['endereco'])
                email=(AGENDA[contato]['e-mail'])
                arquivo.write('{},{}, {}, {}, \n'.format(contato, telefone, endereco, email, ))
            print('>>>>>>>> Agenda importada com sucesso')

    except Exception as error:

        print(error)
        print('algum erro ocorreu!!')


def importar_arquivo(contatos):
    try:
        with open(contatos, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = (linha.strip().split(','))

                nome = detalhes[0]
                telefone = detalhes [1]
                endereco = detalhes [2]
                email = detalhes [3]

                adicionar_editar_contato(nome, telefone, endereco, email)

    except FileNotFoundError:

        print('>>>>>> arquivo não encontrado')

    except Exception as error:

        print(error)


def salvar():
    exportar_contato('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = (linha.strip().split(','))

                nome = detalhes[0]
                telefone = detalhes [1]
                endereco = detalhes [2]
                email = detalhes [3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'e-mail': email,
                    'endereco': endereco,
                }
        print('>>>>>>> database carregado com sucesso!!!')
        print('>>>>>>> {} contatos carregados'.format(len(AGENDA)))

    except FileNotFoundError:

        print('>>>>>> arquivo não encontrado')

    except Exception as error:

        print(error)


def imprimir_menu():
    print('1 - mostrar todos os contatos da agenda')
    print('2 - buscar contato')
    print('3 - adicionar contato')
    print('4 - editar contato')
    print('5 - excluir contato')
    print('6 - exportar contato')
    print('7 - importar contato')
    print('0 - fechar agenda')


carregar()

while True:

    imprimir_menu()

    opcao = input("escolha uma opção: ")

    if opcao == '1':
        mostrar_contatos()

    elif opcao == '2':
        contato = input('insira o contato que deseja buscar: ')
        buscar_contato(contato)

    elif opcao == '3':
        contato = input('digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>>>>>> contato {} já existente'.format(contato, ))

        except KeyError:

            telefone, endereco, email = ler_detalhes_contato()
            adicionar_editar_contato(contato, telefone, endereco, email )

    elif opcao == '4':

        contato = input('insira o nome que deseja editar: ')

        try:

            AGENDA[contato]
            print('>>>>>> Editando contato. ')

            telefone, endereco, email = ler_detalhes_contato()
            adicionar_editar_contato(contato, telefone, endereco, email)

        except KeyError:

            print('>>>>>>>contato inexistente. ')



    elif opcao == '5':
        try:
            contato = input('insira o nome que deseja excluir: ')
            excluir_contato(contato)
        except KeyError:
            print('>>>>>>>>> conatato inexistente')

    elif opcao == '6':
        contatos = input('insira o nome do arquivo a ser exportado: ')
        exportar_contato(contatos)

    elif opcao == '7':
        contatos = input('insira o nome do arquivo: ')
        importar_arquivo(contatos)

    elif opcao == '0':
        print('fechando programa')
        break
    else:
        print('opção invalida!')
