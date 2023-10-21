from django.forms import ModelForm
from animals.models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'text' ]
