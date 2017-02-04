from django.db import models

SOURCE_FACEBOOK = 1
SOURCE_TELEGRAM = 2


class BotUser(models.Model):
    source = models.PositiveSmallIntegerField(choices=[
        (SOURCE_FACEBOOK, 'Facebook'),
        (SOURCE_TELEGRAM, 'Telegram'),
    ])
    chat_user_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=150, default='')
    last_name = models.CharField(max_length=150, default='')
    timezone = models.SmallIntegerField(null=True)
    locale = models.CharField(max_length=10, default='')
    requests_count = models.BigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('source', 'chat_user_id')


class BotUserRequestStats(models.Model):
    bot_user = models.ForeignKey('sitp_bot.BotUser')
    requests_count = models.BigIntegerField(default=0)
    day = models.DateField()

    class Meta:
        unique_together = ('bot_user', 'day')


class MessageStats(models.Model):
    source = models.PositiveSmallIntegerField(choices=[
        (SOURCE_FACEBOOK, 'Facebook'),
        (SOURCE_TELEGRAM, 'Telegram'),
    ])
    phrase = models.CharField(max_length=500)
    requests_count = models.BigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('source', 'phrase')
