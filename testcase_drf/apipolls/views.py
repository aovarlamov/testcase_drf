from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth import authenticate
from .models import Poll, Question, Answer, Choice
from .serializers import PollListSerializer, QuestionListSerializer, ChoiceListSerializer, AnswerListSerializer


class Login(APIView):
    """Авторизация через токен"""
    @csrf_exempt
    def get(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response('Впишите логин и пароль', status=400)
        user = authenticate(username=username, password=password)
        if not user:
            return Response('Данные введены неверно!', status=404)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'Ваш токен': token.key}, status=200)


class PollCreate(APIView):
    """Добавление новых опросов"""
    permission_classes = [IsAdminUser]

    def post(self, request):
        poll = PollListSerializer(data=request.data)
        if poll.is_valid():
            poll.save()
            return Response(status=201)
        return Response(status=400)


class PollUpdate(APIView):
    """Обновление опросов"""
    permission_classes = [IsAdminUser]

    def patch(self, request, poll_id):
        poll = get_object_or_404(Poll, pk=poll_id)
        serializer = PollListSerializer(poll, data=request.data, partial=True)
        if serializer.is_valid():
            poll = serializer.save()
            return Response(PollListSerializer(poll).data)
        return Response(status=400)


class PollDelete(APIView):
    """Удаление опросов"""
    permission_classes = [IsAdminUser]

    def delete(self, request, poll_id):
        poll = get_object_or_404(Poll, pk=poll_id)
        poll.delete()
        return Response(status=204)


class PollListView(APIView):
    """Вывод списка опросов"""
    permission_classes = [IsAdminUser]

    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollListSerializer(polls, many=True)
        return Response(serializer.data)


class PollListViewActive(APIView):
    """Вывод активных опросов"""
    permission_classes = [IsAdminUser]

    def get(self, request):
        polls = Poll.objects.filter(end_date__gte=timezone.now()).filter(pub_date__lte=timezone.now())
        serializer = PollListSerializer(polls, many=True)
        return Response(serializer.data)


class QuestionCreate(APIView):
    """Добавление новых вопросов"""
    permission_classes = [IsAdminUser]

    def post(self, request):
        question = QuestionListSerializer(data=request.data)
        if question.is_valid():
            question.save()
            return Response(status=201)
        return Response(status=400)


class QuestionUpdate(APIView):
    """Обновление вопросов"""
    permission_classes = [IsAdminUser]

    def patch(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        serializer = QuestionListSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionListSerializer(question).data)
        return Response(status=400)


class QuestionDelete(APIView):
    """Удаление вопросов"""
    permission_classes = [IsAdminUser]

    def delete(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        question.delete()
        return Response(status=204)


class ChoiceCreate(APIView):
    """Добавление новых выборов"""
    permission_classes = [IsAdminUser]

    def post(self, request):
        choice = ChoiceListSerializer(data=request.data)
        if choice.is_valid():
            choice.save()
            return Response(status=201)
        return Response(status=400)


class ChoiceUpdate(APIView):
    """Обновление выборов"""
    permission_classes = [IsAdminUser]

    def patch(self, request, choice_id):
        choice = get_object_or_404(Choice, pk=choice_id)
        serializer = ChoiceListSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid():
            choice = serializer.save()
            return Response(ChoiceListSerializer(choice).data)
        return Response(status=400)


class ChoiceDelete(APIView):
    """Удаление выборов"""
    permission_classes = [IsAdminUser]

    def delete(self, request, choice_id):
        choice = get_object_or_404(Choice, pk=choice_id)
        choice.delete()
        return Response(status=204)


class AnswerCreate(APIView):
    """Добавление новых ответов"""
    permission_classes = [IsAdminUser|IsAuthenticated]

    def post(self, request):
        answer = AnswerListSerializer(data=request.data)
        if answer.is_valid():
            answer.save()
            return Response(status=201)
        return Response(status=400)


class AnswerUpdate(APIView):
    """Обновление вопросов"""
    permission_classes = [IsAdminUser]

    def patch(self, request, answer_id):
        answer = get_object_or_404(Answer, pk=answer_id)
        serializer = AnswerListSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            answer = serializer.save()
            return Response(AnswerListSerializer(answer).data)
        return Response(status=400)


class AnswerDelete(APIView):
    """Удаление вопросов"""
    permission_classes = [IsAdminUser]

    def delete(self, request, answer_id):
        answer = get_object_or_404(Answer, pk=answer_id)
        answer.delete()
        return Response(status=204)


class AnswerView(APIView):
    """Вывод списка опросов по ID пользователя"""
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        answer = Answer.objects.filter(user_id=user_id)
        serializer = AnswerListSerializer(answer, many=True)
        return Response(serializer.data)
