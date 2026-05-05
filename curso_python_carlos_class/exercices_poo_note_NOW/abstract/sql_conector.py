from conector_db import ConectorDB

class MySQLConector(ConectorDB):
    def conectar(self):
        print("Conectado ao MySQL em localhost:3306")

    def executar_query(self, query: str):
        print(f"Executando '{query}' no MySQL.")