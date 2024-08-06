from django.forms import ModelForm
from resumes.models import Resume
from django.forms.widgets import TextInput, Textarea, CheckboxInput, EmailInput


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ["name", "email", "introduce", "profile", "online"]
        widgets = {
            "name": TextInput(attrs={"class": "input"}),
            "email": EmailInput(attrs={"class": "input"}),
            "introduce": TextInput(attrs={"class": "input"}),
            "profile": Textarea(attrs={"class": "textarea", "rows": 5}),
            "online": CheckboxInput(attrs={"class": "input"}),
        }

        labels = {
            "name": "姓名",
            "email": "Email",
            "introduce": "簡介",
            "profile": "個人檔案",
            "online": "是否上線",
        }
