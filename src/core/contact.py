from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email:*'}), required=True)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Телефон:*', 'class': 'phone-mask'}),
                                   required=True)
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Комментарий (необязательно)'}),
                              required=False)
    additional_info = forms.CharField(widget=forms.HiddenInput(), required=False)
    check = forms.BooleanField(required=True, widget=forms.CheckboxInput(attrs={'checked': 'checked'}))


def contact_form(request):
    form = ContactForm()
    return {'contact_form': form}
