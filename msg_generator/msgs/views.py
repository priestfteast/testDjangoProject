from django.forms import Form
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Message, MsgForm
from typing import List
import re


class IndexView(generic.ListView):
    template_name = 'msgs/index.html'
    context_object_name = 'latest_messages_list'

    def get_queryset(self):
        return Message.objects.order_by('-variables_quantity')


class DetailView(generic.DetailView):
    model = Message
    template_name = 'msgs/detail.html'


def new(request, msgform_id):
    msg_form = get_object_or_404(MsgForm, pk=msgform_id)
    arguments = get_arguments_from_pattern(msg_form.template_text)
    all_forms = MsgForm.objects.all()
    return render(request, 'msgs/new.html', {
            'msgForm': msg_form,
            'arguments': arguments,
            'all_forms': all_forms,
        })


def save_message(request):
    msg_form = MsgForm.objects.get(pk=request.POST.get('id'))
    arguments = get_arguments_from_pattern(msg_form.template_text)
    message = Message()
    message.msgForm = msg_form
    message.variables_quantity = len(arguments)
    list = []
    for argument in arguments:
        list.append(request.POST.get(argument))
    message.message_text = build_message(msg_form.template_text, list)
    print(message, '!!!')
    message.save()

    return HttpResponseRedirect(reverse('msgs:index'))
    # message.message_text = build_message(msg_form.template_text, )


def get_arguments_from_pattern(pattern: str) -> List[str]:
    result = []
    arguments = re.findall(r'\${\w+}', pattern)
    for argument in arguments:
        result.append(re.sub('[${}]', '', argument))
    return result


def build_message(pattern: str, arguments: List[str]) -> str:
    message = pattern
    for argument in arguments:
        message = re.sub('\${\w+}', argument, message, 1)
    return message