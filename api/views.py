from api.models import GameRoom, Player, Question, Answer
from api.serializers import GameRoomSerializer, PlayerSerializer, QuestionSerializer, AnswerSerializer
from rest_framework import generics
from rest_framework.exceptions import AuthenticationFailed


class GameRoomCreateView(generics.CreateAPIView):
    queryset = GameRoom.objects.all()
    serializer_class = GameRoomSerializer


class PlayerCreateView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def post(self, request, *args, **kwargs):
        try:
            GameRoom.objects.get(**request.data['game_room'])
        except:
            raise AuthenticationFailed('Your GameRoom or Password was incorrect')
        return super(PlayerCreateView, self).post(request, *args, **kwargs)



class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerUpdateView(generics.UpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerListView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Answer.objects.filter(question_id=kwargs['pk'])
        return super(AnswerListView, self).get(request, *args, **kwargs)


class PlayerDestroyView(generics.DestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer