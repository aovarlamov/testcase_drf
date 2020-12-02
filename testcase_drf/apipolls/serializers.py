from rest_framework import serializers

from .models import Poll, Question, Answer, Choice


class AnswerListSerializer(serializers.ModelSerializer):
    """Работа с ответами"""

    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice = serializers.SlugRelatedField(queryset=Choice.objects.all(), slug_field='id', allow_null=True)
    answer_text = serializers.CharField(max_length=200, allow_null=True, required=False)

    class Meta:
        model = Answer
        fields = '__all__'

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validate_data):
        for key, val in validate_data.items():
            setattr(instance, key, val)
        instance.save()
        return instance


class ChoiceListSerializer(serializers.ModelSerializer):
    """Работа с выбором"""
    id = serializers.IntegerField(read_only=True)
    question = serializers.SlugRelatedField(queryset=Question.objects.all(), slug_field='id')
    choice_text = serializers.CharField(max_length=200)

    class Meta:
        model = Choice
        fields = '__all__'

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)

    def update(self, instance, validate_data):
        for key, val in validate_data.items():
            setattr(instance, key, val)
        instance.save()
        return instance


class QuestionListSerializer(serializers.ModelSerializer):
    """Работа с вопросами"""
    id = serializers.IntegerField(read_only=True)
    poll = serializers.SlugRelatedField(queryset=Poll.objects.all(), slug_field='id')
    question_text = serializers.CharField(max_length=200)
    question_type = serializers.CharField(max_length=200)
    choices = ChoiceListSerializer(many=True, read_only=True)

    def validate(self, attrs):
        question_type = attrs['question_type']
        if question_type == 'текст' or question_type == 'один вариант' or question_type=='несколько вариантов':
            return attrs
        raise serializers.ValidationError('Тип вопроса должен определяться как - "текст", "один вариант", '
                                          '"несколько вариантов"')

    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        return Question.objects.create(**validated_data)


class PollListSerializer(serializers.ModelSerializer):
    """Работа с опросами"""
    id = serializers.IntegerField(read_only=True)
    poll_name = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    poll_description = serializers.CharField(max_length=200)
    questions = QuestionListSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'pub_date' in validated_data:
            raise serializers.ValidationError('Вы не можете изменять дату начала опроса')
        for key, val in validated_data.items():
            setattr(instance, key, val)
        instance.save()
        return instance

