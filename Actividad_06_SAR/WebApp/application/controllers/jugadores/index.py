import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):
        jugadores = config.model_jugadores.select_jugadores().list() # Selecciona todos los registros de jugadores de la BD
        return config.render.index(jugadores) # Envia todos los registros y renderiza index.html
