import json
import random

from django.conf import settings
from django.core.management.base import BaseCommand, CommandParser



DATA_DIR = settings.BASE_DIR / "data" / "riddles.json"

class Command(BaseCommand):

    """
    Load the riddle json data from the data/riddles.json.
    """

    def add_arguments(self, parser: CommandParser) -> None:
        
        parser.add_argument("--yield", action="store_true", default=False)
        parser.add_argument("-a", "--all", action="store_true", default=False)

    def handle(self, *args, **options):
        yield_data = options['yield']
        all_data = options['all']

        if yield_data:
            print(next(self.yield_data()))
        
        if all_data:
            print(self.get_data())
        else:
            print(self.get_random_riddle())

    def yield_data(self):

        with open(DATA_DIR, "r", encoding='utf-8') as json_file:
            data = json.load(json_file)
            for obj in data:
                yield obj
    
    def get_data(self):

        with open(DATA_DIR, "r", encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data


    def get_random_riddle(self):
        data = self.get_data()
        new_data = random.choice(data)

        return new_data