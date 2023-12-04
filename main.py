AGENDA = {}


def mostrar_menu():
    print('-------------------------')
    print('1 - Mostrar todos os contatos')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contatos CSV')
    print('7 - Importar contatos CSV')
    print('0 - Fechar agenda')
    print('-------------------------')


def carregar_agenda():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            contador_contatos = 0
            for linha in linhas:
                dados = linha.strip().split(',')
                nome = dados[0]
                email = dados[1]
                tel = dados[2]
                end = dados[3]
                adicionar_e_editar_contato(nome, email, tel, end)
                contador_contatos += 1

            print('\n>>> {} contato(s) carregados.'.format(contador_contatos))
    except FileNotFoundError:
        print('\n>>> Arquivo nao encontrado.')
    except Exception as error:
        print('\n>>> Algum erro ocorreu.')
        print(error)


def salvar_agenda():
    exportar_contatos('database.csv')


def mostrar_info_contato(contato):
    print('\nNome: {}'.format(contato))
    print('Email: {}'.format(AGENDA[contato]['email']))
    print('Telefone: {}'.format(AGENDA[contato]['telefone']))
    print('Endereco: {}'.format(AGENDA[contato]['endereco']))


def mostrar_todos_contatos():
    if AGENDA:
        for contato in AGENDA:
            mostrar_info_contato(contato)
    else:
        print('\n>>> Agenda vazia.')

def buscar_contato(contato):
    try:
        mostrar_info_contato(contato)
    except KeyError:
        print('\n>>> Contato nao existe.')
    except Exception as error:
        print('\n>>> Algum erro ocorreu.')
        print(error)


def adicionar_e_editar_contato(contato, email, telefone, endereco):
    AGENDA[contato] = {
        'email': email,
        'telefone': telefone,
        'endereco': endereco
    }


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar_agenda()
        print('\nContato {} excluido com sucesso.'.format(contato))
    except KeyError:
        print('\n>>> Contato nao existe.')
    except Exception as error:
        print('\n>>> Algum erro ocorreu.')
        print(error)


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                email = AGENDA[contato]['email']
                tel = AGENDA[contato]['telefone']
                end = AGENDA[contato]['endereco']
                arquivo.write('{},{},{},{}\n'.format(contato,email,tel,end))
    except Exception as error:
        print('\n>>> Algum erro ocorreu.')
        print(error)


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            contador_de_contatos = 0
            for linha in linhas:
                dados = linha.strip().split(',')
                nome = dados[0]
                email = dados[1]
                tel = dados[2]
                end = dados[3]
                adicionar_e_editar_contato(nome, email, tel, end)
                contador_de_contatos += 1
        salvar_agenda()
        print('\n>>> {} contato(s) importados com sucesso.'.format(contador_de_contatos))
    except FileNotFoundError:
        print('\n>>> Arquivo nao encontrado.')
    except Exception as error:
        print('\n>>> Algum erro ocorreu.')
        print(error)



# INICIO DO PROGRAMA
carregar_agenda()
while True:
    mostrar_menu()
    opcao = input('Selecione uma opcao: ')

    if opcao == '1':
        mostrar_todos_contatos()
    elif opcao == '2':
        contato = input('Digite o contato: ')
        buscar_contato(contato)
    elif opcao == '3' or opcao == '4':
        contato = input('Digite o contato: ')
        if contato in AGENDA:
            print('\nEditando contato {}:'.format(contato))
            email = input('Digite o novo email: ')
            tel = input('Digite o novo telefone: ')
            end = input('Digite o novo endereco: ')
            adicionar_e_editar_contato(contato, email, tel, end)
            salvar_agenda()
            print('\n>>> Contato {} editado com sucesso.'.format(contato))
        else:
            print('\nAdicionando novo contato {}:'.format(contato))
            email = input('Digite o email: ')
            tel = input('Digite o telefone: ')
            end = input('Digite o endereco: ')
            adicionar_e_editar_contato(contato, email, tel, end)
            salvar_agenda()
            print('\n>>> Contato {} adicionado com sucesso.'.format(contato))
    elif opcao == '5':
        contato = input('Digite o contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo que deseja exportar (ex.: agenda.csv):')
        exportar_contatos(nome_do_arquivo)
        print('\n>>> Contatos exportados atraves do arquivo {}'.format(nome_do_arquivo))
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo que deseja importar (ex.: agenda.csv):')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('\n>>> Fechando agenda.')
        break
    else:
        print('\n>>> Opcao invalida. Tente novamente.')