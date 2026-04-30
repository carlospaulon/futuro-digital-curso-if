from conta_desativada_exception import ContaDesativadaException

class Main:
    def __init__(self, user, password, is_active):
        self.user = user
        self.password = password
        self.is_active = is_active
        self.users = {}

    def sign_up(self):
        self.users[self.user] = (self.password, self.is_active)
    
    def login(self, user, password):

        # user in users - else com raise
        if user in self.users:
            values = self.users.get(user)
            pswd = values[0] # em 0 está a senha, em 1 o status de administrador
            status = values[1]

            if not status:
                raise ContaDesativadaException('Conta desativada', 'is_active')
            else:
                if pswd == password:
                    return True
                else:
                    raise PermissionError('Senha inválida')
        else:
            raise KeyError('Usuário incorreto')

    def __str__(self):
        print(self.users)


if __name__ == '__main__':

    try:
        print('Criando o usuário')
        user = input('Informe o usuário: ')
        password = input('Informe a senha: ')
        status_inp = input('Está ativado (s)im ou (n)ao: ')
        status = True

        if status_inp.lower().startswith('n'):
            status = False
        else:
            status = True
        teste = Main(user, password, status)
        teste.sign_up()


        print('\nLogando o usuário')
        user_log = input('Informe o usuário: ')
        passwrod_log = input('Informe a senha: ')
        logou = teste.login(user_log, passwrod_log)
        if logou:
            print('Login realizado com sucesso')
            print(teste.users)

    except KeyError as e:
        print(e)
    except PermissionError as e:
        print(e)
    except ContaDesativadaException as e:
        print(e)
        print(f'Erro no campo {e.nome_campo}')
    except Exception as e:
        print(f'Erro inesperado: {e}')
    finally:
        print('finalizando execução')