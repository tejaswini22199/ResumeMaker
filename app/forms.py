from django import forms
from . models import extrafield,educ,contactdetails,workexp,skills


class Extrafieldform(forms.ModelForm):
	class Meta:
		model = extrafield
		fields = ['field_name','explanation']
		widgets ={
			'field_name' : forms.TextInput(attrs={'class':'form-control'}),
			'explanation' : forms.Textarea(attrs={'class':'form-control'})
		}

			
class Educationdetails(forms.ModelForm):
	class Meta:
		model = educ
		fields =['school_name','school_location','Degree','CGPA','Field_of_Study','Expected_year_of_grad']
		widgets = {
		'school_name' : forms.TextInput(attrs={'class':'form-control'}),
		'school_location' : forms.TextInput(attrs={'class':'form-control'}),
		'Degree' : forms.TextInput(attrs={'class':'form-control'}),
		'CGPA' : forms.TextInput(attrs={'class':'form-control'}),
		'Field_of_Study' : forms.TextInput(attrs={'class':'form-control'}),
		'Expected_year_of_grad' : forms.TextInput(attrs={'class':'form-control'}),
	}
		
		
class contactdetailsform(forms.ModelForm):
	class Meta:
		model = contactdetails
		fields ='__all__'
	


class jobform(forms.ModelForm):
	class Meta:
		model = workexp
		fields ='__all__'
		widgets = {
		'author' : forms.TextInput(attrs={'class':'form-control'}),
		'resume_name' : forms.TextInput(attrs={'class':'form-control'}),
		'job_title' : forms.TextInput(attrs={'class':'form-control'}),
		'employer' : forms.TextInput(attrs={'class':'form-control'}),
		'city' : forms.TextInput(attrs={'class':'form-control'}),
		'state' : forms.TextInput(attrs={'class':'form-control'}),
		'jobdesc' : forms.TextInput(attrs={'class':'form-control'}),
	}


 #THE BELOW CODE IS ADDED BY SIRI.
class skilldetails(forms.ModelForm):
	class Meta:
		model=skills
		fields=['skill']
		widgets = {
			'skill' : forms.TextInput(attrs={'class':'form-control'})
		}