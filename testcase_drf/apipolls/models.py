from django.db import models


class Poll(models.Model):
    """"Опрос"""
    poll_name = models.CharField('Название опроса', max_length=200)
    pub_date = models.DateTimeField('Дата публикации')
    end_date = models.DateTimeField('Дата окончания')
    poll_description = models.CharField('Описание опроса', max_length=200)

    def __str__(self):
        return self.poll_name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    """"Вопрос"""
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField('Текст вопроса', max_length=200)
    question_type = models.CharField('Тип вопроса', max_length=200)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    """"Варианты"""
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField('Текст варианта ответа', max_length=200)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Варианты'
        verbose_name_plural = 'Варианты'


class Answer(models.Model):
    """Ответ"""
    user_id = models.IntegerField('ID Пользователя')
    poll = models.ForeignKey(Poll, related_name='poll', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE, null=True)
    answer_text = models.CharField('Текст варианта ответа', max_length=200, null=True)

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

