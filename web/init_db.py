import os
from app import app, db
from models import Bill, Cause, Discussion, Community


def init_db():
    # Ensure the instance folder exists
    if not os.path.exists('instance'):
        os.makedirs('instance')

    with app.app_context():
        db.create_all()

        # Add initial bills
        bill1 = Bill(title="Environmental Protection Act",
                     description="A bill to enhance environmental protection measures.")
        bill2 = Bill(title="Education Reform Bill",
                     description="A bill to improve the education system in Kenya.")
        db.session.add_all([bill1, bill2])

        # Add initial causes
        cause1 = Cause(title="Clean Water Initiative",
                       description="Provide clean water to rural communities.")
        cause2 = Cause(title="Digital Literacy Campaign",
                       description="Promote digital literacy across all age groups.")
        db.session.add_all([cause1, cause2])

        # Add initial discussions
        discussion1 = Discussion(title="Economic Recovery Post-COVID",
                                 content="Let's discuss strategies for economic recovery after the pandemic.")
        discussion2 = Discussion(title="Renewable Energy Solutions",
                                 content="What are the best renewable energy options for Kenya?")
        db.session.add_all([discussion1, discussion2])

        # Add Kenyan counties as communities
        counties = [
            "Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu", "Taita-Taveta", "Garissa", "Wajir", "Mandera", "Marsabit",
            "Isiolo", "Meru", "Tharaka-Nithi", "Embu", "Kitui", "Machakos", "Makueni", "Nyandarua", "Nyeri", "Kirinyaga",
            "Murang'a", "Kiambu", "Turkana", "West Pokot", "Samburu", "Trans-Nzoia", "Uasin Gishu", "Elgeyo-Marakwet",
            "Nandi", "Baringo", "Laikipia", "Nakuru", "Narok", "Kajiado", "Kericho", "Bomet", "Kakamega", "Vihiga",
            "Bungoma", "Busia", "Siaya", "Kisumu", "Homa Bay", "Migori", "Kisii", "Nyamira", "Nairobi"
        ]
        for county in counties:
            community = Community(name=f"{county} County")
            db.session.add(community)

        db.session.commit()


if __name__ == "__main__":
    init_db()
    print("Database initialized with sample data.")
