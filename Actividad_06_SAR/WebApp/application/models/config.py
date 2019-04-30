import web
'''
Parametros de configuracion para conectarse a una base de datos MySQL o MariaDB
'''

db = web.database(
    dbn='mysql', # Motor de base de datos
    host='localhost', # Ruta del servidor
    db='brawlbot', # Nombre de la Base de Datos
    user='brawlbot1', # Usuario de la Base de Datos
    pw='brawlbot.2019', # Password del usuario
    port = 3306 # Puerto de MariaDB
    )
