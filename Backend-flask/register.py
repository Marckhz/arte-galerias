class RegistrationForm(form):
	username = Textfield('Username', [validators.length(min=4, max=20)])
	email = Textfield('Email Address', [validators.length(min=6, max=50)])
	password = PasswordField('New Password', [validators.length(min=8, max=50)
		validators.Required(),
		validators.Equalto('confirm', message = 'Passowrds must match')])
	confirm = PasswordField('Repeat Password')
	accept_tos = BooleanField('I accept')