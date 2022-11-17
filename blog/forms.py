from django import forms

class BlogForm (forms.Form) :
    title = forms.CharField(required=True)
    
    PILIHAN = {
        ('category1','Kdrama'),
        ('category2','Movies'),
        ('category3','Variety Show'),
        ('category4',''),
    }
    category = forms.ChoiceField(choices=PILIHAN)
    