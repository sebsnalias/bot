import config as config 

db = config.db 


def select_jugadores():
    try:
        return db.select('jugadores') 
    except Exception as e:
        print "Model select_jugadores Error {}".format(e.args)
        print "Model select_jugadores Message {}".format(e.message)
        return None



def select_numero(numero):
    try:
        return db.select('jugadores', where='numero=$numero', vars=locals())[0] 
    except Exception as e:
        print "Model select_numero Error {}".format(e.args)
        print "Model select_numero Message {}".format(e.message)
        return None


def insert_jugador(numero, nombre, pais, posicion, equipo):
    try:
        return db.insert('jugadores', numero=numero, nombre=nombre, pais=pais, posicion=posicion, equipo=equipo)
    except Exception as e:
        print "Model insert_jugador Error {}".format(e.args)
        print "Model insert_jugador Message {}".format(e.message)
        return None


def delete_jugador(numero):
    try:
        return db.delete('jugadores', where='numero=$numero', vars=locals()) 
    except Exception as e:
        print "Model delete_jugador Error {}".format(e.args)
        print "Model delete_jugador Message {}".format(e.message)
        return None


def update_jugador(numero, nombre, pais, posicion, equipo): 
    try:
        return db.update('jugadores',
            nombre=nombre,
            pais=pais,
            posicion=posicion,
            equipo=equipo,
            where='numero=$numero',
            vars=locals())
    except Exception as e:
        print "Model update_jugadores Error {}".format(e.args)
        print "Model update_jugadores Message {}".format(e.message)
        return None
