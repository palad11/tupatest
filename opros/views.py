from django.shortcuts import render
from .models import *

def test(request, id):
    testOpros = Opros.objects.filter(pk=id)
    print(testOpros[0].opros.all())
    questions = testOpros[0].opros.all()

    #question = Question.objects.all()
    answer = []
    for answer_model in questions[0].answers.all():
        answer.append(answer_model)
    #questions = []
    # for unit in testUnit:
    #     items_keys = [x for x in range(len(unit.questions.all()))]
    #     needed_items = random.sample(items_keys,unit.questions_limit)
    #     print(unit.questions_limit)
    #     print(items_keys, needed_items)
    #     for i, x in enumerate(unit.questions.all()):
    #         print(i)
    #         if i in needed_items:
    #             # print(x.id)
    #             questions.append(x)


    #print(questions)


    return render(request, 'opros/main.html', {'link': 'check_test','questions': questions, 'testScenarios':testOpros,'answers':answer})
