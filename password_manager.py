from cryptography.fernet import Fernet

""" !! nao rodar func mais de uma vez!!
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
"""

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def ver():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip().split('|')
            if len(data) == 2:
                user , passw = data
                print("user:", user, "passw:", fer.decrypt(passw.encode()).decode())

def add():
    nome = input('Nome da conta: ')
    pwd = input('Senha: ')

    with open('password.txt', 'a') as f:
        f.write(nome + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("voce quer adicionar uma nova senha ou ver as existentes(digite S para sair): ").lower()

    if mode == "s":
        break

    if mode == "ver":
        ver()
    elif mode == "adicionar":
        add()
    else:
        print("Opção inválida!")
        continue

    