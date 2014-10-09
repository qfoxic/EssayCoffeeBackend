from django import forms
from django.contrib.auth.models import Group
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Count

from general.views import BaseView
from general.models import Task
from django.core.urlresolvers import reverse_lazy

from userprofile.models import UserProfile

import constants as co


class ProfileForm(forms.ModelForm):
  def __init__(self, group_name=None, user_id=None, request=None, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    self.group_name = group_name
    self.user_id = user_id
    self.request = request
    if user_id:
      self.fields['password'].required = False
      self.fields['username'].required = False

  class Meta:
    model = UserProfile
    fields = ['username', 'password', 'first_name', 'last_name', 'email', 'gender',
              'country', 'phone', 'site']

  def clean_site(self):
    """Specifies default Host parameter."""
    return self.request.get_host()
  
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
    kwargs['user_id'] = None
    kwargs['request'] = self.request
    return kwargs


class ListProfileView(BaseView, ListView):
  queryset = UserProfile.objects.all()
  template_name = 'userprofile/index.html'

  def get_context_data(self, **kwargs):
    context = super(ListProfileView, self).get_context_data(**kwargs)
    tasks_per_user = dict(Task.objects.all().values('owner').annotate(
                          tasks=Count('owner')).values_list('owner', 'tasks'))
    # Count of user's tasks.
    context['user_tasks'] = tasks_per_user
    return context


class DetailProfileView(BaseView, DetailView):
  template_name = 'userprofile/detail.html' 
  queryset = UserProfile.objects.all()

  def user_id(self):
    return self.get_object().pk


class UpdateProfileView(BaseView, UpdateView):
  template_name = 'userprofile/edit.html'
  form_class = ProfileForm
  queryset = UserProfile.objects.all()
  group_name = ''

  def get_form_kwargs(self):
    kwargs = super(UpdateProfileView, self).get_form_kwargs()
    kwargs['group_name'] = self.group_name
    kwargs['user_id'] = self.user_id()
    kwargs['request'] = self.request
    return kwargs

  def user_id(self):
    return self.get_object().pk


class RemoveProfileView(BaseView, DeleteView):
  queryset = UserProfile.objects.all()
  template_name = 'userprofile/delete.html'

  def get_success_url(self):
    group = self.object.get_group()
    if group == co.ADMIN_GROUP:
      return reverse_lazy('admins')
    elif group == co.EDITOR_GROUP:
      return reverse_lazy('editors')
    elif group == co.WRITER_GROUP:
      return reverse_lazy('writers')
    else:
      return reverse_lazy('customers')

  def form_invalid(self, form):
    messages.add_message(self.request, messages.ERROR, str(form.errors))
    return HttpResponseRedirect(self.get_success_url())

  def user_id(self):
    return self.get_object().pk

