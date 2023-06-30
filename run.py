# from src.main.routes.api_routes import app
from src.main.config.app import app 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)