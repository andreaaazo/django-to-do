from django.forms import ModelForm, CharField, Textarea, TextInput
from .models import Thing


class CreateThing(ModelForm):
    body = CharField(
        max_length=20,
        label="",
        widget=TextInput(
            attrs={"class": "form-control form-control-lg", "placeholder": "ex. study"}
        ),
    )

    class Meta:
        model = Thing
        fields = ["body"]
