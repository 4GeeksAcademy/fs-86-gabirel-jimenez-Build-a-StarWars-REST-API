from models import Favorite

class FavoriteService:
    def get_list(self):
        favorite_list = Favorite.query.all()
        return [favorite.serialize() for favorite in favorite_list]