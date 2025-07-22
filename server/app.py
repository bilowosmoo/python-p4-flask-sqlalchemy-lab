from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Animal, Zookeeper, Enclosure

@app.route("/animal/<int:id>")
def animal_by_id(id):
    animal = Animal.query.get_or_404(id)
    return f'''
    <ul>
        <li>Name: {animal.name}</li>
        <li>Species: {animal.species}</li>
        <li>Zookeeper: {animal.zookeeper.name}</li>
        <li>Enclosure: {animal.enclosure.environment}</li>
    </ul>
    '''

@app.route("/zookeeper/<int:id>")
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get_or_404(id)
    animals = "".join(f"<li>{a.name} ({a.species})</li>" for a in zookeeper.animals)
    return f'''
    <ul>
        <li>Name: {zookeeper.name}</li>
        <li>Birthday: {zookeeper.birthday}</li>
        <li>Animals:<ul>{animals}</ul></li>
    </ul>
    '''

@app.route("/enclosure/<int:id>")
def enclosure_by_id(id):
    enclosure = Enclosure.query.get_or_404(id)
    animals = "".join(f"<li>{a.name} ({a.species})</li>" for a in enclosure.animals)
    return f'''
    <ul>
        <li>Environment: {enclosure.environment}</li>
        <li>Open to Visitors: {enclosure.open_to_visitors}</li>
        <li>Animals:<ul>{animals}</ul></li>
    </ul>
    '''
if __name__ == "__main__":
    app.run(debug=True)