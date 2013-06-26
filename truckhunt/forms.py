from django import forms
from gmapi.forms.widgets import GoogleMap

class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={}))
#    map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))
