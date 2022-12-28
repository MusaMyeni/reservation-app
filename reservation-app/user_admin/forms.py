from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm


class MyAuthenticationForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super(MyAuthenticationForm, self).__init__(*args, **kwargs)
    for _, field in self.fields.items():
            field.label = ""

    self.fields['username'].widget.attrs.update(
      {
        'class': 'bg-white rounded-lg font-light font-montserrat text-center focus:ring-0 h-14 w-full',
        'placeholder':'Username',
        'autocomplete': 'off'
      }
    )
    self.fields['password'].widget.attrs.update(
      {
        'class': 'bg-white rounded-lg font-light font-montserrat text-center focus:ring-0 h-14 my-4 mb-8 w-full',
        'placeholder':'Password',
      }
    )