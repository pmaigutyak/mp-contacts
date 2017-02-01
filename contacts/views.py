
from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from contacts.forms import FeedbackForm, ReturnCallForm
from contacts.lib import (
    send_new_feedback_notification, send_new_return_call_notification
)


def index(request):

    data = request.POST
    user = request.user

    feedback_form_params = {'data': data if data.get('feedback') else None}
    return_call_form_params = {'data': data if data.get('call') else None}

    if user.is_authenticated():
        mobile = user.profile.mobile if hasattr(user, 'profile') else ''

        feedback_form_params['initial'] = {
            'name': user.get_full_name(),
            'email': user.email,
            'mobile': mobile
        }
        return_call_form_params['initial'] = {
            'mobile': mobile
        }

    feedback_form = FeedbackForm(**feedback_form_params)
    return_call_form = ReturnCallForm(**return_call_form_params)

    if data and data.get('feedback'):

        if feedback_form.is_valid():

            feedback = feedback_form.save(commit=False)

            if user.is_authenticated():
                feedback.user = user

            feedback.save()

            messages.success(request, _('Message was successfully sent'))

            send_new_feedback_notification(feedback)

            return redirect(request.path)

        else:
            messages.error(
                request, _('Please fix the errors in the feedback form'))

    if data and data.get('call'):

        if return_call_form.is_valid():

            return_call = return_call_form.save(commit=False)

            if user.is_authenticated():
                return_call.user = user

            return_call.save()

            messages.success(request, _('Call request was successfully sent'))

            send_new_return_call_notification(return_call)

            return redirect(request.path)

        else:
            messages.error(
                request, _('Please fix the errors in the return call form'))

    context = {
        'feedback_form': feedback_form,
        'return_call_form': return_call_form
    }

    return render(request, 'contacts/index.html', context)
