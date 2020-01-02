from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    age = forms.IntegerField(label="возраст", widget=forms.Textarea)

    name2 = forms.CharField(label="Имя_2", initial="undefined")
    age2 = forms.IntegerField(label="Возраст_2", initial=18)
    field_order = ["age2"]

    # widget = forms.TextInput(attrs={'placeholder': 'Search'}))
    name3 = forms.CharField(help_text="Введите свое имя", label="имя 3",
            widget=forms.TextInput(attrs={'placeholder': 'сюда надобно ввести свое имя'} ))
            # widget = forms.CharField(attrs={'placeholder': 'надобно ввести свое имя'}))
            # с CharField не хочет

    age3 = forms.IntegerField(label="Возраст 3", initial=50, help_text="Введите свой возраст")
    # age3 = forms.IntegerField(label="Возраст 3", initial=50)


class UserForm2(forms.Form):
    name = forms.CharField(min_length=2, max_length=10)
    age = forms.IntegerField(required=False)
    email = forms.EmailField(required=False, min_length=7)
    weight = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)

class UserForm3(forms.Form):
    name = forms.CharField(min_length=3)
    age = forms.IntegerField(min_value=1, max_value=100)
    required_css_class = "field"
    error_css_class = "error"

class UserForm4(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':"myfield"} ) )
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"myfield"} ))



