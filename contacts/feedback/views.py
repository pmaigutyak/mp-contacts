
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import FormView
from django.template.loader import render_to_string

from contacts.feedback.forms import FeedbackForm
from contacts.lib import send_notification


class CreateFeedbackView(FormView):

    form_class = FeedbackForm

    def dispatch(self, request, *args, **kwargs):
        self.is_modal = request.GET.get('modal', False)
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):

        user = self.request.user

        if user.is_authenticated:

            mobile = user.profile.mobile if hasattr(user, 'profile') else ''

            return {
                'name': user.get_full_name(),
                'email': user.email,
                'mobile': mobile
            }

        return self.initial

    def get_template_names(self):

        if self.is_modal:
            return ['feedback/modal.html']

        return ['feedback/view.html']

    def form_valid(self, form):

        obj = form.save(commit=False)

        if self.request.user.is_authenticated:
            obj.user = self.request.user

        obj.save()

        send_notification(
            obj,
            subject_template='feedback/email/subject.txt',
            email_template='feedback/email/message.html',
            sms_template='feedback/sms.txt')

        message = render_to_string(
            'feedback/success_message.html', {'object': obj})

        return HttpResponse(message)

    def form_invalid(self, form):

        if self.is_modal:
            template_name = 'feedback/form.html'
        else:
            template_name = 'feedback/view.html'

        return render(self.request, template_name, {'form': form}, status=403)
