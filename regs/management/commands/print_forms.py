import os

from django.core.management.base import BaseCommand
from django.template.loader import get_template


class Command(BaseCommand):
    help = 'Распечатать формы воинского учета'

    def handle(self, *args, **options):
        
        context = {
            "personnel": ""
        }
        template = get_template('card-template.html')
        html  = template.render(context)
        
        if not os.path.exists('records'):
            os.makedirs('records')

        with open('records/file.html', 'w', encoding='utf8') as file:
            file.write(html)