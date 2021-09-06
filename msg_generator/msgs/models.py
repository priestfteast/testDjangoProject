from django.db import models


class MsgForm(models.Model):
    template_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    variables_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.template_text


class Message(models.Model):
    msgForm = models.ForeignKey(MsgForm, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=200)
    variables_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.message_text