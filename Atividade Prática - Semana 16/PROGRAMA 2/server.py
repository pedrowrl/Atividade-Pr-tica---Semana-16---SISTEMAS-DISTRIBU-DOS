# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

import xmlrpc.server

class MathServer:
    def add(self, x, y):
        return x + y

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(MathServer())
print("Servidor iniciado.")
server.serve_forever()
