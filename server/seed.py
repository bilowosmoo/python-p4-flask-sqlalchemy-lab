from app import app, db
from models import Animal, Zookeeper, Enclosure

with app.app_context():
    db.drop_all()
    db.create_all()

    z1 = Zookeeper(name="Ali", birthday="1980-05-12")
    z2 = Zookeeper(name="Fatuma", birthday="1991-07-23")

    e1 = Enclosure(environment="grass", open_to_visitors=True)
    e2 = Enclosure(environment="sand", open_to_visitors=False)

    a1 = Animal(name="Simba", species="Lion", zookeeper=z1, enclosure=e1)
    a2 = Animal(name="Twiga", species="Giraffe", zookeeper=z1, enclosure=e1)
    a3 = Animal(name="Nyoka", species="Snake", zookeeper=z2, enclosure=e2)

    db.session.add_all([z1, z2, e1, e2, a1, a2, a3])
    db.session.commit()
