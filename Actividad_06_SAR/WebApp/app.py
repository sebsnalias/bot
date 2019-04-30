import web
        
urls = ('/', 'application.controllers.jugadores.index.Index',
    '/insert', 'application.controllers.jugadores.insert.Insert',
    '/update/(.*)', 'application.controllers.jugadores.update.Update',
    '/delete/(.*)', 'application.controllers.jugadores.delete.Delete',
    '/view/(.*)', 'application.controllers.jugadores.view.View',)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()

