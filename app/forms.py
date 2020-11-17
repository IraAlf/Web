from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(max_length=18, min_length=5, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, max_length=40, label='Пароль')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=20, label='Логин', min_length=5,
                               help_text='Логин более 5 символов и не длиннее 20.')
    email = forms.CharField(label='E-mail')
    nick_name = forms.CharField(max_length=20, label='Никнейм', min_length=5,
                                help_text='Никнейм более 5 символов и не длиннее 20.')
    password = forms.CharField(widget=forms.PasswordInput, max_length=40, min_length=10, label='Пароль',
                               help_text='Придумайте надежный пароль не менее 10 символов')
    repeat_password = forms.CharField(widget=forms.PasswordInput, max_length=40, min_length=10, label='Повторите пароль')
    avatar = forms.ImageField(label='Аватар', required=False, help_text='Прикрепите фото, чтобы друзьям было легче узнать Вас.')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)


class SettingsForm(forms.Form):
    username = forms.CharField(max_length=20, label='Логин',
                               help_text='Логин более 5 символов и не длиннее 20.')
    email = forms.CharField(label='E-mail')
    nick_name = forms.CharField(max_length=20, label='Никнейм',
                                help_text='Никнейм более 5 символов и не длиннее 20.')
    avatar = forms.ImageField(widget=forms.FileInput, label='Аватар', required=False, help_text='Прикрепите фото, чтобы друзьям было легче узнать Вас.')

    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)


class AskForm(forms.Form):
    title = forms.CharField(label='Заголовок')
    text = forms.CharField(widget=forms.Textarea, label='Текст')
    tags = forms.CharField(label='Теги')

    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)
