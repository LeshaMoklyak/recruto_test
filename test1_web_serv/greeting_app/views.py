from django.shortcuts import render


def greeting(requests):
    name = requests.GET.get('name', 'Recruto')
    message = requests.GET.get('message', 'Давай дружить')

    return render(requests, 'greeting/index.html', context={'name': name, 'message': message})
