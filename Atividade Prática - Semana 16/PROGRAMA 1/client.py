# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

import xmlrpc.client

# Estabelece a conexão com o servidor
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

mensagem = input("Digite uma mensagem: ")

resultado = server.inverter(mensagem)

# Mostra o resultado invertido
print("Resultado: ", resultado)

