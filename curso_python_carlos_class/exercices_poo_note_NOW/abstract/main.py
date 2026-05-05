from sql_conector import MySQLConector
# db = ConectorDB() # Isso causaria erro pois não pode ser instanciada
mysql = MySQLConector()
mysql.conectar()