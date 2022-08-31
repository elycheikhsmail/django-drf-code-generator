# create views_{{model_name|lower}}.py in right folder
# generate text from view_by_model_template 
from django.core.management.base import BaseCommand, CommandError 
from django.template.loader import render_to_string

class Command(BaseCommand):
    help = 'create file serilazer.py with needed import' 
    
    def add_arguments(self, parser):
        parser.add_argument('model_name', nargs='+', type=str)
     
    def create_view(self,model_name:str):   
        context = dict(model_name=model_name)
        text = render_to_string('g/g_view_by_model.txt',context) 
        f = open(f"eboutique_api/view_{model_name.lower()}.py", "w")
        f.write(text)
        f.close()

    def handle(self, *args, **options):   
        model_name = str(options['model_name'][0])
        self.create_view(model_name)
        self.stdout.write(self.style.SUCCESS('Successfully create serilazer.py file'  ))