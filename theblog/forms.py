from django import forms
from .models import Post,Category

# choices = [('coding','coding'),('martial arts', 'martial arts'),('motor cycle', 'motor cycle')]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','category', 'body')
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title Here'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','type':'hidden','id':'elder'}),
            # 'author' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }