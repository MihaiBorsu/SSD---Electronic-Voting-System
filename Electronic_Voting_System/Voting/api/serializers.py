from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from ..models import (
    VotingEvent,
    Question,
    Choice,
)


class EventListSerializer(ModelSerializer):
    class Meta:
        model = VotingEvent
        fields = [
            'id',
            'event_name',
            'event_description',
            'pub_date',
            'is_public',
            'owner',
            'enrolled_users'
        ]

class EventCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = VotingEvent
        fields = [
            'event_name',
            'event_description',
            'pub_date',
            'is_public',
            'enrolled_users'
        ]

class QuestionListSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'id',
            'voting_event',
            'question_text',
            'pub_date',
            'voted_users',
        ]

class QuestionCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'voting_event',
            'question_text',
            'pub_date',
            #'voted_users',
        ]


class ChoiceListSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'id',
            'question',
            'choice_text',
            'choice_count',
        ]

class ChoiceCreateUodateSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'question',
            'choice_text',
            #'choice_count',
        ]
