from django import forms

# place form definition here

CHOICE = (
	('DB', 'DB'),
	('BATCH', 'BATCH'),
	('ONE', 'ONE'),
	)

CHOICE2 = (
	('DB', 'DB'),
	('API', 'API'),
	)


class TestModuleForm(forms.Form):
    insertnumber = forms.CharField(label="insertnumber", max_length=100)
    choice = forms.ChoiceField(choices = CHOICE, initial='DB', label="choice")


class DisplayModuleForm(forms.Form):
    choice = forms.ChoiceField(choices = CHOICE2, initial='DB', label="choice")