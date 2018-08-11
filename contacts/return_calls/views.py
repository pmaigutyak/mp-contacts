
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import FormView
from django.template.loader import render_to_string

from contacts.return_calls.forms import ReturnCallForm
from contacts.lib import send_notification


class CreateReturnCallView(FormView):

    form_class = ReturnCallForm

    def dispatch(self, request, *args, **kwargs):
        self.is_modal = request.GET.get('modal', False)
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):

        user = self.request.user

        if user.is_authenticated:
            mobile = user.profile.mobile if hasattr(user, 'profile') else ''
            return {'mobile': mobile}

        return self.initial

    def get_template_names(self):

        if self.is_modal:
            return ['return_calls/modal.html']

        return ['return_calls/view.html']

    def form_valid(self, form):

        obj = form.save(commit=False)

        if self.request.user.is_authenticated:
            obj.user = self.request.user

        obj.save()

        send_notification(
            obj,
            subject_template='return_calls/email/subject.txt',
            email_template='return_calls/email/message.html',
            sms_template='return_calls/sms.txt')

        message = render_to_string(
            'return_calls/success_message.html', {'object': obj})

        return HttpResponse(message)

    def form_invalid(self, form):

        if self.is_modal:
            template_name = 'return_calls/form.html'
        else:
            template_name = 'return_calls/view.html'

        return render(self.request, template_name, {'form': form}, status=403)
