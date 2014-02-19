from django import forms
from django.contrib.auth.models import Group
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic import DetailView

from general.views import BaseView, owner_required
from django.core.urlresolvers import reverse

from userprofile.models import UserProfile
from django.contrib.auth.models import User

import constants as co


class NewProfileForm(forms.Form):
  username = forms.CharField()
  first_name = forms.CharField()
  last_name = forms.CharField()
  email = forms.EmailField()
  photo = forms.FileField()

  def __init__(self, instance=None, request=None, groupname=None,
               *args, **kwargs):
    super(NewProfileForm, self).__init__(*args, **kwargs)
    self.request = request
    self.instance = instance
    self.groupname = groupname

  class Meta:
    fields = ['username', 'first_name', 'last_name', 'email', 'photo']

  def save(self):
    cl = self.cleaned_data
    user = User(username=cl.get('username'), first_name=cl.get('first_name'),
                last_name=cl.get('last_name'), email=cl.get('email'))
    user.save()
    user.groups.add(Group.objects.get(name=self.groupname))
    user.save()
    profile = UserProfile(user=user, photo=cl.get('photo'))
    profile.save()
    return profile


class CreateProfileEmployerView(BaseView, CreateView):
  module_name = 'userprofile'
  form_class = NewProfileForm
  queryset = UserProfile.objects.all()
  template_name = 'edit.html'

  def get_form_kwargs(self):
    kwargs = super(CreateProfileEmployerView, self).get_form_kwargs()
    kwargs['request'] = self.request
    kwargs['groupname'] = co.EMPLOYER_GROUP_NAME
    return kwargs

  def get_context_data(self, **kwargs):
    context = super(CreateProfileEmployerView, self).get_context_data(**kwargs)
    context.update(self.settings)
    return context


class DetailProfileEmployerView(BaseView, DetailView):
  module_name = 'userprofile'
  queryset = UserProfile.objects.all()
  template_name = 'detail.html'

  def get_context_data(self, **kwargs):
    context = super(DetailProfileEmployerView, self).get_context_data(**kwargs)
    context.update(self.settings)
    return context

