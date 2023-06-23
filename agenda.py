def contarContatos():
    try:
        with open("agenda.txt", "r") as agenda:
            return len(agenda.readlines())
    except FileNotFoundError:
        return 0

def atualizarContato():
    nomeDeletado = input("Digite o nome para ser Atualizado: ").lower()
    with open("agenda.txt", "r") as agenda:
        aux = []
        aux2 = []
        for i in agenda:
            aux.append(i)
        for i in range(0, len(aux)):
            if nomeDeletado not in aux[i].lower():
                aux2.append(aux[i])
    with open("agenda.txt", "w") as agenda:
        for i in aux2:
            agenda.write(i)
    idContato = input("Escolha o Id do contato atualizado: ")
    nome = input("Escreva o nome do contato atualizado: ")
    telefone = input("Escreva o telefone do contato atualizado: ")
    email = input("Escreva o email do contato atualizado: ")
    try:
        with open("agenda.txt", "a") as agenda:
            dados = f'{idContato};{nome};{telefone};{email}\n'
            agenda.write(dados)
        print('Contato Atualizado com sucesso!!!!')
    except:
        print("ERRO na gravação do contato")

def cadastrarContato():
    idContato = input("Escolha o Id do contato: ")
    nome = input("Escreva o nome do contato: ")
    telefone = input("Escreva o telefone do contato: ")
    email = input("Escreva o email do contato: ")
    try:
        with open("agenda.txt", "a") as agenda:
            dados = f'{idContato};{nome};{telefone};{email}\n'
            agenda.write(dados)
        print('Contato gravado com sucesso!!!!')
    except:
        print("ERRO na gravação do contato")

def listarContato():
    try:
        with open("agenda.txt", "r") as agenda:
            for contato in agenda:
                print(f'{contato.split(";")[0]}  {contato.split(";")[1]}  {contato.split(";")[2]}  {contato.split(";")[3]}')
    except FileNotFoundError:
        print("Nenhum contato cadastrado.")

def deletarContato():
    nomeDeletado = input("Digite o nome para ser deletado: ").lower()
    with open("agenda.txt", "r") as agenda:
        aux = []
        aux2 = []
        for i in agenda:
            aux.append(i)
        for i in range(0, len(aux)):
            if nomeDeletado not in aux[i].lower():
                aux2.append(aux[i])
    with open("agenda.txt", "w") as agenda:
        for i in aux2:
            agenda.write(i)
    print('Contato deletado com sucesso')
    listarContato()

def buscarContatoPeloNome():
    nome = input('Digite o nome a ser procurado: ').upper()
    try:
        with open("agenda.txt", "r") as agenda:
            for contato in agenda:
                if nome in contato.split(";")[1].upper():
                    print(contato)
    except FileNotFoundError:
        print("Nenhum contato cadastrado.")

def ultimoContatoCadastrado():
    try:
        with open("agenda.txt", "r") as contatos:
            linhas = contatos.readlines()
            if linhas:
                ultimoContato = linhas[-1]
                return ultimoContato
            else:
                return "Nenhum contato cadastrado."
    except FileNotFoundError:
        return "Nenhum contato cadastrado."

def sair():
    print('Até mais... !!!')
    exit()

def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao = input('''
  =================================================================
                    PROJETO AGENDA EM PYTHON                v.1
                                +
                                + {} CONTATOS CADASTRADOS
                                +
  MENU:                         + ÚLTIMO CADASTRO
                                + {}
  [1]CADASTRAR CONTATO          +
  [2]LISTAR CONTATO             +
  [3]DELETAR CONTATO            +     
  [4]BUSCAR CONTATO PELO NOME   +
  [5]ATUALIZAR CONTATO          +
  [6]SAIR                       +
                                +
  ==================================================================

  ESCOLHA UMA OPÇÃO ACIMA: 
  
  '''.format(contarContatos(), ultimoContatoCadastrado()))
        
        if opcao == "1":
            cadastrarContato()
        elif opcao == "2":
            listarContato()
        elif opcao == "3":
            deletarContato()
        elif opcao == "4":
            buscarContatoPeloNome()
        elif opcao == '5':
            atualizarContato()
        elif opcao == '6':
            sair()
        else:
            print("Opção inválida")
        voltarMenuPrincipal = input("Deseja voltar ao menu principal? (s/n) ").lower()

def main():
    menu()

main()
