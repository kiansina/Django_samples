$ python manage.py shell

from polls.models import Choice, Question
from django.utils import timezone

q = Question.objects.get(pk=2)



q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='42', votes=0)
q.choice_set.create(choice_text='21', votes=0)

q.choice_set.all()
