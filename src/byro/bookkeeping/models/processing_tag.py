from decimal import Decimal

from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils.decorators import classproperty
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


class ProcessingTag(models.Model):
    token = models.CharField(max_length=300, null=False, unique=True)

    account = models.ForeignKey(
        to="bookkeeping.Account",
        #related_name="debits",
        on_delete=models.CASCADE,
        null=True
    )

    member = models.ForeignKey(
        to="members.Member",
        #related_name="bookings",
        on_delete=models.CASCADE,
        null=True,
    )

    check_memo = models.BooleanField(default=True)
    check_other = models.BooleanField(default=False)

    def __str__(self):
        return self.token

    def check_match_transaction(self, t):
        if self.check_memo:
            if self.token.lower() in t.memo.lower():
                return True

        if self.check_other:
            raise NotImplemented

        return False

