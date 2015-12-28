from django import forms


class teacherform(forms.Form):
    fn=forms.CharField(max_length=37)
    ls=forms.CharField(max_length=57)
    od=forms.CharField(max_length=100)
    pn=forms.CharField(max_length=15)
    email=forms.EmailField()


class courseform(forms.Form):
    name=forms.CharField(max_length=100)
    code=forms.CharField(max_length=11)
    croom=forms.CharField(max_length=10)
    time=forms.DateTimeField()
    tc=forms.CharField()

class studentform(forms.Form):
    fn=forms.CharField(max_length=37)
    ls=forms.CharField(max_length=57)
    crs=forms.CharField()
    email=forms.EmailField()