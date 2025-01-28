from models import People
class PeopleService:
    def __init__(self,id):
        self.id = id

    def get_list(self):
        people_list = People.query.all()
        return [people.serialize() for people in people_list]
    
    def get_list_byId(self, id ):
        person_id = People.query.filter_by(id=id).all()
        return [person.serialize_byId() for person in person_id]