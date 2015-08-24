from django.db import models
from django.utils.translation import ugettext_lazy

from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.signals import user_login_failed


LOGIN_ACTION = 'I'
LOGOUT_ACTION = 'O'
FAIL_ACTION = 'F'

ACTION_TYPES = (
    (LOGIN_ACTION, ugettext_lazy('Login')),
    (LOGOUT_ACTION, ugettext_lazy('Logout')),
    (FAIL_ACTION, ugettext_lazy('Fail')),
)


class UserAuthAction(models.Model):

    action_type = models.CharField(
        ugettext_lazy("Action Type"),
        max_length=1,
        choices=ACTION_TYPES
    )

    user = models.ForeignKey(
        User,
        null=True,
        blank=True
    )

    performed = models.DateTimeField(
        ugettext_lazy("Performed"),
        auto_now_add=True
    )

    notes = models.TextField(
        ugettext_lazy("Notes"),
        null=True,
    )

    class Meta:
        verbose_name = ugettext_lazy("Action")
        verbose_name_plural = ugettext_lazy("Actions")


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
