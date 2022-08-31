from re import template
from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll
from django.template import loader

from django.template.loader import render_to_string

class Command(BaseCommand):
    help = ' g django model class by name, Todo model for example' 
    def add_arguments(self, parser):
        parser.add_argument('model_name', nargs='+', type=str)
    
    def g_model_fn(self,model_name:str): 
        context = {'model_name':  model_name}
        text = render_to_string('g/g_model_class.txt',context)
        print(text)
        f = open("eboutique_api/models.py", "a")
        f.write(text)
        f.close()

    def handle(self, *args, **options):   
        self.g_model_fn(str(options['model_name'][0]))
        self.stdout.write(self.style.SUCCESS('Successfully run commande g code 1'  ))