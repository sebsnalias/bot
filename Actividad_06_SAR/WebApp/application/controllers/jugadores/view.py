import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, numero):
        jugador = config.model_jugadores.select_numero(numero)
        return config.render.view(jugador) 
