from django import forms
from django.utils.translation import ugettext_lazy as _


class RestrictedFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop('content_types', None)

    def clean(self, *args, **kwargs):
        data = super(RestrictedFileField, self).clean(*args, **kwargs)
        try:
            if data.content_type not in self.content_types:
                raise forms.ValidationError(_('Формат файла не поддерживается.') % data.content_type)
        except AttributeError:
            pass

        return data


class UploadForm(forms.Form):
    file = forms.FileField(label='Файл')
    # file = RestrictedFileField(content_types=['text/csv'])
