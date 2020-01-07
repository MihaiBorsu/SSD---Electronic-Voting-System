from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
)

from ..models import (
    VotingEvent,
    Question,
    Choice,
)

from .serializers import (
    EventListSerializer,
    EventCreateUpdateSerializer,
    QuestionListSerializer,
    QuestionCreateUpdateSerializer,
    ChoiceListSerializer,
    ChoiceCreateUodateSerializer,
)

class ChoiceAPIView(ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceListSerializer

class ChoiceFormAPIView(CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceCreateUodateSerializer

class EventAPIView(ListAPIView):
    queryset = VotingEvent.objects.all()
    serializer_class = EventListSerializer

class EventFormAPIView(CreateAPIView):
    queryset = VotingEvent.objects.all()
    serializer_class = EventCreateUpdateSerializer

class QuestionAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer

class QuestionFormAPIView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateUpdateSerializer





