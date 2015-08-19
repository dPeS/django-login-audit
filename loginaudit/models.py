from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.signals import user_login_failed


LOGIN_ACTION = 'I'
LOGOUT_ACTION = 'O'
FAIL_ACTION = 'F'

ACTION_TYPES = (
    (LOGIN_ACTION, 'Login'),
    (LOGOUT_ACTION, 'Logout'),
    (FAIL_ACTION, 'Fail'),
)


class UserAuthAction(models.Model):

    action_type = models.CharField(
        max_length=1,
        choices=ACTION_TYPES
    )

    user = models.ForeignKey(
        User,
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )


def user_in(sender, user, request, **kwargs):
    UserAuthAction.objects.create(
        user=user,
        action_type=LOGIN_ACTION
    )
user_logged_in.connect(user_in)


def user_out(sender, user, request, **kwargs):
    UserAuthAction.objects.create(
        user=user,
        action_type=LOGOUT_ACTION
    )
user_logged_out.connect(user_out)


def user_fail(sender, credentials, **kwargs):
    UserAuthAction.objects.create(
        action_type=FAIL_ACTION
    )
user_login_failed.connect(user_fail)
