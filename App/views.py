from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import datetime
from django.urls import reverse
from .forms import MessageForm
from .models import Message


class HomeView(TemplateView):
    template_name = 'Page/index.html'

    def Home(self, request):
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits+1
        return render(request, self.template_name, context={'num_visits': num_visits})


@login_required()
def message_page(request):
    messages = Message.objects.filter(author=request.user)
    date = datetime.now().strftime("%Y-%m-%d")
    errors = {}
    ckboxs = request.POST.getlist('status')
    mode = request.POST.get('status_select')

    if request.method == 'POST':

        if not ckboxs and not mode:
            errors['error_all'] = 'Выберите действие и заметку'

        elif not ckboxs:
            errors['error_ckboxs'] = "Выберите хотябы одину заметку"

        elif mode == "None":
            errors['error_mode'] = 'Выберите действия'

        elif mode == 'remove':
            for pk in ckboxs:
                message = get_object_or_404(Message, pk=pk)
                message.delete()
        else:
            for pk in ckboxs:
                message = get_object_or_404(Message, pk=pk)
                message.status = mode
                message.save()

    return render(request, 'Page/note_page.html', {'messages': messages, "errors": errors})


@login_required()
def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.save()
            return redirect(reverse('notes'))
    else:
        form = MessageForm()

        return render(request, 'forms/note_add.html', {'form': form})


class RegisterFormView(TemplateView):
    template_name = 'forms/register.html'

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            user = User.objects.filter(username=username)
            user_email = User.objects.filter(email=email)

            if user:
                context['username_error'] = 'Пользователь с таким логином уже существует'

            elif user_email:
                context['email_error'] = 'Пользователь с таким Email уже существует'

            elif password != password2:
                context['password2_error'] = 'Пароль не совпадает'

            else:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.save()
                return redirect(reverse('home'))
        return render(request, self.template_name, context)

# def user():
#     user1 = User(username=adi, email=,password=)

# Получение значения сессии при помощи ключа(то есть, 'my_car').
# Если такого ключа нет, то возникнет ошибка KeyError
# my_car = request.session['my_car']

# Получение значения сессии. Если значения не существует,
# то вернется значение по умолчанию ('mini')
# my_car = request.session.get('my_car', 'mini')

# Передача значения в сессию
# request.session['my_car'] = 'mini'

# Удаление значения из сессии
# del request.session['my_car']