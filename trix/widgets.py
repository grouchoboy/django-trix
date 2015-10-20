from __future__ import unicode_literals
from django import forms
from django.contrib.admin import widgets as admin_widgets


class TrixEditor(forms.Textarea):

    def render(self, name, value, attrs=None):

        if attrs is None:
            attrs = {}
        attrs.update({'style': 'visibility: hidden; position: absolute;'})

        params = {
            'input': attrs.get('id') or '{}_id'.format(name),
            'class': 'trix-content',
        }
        param_str = ' '.join('{}="{}"'.format(k, v) for k, v in params.items())

        html = super(TrixEditor, self).render(name, value, attrs)
        html += '<p><trix-editor {}></trix-editor></p>'.format(param_str)
        return html

    class Media:
        css = {'all': ('trix/trix.css',)}
        js = ('trix/trix.js', 'trix/trix-django.js')