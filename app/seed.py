from app import app
from models import Power, Hero, HeroPower, db
import random


def seed_database():
    with app.app_context():
        Power.query.delete()
        Hero.query.delete()
        HeroPower.query.delete()

        # Seeding powers
        print("🦸‍♀️ Seeding powers...")
        powers_data = [
            {"name": "super strength", "description": "gives the wielder super-human strengths"},
            {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
            {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
            {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
        ]

        powers = [Power(**power_data) for power_data in powers_data]
        db.session.bulk_save_objects(powers)

        # Seeding heroes
        print("🦸‍♀️ Seeding heroes...")
        heroes_data = [
            {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
            {"name": "Doreen Green", "super_name": "Squirrel Girl"},
            {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
            {"name": "Janet Van Dyne", "super_name": "The Wasp"},
            {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
            {"name": "Carol Danvers", "super_name": "Captain Marvel"},
            {"name": "Jean Grey", "super_name": "Dark Phoenix"},
            {"name": "Ororo Munroe", "super_name": "Storm"},
            {"name": "Kitty Pryde", "super_name": "Shadowcat"},
            {"name": "Elektra Natchios", "super_name": "Elektra"}
        ]

        heroes = [Hero(**hero_data) for hero_data in heroes_data]
        db.session.bulk_save_objects(heroes)

        # Adding powers to heroes
        print("🦸‍♀️ Adding powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]
        for hero in Hero.query.all():
            for _ in range(random.randint(1, 3)):
                # get a random power
                power = Power.query.order_by(db.func.random()).first()

                hero_power = HeroPower(hero_id=hero.id, power_id=power.id, strength=random.choice(strengths))
                db.session.add(hero_power)

        db.session.commit()

        print("🦸‍♀️ Done seeding!")


# Call the function to execute the script
seed_database()
