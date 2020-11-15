from django import forms
from django.contrib import messages
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, FormView, ListView

from byro.bookkeeping.models import ProcessingTag,Account
from byro.members.models import Member

class ProcessingTagForm(forms.ModelForm):
    class Meta:
        model = ProcessingTag
        fields = ["token", "account", "member", "check_memo", "check_other"]

    account = forms.ModelChoiceField(queryset=Account.objects.all(), required=False)
    member = forms.ModelChoiceField(queryset=Member.objects.all(), required=False)

class ProcessingTagListView(ListView):
    template_name = "office/processing_tag/list.html"
    context_object_name = "processing_tags"
    model = ProcessingTag

class ProcessingTagCreateView(FormView):
    template_name = "office/processing_tag/add.html"
    model = ProcessingTag
    form_class = ProcessingTagForm

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,
            _("The processing tag was added."),
        )
        self.form = form
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "office:finance.processing_tags.list"
        )

#