# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

from xmlrpc.server import SimpleXMLRPCServer

def inverter_string(string):
    return string[::-1]

server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor iniciado...")

server.register_function(inverter_string, "inverter")

server.serve_forever()
