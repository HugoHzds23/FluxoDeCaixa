from django import forms

class loginforms(forms.Form):
        nome_login = forms.CharField(
                label= "Nome de Login",
                required=True,
                max_length= 100,
                widget=forms.TextInput(
                        attrs = {
                                "class": "form-control",
                                "placeholder": "Digite seu Login"
                        }
                )
        )
        senha = forms.CharField(
                label= "Senha",
                required=True,
                max_length= 50,
                widget=forms.PasswordInput(
                       attrs = {
                                "class": "form-control",
                                "placeholder": "Digite sua Senha"
                        }
                )
        )

class cadastroforms(forms.Form):
        nome_cadastro = forms.CharField(
                label= "Nome",
                required=True,
                max_length= 100,
                widget=forms.TextInput(
                        attrs = {
                                "class": "form-control",
                                "placeholder": "Digite seu nome"
                        }
                )
        )

        email = forms.EmailField(
                label= "Email",
                required=True,
                max_length= 100,
                widget=forms.EmailInput(
                        attrs= {
                                 "class": "form-control",
                                 "placeholder": "Digite seu Email"
                                }
                        )
        )


        senha_1 = forms.CharField(
                label= "Senha",
                required=True,
                max_length= 50,
                widget=forms.PasswordInput(
                       attrs = {
                                "class": "form-control",
                                "placeholder": "Digite sua Senha"
                        }
                )
        )

        senha_2 = forms.CharField(
                label= "Confirmação Senha",
                required=True,
                max_length= 50,
                widget=forms.PasswordInput(
                       attrs = {
                                "class": "form-control",
                                "placeholder": "Digite sua Senha novamente"
                        }
                )
        )