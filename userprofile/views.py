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

  def __init__(self, group_name=None, user_id=None, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    self.group_name = group_name
    self.user_id = user_id

  class Meta:
    model = UserProfile
    fields = ['username','password', 'first_name', 'last_name', 'email', 'gender',
              'country', 'phone']

  def save(self, commit=True):
    if self.user_id:
      # In case it will be passed somehow.
      del self.cleaned_data['password']
      user = UserProfile(pk=self.user_id, **self.cleaned_data)
    else:
      user = UserProfile.objects.create_user(**self.cleaned_data)
      user.groups.add(Group.objects.get(name=self.group_name))
    user.save()
    return user


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
    kwargs['user_id'] = self.user_id()
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
  success_url = reverse_lazy('task_list')
  template_name = 'delete.html'
  owner_required = True

  def user_id(self):
    return self.get_object().pk


class DetailProfileWriterView(DetailProfileView):
  group_name = co.WRITER_GROUP


class CreateProfileWriterView(CreateProfileView):
  group_name = co.WRITER_GROUP


class UpdateProfileWriterView(UpdateProfileView):
  group_name = co.WRITER_GROUP


class DetailProfileCustomerView(DetailProfileView):
  group_name = co.CUSTOMER_GROUP


class CreateProfileCustomerView(CreateProfileView):
  group_name = co.CUSTOMER_GROUP


class UpdateProfileCustomerView(UpdateProfileView):
  group_name = co.CUSTOMER_GROUP


