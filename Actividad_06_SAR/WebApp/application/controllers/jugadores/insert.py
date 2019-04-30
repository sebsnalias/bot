import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):
        return config.render.insert() # Renderiza la pagina insert.html

    def POST(self):
        formulario = web.input() # Almacena los datos del formulario
        numero = formulario['numero'] # Almacena el numero escrito en el input
        nombre = formulario['nombre'] # Almacena el nombre escrito en el input
        pais = formulario['pais'] # Almacena el pais escrito en el input
        posicion = formulario['posicion'] # Almacena el posicion escrito en el input
        equipo = formulario['equipo'] # Almacena el equipo escrito en el input
        config.model_jugadores.insert_jugador(numero, nombre, pais, posicion, equipo) # Llama al metodo insert_jugador y le pasa los datos guardados
        raise web.seeother('/') # Redirecciona al index.html
