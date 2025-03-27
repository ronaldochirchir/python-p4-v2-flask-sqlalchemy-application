from faker import Faker
from models import db, Pet
from app import app

fake = Faker()

with app.app_context():
    db.create_all()
    
    pets = []
    species_list = ['Dog', 'Cat', 'Turtle', 'Hamster', 'Chicken']
    
    for _ in range(10):
        pet = Pet(name=fake.first_name(), species=fake.random.choice(species_list))
        pets.append(pet)

    db.session.add_all(pets)
    db.session.commit()

    print("Database seeded successfully!")
