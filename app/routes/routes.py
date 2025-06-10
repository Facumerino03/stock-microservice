class Route():

    def init_app(self, app):
        from app.controllers import stock_bp
        app.register_blueprint(stock_bp, url_prefix='/api/v1')