from django import forms
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView

from general.views import BaseView
from django.core.urlresolvers import reverse_lazy

from userprofile.models import UserProfile

import constants as co


class ProfileForm(forms.ModelForm):
  def __init__(self, group_name=None, user_id=None, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    self.group_name = group_name
    self.user_id = user_id
    if user_id:
      self.fields['password'].required = False
      self.fields['username'].required = False

  class Meta:
    model = UserProfile
    fields = ['username', 'password', 'first_name', 'last_name', 'email', 'gender',
              'country', 'phone']
  
  def save(self, commit=True):
    if self.user_id:
      user = UserProfile.objects.get(pk=self.user_id)
      user.first_name=self.cleaned_data['first_name']
      user.last_name=self.cleaned_data['last_name']
      user.email=self.cleaned_data['email']
      user.gender=self.cleaned_data['gender']
      user.country=self.cleaned_data['country']
      user.phone=self.cleaned_data['phone']
    else:
      user = UserProfile.objects.create_user(**self.cleaned_data)
      user.groups.add(Group.objects.get(name=self.group_name))
    user.save()
    return user


class CreateProfileView(BaseView, CreateView):
  module_name = ''
  form_class = ProfileForm
  queryset = UserProfile.objects.all()
  template_name = 'userprofile/edit.html'
  group_name = ''

  def get_form_kwargs(self):
    kwargs = super(CreateProfileView, self).get_form_kwargs()
    kwargs['group_name'] = self.group_name
    return kwargs


class ListProfileView(BaseView, TemplateView):
  module_name = ''
  queryset = UserProfile.objects.all()
  template_name = 'userprofile/index.html'


class UpdateProfileView(BaseView, UpdateView):
  template_name = 'userprofile/edit.html'
  form_class = ProfileForm
  queryset = UserProfile.objects.all()
  group_name = ''
  owner_required = True

  def get_form_kwargs(self):
    kwargs = super(UpdateProfileView, self).get_form_kwargs()
    kwargs['group_name'] = self.group_name
    kwargs['user_id'] = self.user_id()
    return kwargs

  def user_id(self):
    return self.get_object().pk


class RemoveProfileView(BaseView, DeleteView):
  queryset = UserProfile.objects.all()
  success_url = reverse_lazy('task_list')
  template_name = 'userprofile/delete.html'
  owner_required = True

  def user_id(self):
    return self.get_object().pk

