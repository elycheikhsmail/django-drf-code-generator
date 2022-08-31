from re import template
from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll
from django.template import loader

from django.template.loader import render_to_string

class Command(BaseCommand):
    help = ' g DRF class Serializer by name, Todo model for example' 
    def add_arguments(self, parser):
        parser.add_argument('model_name', nargs='+', type=str)
    
    def g_serializer_fn(self,model_name:str): 
        context = {'model_name':  model_name}
        text_serelazer_model_import = render_to_string('g/g_serelazer_model_import.txt',context)
        print()
        #print(text_serelazer_model_import)
        print() 

        text_serialezer_model = render_to_string('g/g_serialezer_model.txt',context)
        #print(text_serialezer_model)
        print()
      


        c  = ""
        f = open("eboutique_api/serializers.py", "r")
        c  = f.read()
        f.close()
        c2 = c.replace("#new_model_import", text_serelazer_model_import)
        print(c2)
        c3 = c2.replace("#new_class_def", text_serialezer_model)
        print(c3)

        #serializers
        f = open("eboutique_api/serializers.py", "w")
        f.write(c3)
        f.close()

    def handle(self, *args, **options):   
        self.g_serializer_fn(str(options['model_name'][0]))
        self.stdout.write(self.style.SUCCESS('Successfully done => update fields manualy'))