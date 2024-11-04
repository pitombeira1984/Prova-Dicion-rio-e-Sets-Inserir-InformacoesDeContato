
def InserirInformacoesDeContato():
    dados_usuario = {}
    while True:
        try:
            dados_usuario['id'] = int(input('Digite o ID do contato: '))
            break
        except ValueError:
            print('O ID deve ser um número inteiro. Tente novamente.')
    dados_usuario['nome'] = input('Digite o nome do contato: ')
    dados_usuario['telefone'] = input('Digite o telefone do contato: ')
    dados_usuario['email'] = input('Digite o email do contato: ')
    return dados_usuario
print(InserirInformacoesDeContato())