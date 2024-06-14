import logging
from flask import Flask

def create_app() -> Flask:
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)

    app.secret_key = 'your_secret_key'  # Replace with a secure random key in production
    
    # Configure logging
    logging.basicConfig(filename='app.log', level=logging.INFO, 
                        format='%(asctime)s %(levelname)s: %(message)s')
    logger = logging.getLogger()

    with app.app_context():
        from . import main
        app.register_blueprint(main.bp)

    return app

