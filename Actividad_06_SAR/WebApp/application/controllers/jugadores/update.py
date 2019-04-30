import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, numero):
        jugador = config.model_jugadores.select_numero(numero) 
        return config.render.update(jugador)

    def POST(self, nombre, pais, posicion, equipo):
        formulario = web.input() 
        numero = formulario['numero'] 
        nombre = formulario['nombre']
        pais = formulario['pais']
        posicion = formulario['posicion'] 
        equipo = formulario['equipo'] 
        config.model_jugadores.update_jugador(numero, nombre, pais, posicion, equipo) 
        raise web.seeother('/') # Redirecciona al index.html
