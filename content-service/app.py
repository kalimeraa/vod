from application import create_app, db
from flask_migrate import Migrate
import application.models
import application.observer

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)