# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

import xmlrpc.client

# Conecta ao servidor RPC
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

result = server.add(x, y)

# Mostra o resultado
print("Resultado:", result)

