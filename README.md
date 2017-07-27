# MP-Contacts

Django contacts app.

### Installation

Install with pip:

```sh
$ pip install django-mp-contacts
```

Add contacts to urls.py:

```
urlpatterns += i18n_patterns(
    
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    
)
```

Add contacts to settings.py:
```
INSTALLED_APPS = [
    'contacts',
    'captcha',
]

NOCAPTCHA = True
RECAPTCHA_PUBLIC_KEY = '***************************************'
RECAPTCHA_PRIVATE_KEY = '*****************************************'
```

### JS Modal:

Add 'contacts/contacts.js' to js files

HTML:
```
<button class="btn btn-primary scroll" data-role="feedback-btn">
    <i class="fa fa-envelope"></i>
</button>
```

Javascript:
```
(function ($) {
    $('[data-role=feedback-btn]').contactMessageModal({
        url: '{% url 'contacts:feedback' %}'
    }).tooltip();
})(jQuery);
```

Run migrations:
```
$ python manage.py migrate
```

### Requirements

App require this packages:

* django-recaptcha
* django-widget-tweaks
