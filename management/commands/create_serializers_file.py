from re import template
from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll
from django.template import loader

from django.template.loader import render_to_string

class Command(BaseCommand):
    help = 'create file serilazer.py with needed import'  
    
    def create_serilazer(self):   
        text = render_to_string('g/g_serilazer_empty.txt',{})
        print(text)
        f = open("eboutique_api/serializer.py", "w")
        f.write(text)
        f.close()

    def handle(self, *args, **options):   
        self.create_serilazer()
        self.stdout.write(self.style.SUCCESS('Successfully create serilazer.py file'  ))