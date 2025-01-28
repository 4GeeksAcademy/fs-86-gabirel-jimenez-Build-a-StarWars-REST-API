from models import Planet
class PlanetServise:
    def __init__(self,id):
        self.id = id

    def get_list(self):
        planet_list = Planet.query.all()
        return [planet.serialize() for planet in planet_list]
    
    def get_list_byId(self, id ):
        planet_id = Planet.query.filter_by(id=id).all()
        return [planet.serialize_byId() for planet in planet_id]
