import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, numero):
        jugadores = config.model_jugadores.select_numero(numero)
        return config.render.delete(jugadores)

    def POST(self, numero):
        formulario = web.input() 
        numero = formulario['numero'] 
        config.model_jugadores.delete_jugador(numero) 
        raise web.seeother('/') 
