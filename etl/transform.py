from datetime import datetime


class AnimalTransformer:

    def transform(self, animal: dict):
        friends = animal.get('friends', '')
        animal['friends'] = [f.strip() for f in friends.split(',')] if friends else []

        born_at = animal.get('born_at')
        if born_at:
            try:
                dt = datetime.utcfromtimestamp(born_at//1000)
                animal['born_at'] = f'{dt.isoformat()}Z'
            except Exception:
                animal['born_at'] = None

        return animal
