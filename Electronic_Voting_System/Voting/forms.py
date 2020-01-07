from django.forms import ModelForm

from .models import *

class VotingEventForm(ModelForm):
    class Meta:
        model = VotingEvent
        fields = ['event_name',
                  'event_description',
                  'is_public',
                  'enrolled_users'
                  ]

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text'
                  ]

class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text'
                  ]






