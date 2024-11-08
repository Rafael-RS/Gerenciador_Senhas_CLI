import sys, os
sys.path.append(os.path.abspath(os.curdir))

from model.passwords import Password
from view.password_view import FernetHasher

action = input('Digite 1 para salvar uma senha e 2 para ver uma senha: ')

match action:
    case '1':
        if len(Password.get()) == 0:
            key, path = FernetHasher.create_key(arquive=True)
            print('Sua chave foi criada com sucesso.')
            print(f'Chave: {key.decode("utf-8")}')
            if path:
                print('Chave salva no arquivo, lembre-se de remover o arquivo apos transferir de local')
                print(f'Caminho: {path}')
        
        else:
            key = input('Digite a chave: ')

        domain = input('Dominio: ')
        password = input('Password: ')
        fernet_User = FernetHasher(key)
        p1 = Password(domain=domain, password=fernet_User.encrypt(password).decode('utf-8')) 
        p1.save()

    case '2':
        domain = input('Dominio: ')
        key = input('Chave: ')
        fernet_User = FernetHasher(key)
        data = Password.get()

        for i in data:
            if domain in i['domain']:
                password = fernet_User.decrypt(i['password'])
        if password:
            print(f'Sua senha e: {password}')
        else:
            print(f'Nenhuma senha encontrada para o dominio')