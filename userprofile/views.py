from django import forms
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView

from general.views import BaseView
from django.core.urlresolvers import reverse_lazy

from userprofile.models import UserProfile

import constants as co


class ProfileForm(forms.ModelForm):

  def __init__(self, group_name=None, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    self.group_name = group_name

  class Meta:
    model = UserProfile
    fields = ['username', 'first_name', 'last_name', 'email', 'photo']

  def save(self, commit=True):
    instance = super(ProfileForm, self).save(commit=commit)
    instance.groups.add(Group.objects.get(name=self.group_name))
    instance.save()
    return instance


class CreateProfileView(BaseView, CreateView):
  module_name = 'userprofile'
  form_class = ProfileForm
  queryset = UserProfile.objects.all()
  template_name = 'edit.html'
  group_name = ''

  def get_form_kwargs(self):
    kwargs = super(CreateProfileView, self).get_form_kwargs()
    kwargs['group_name'] = self.group_name
    return kwargs


class UpdateProfileView(BaseView, UpdateView):
  template_name = 'edit.html'
  form_class = ProfileForm
  queryset = UserProfile.objects.all()
  module_name = 'userprofile'
  group_name = ''
  owner_required = True

  def get_form_kwargs(self):
    kwargs = super(UpdateProfileView, self).get_form_kwargs()
    kwargs['group_name'] = self.group_name
    return kwargs

  def user_id(self):
    return self.get_object().pk


class DetailProfileView(BaseView, DetailView):
  module_name = 'userprofile'
  queryset = UserProfile.objects.all()
  template_name = 'detail.html'
  group_name = ''


class RemoveProfileView(BaseView, DeleteView):
  module_name = 'userprofile'
  queryset = UserProfile.objects.all()
  success_url = reverse_lazy('all_tasks')
  template_name = 'delete.html'
  owner_required = True

  def user_id(self):
    return self.get_object().pk


class DetailProfileEmployerView(DetailProfileView):
  group_name = co.EMPLOYER_GROUP_NAME


class CreateProfileEmployerView(CreateProfileView):
  group_name = co.EMPLOYER_GROUP_NAME


class UpdateProfileEmployerView(UpdateProfileView):
  group_name = co.EMPLOYER_GROUP_NAME
