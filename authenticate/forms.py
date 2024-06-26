from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .data_validator import *


class UserSignInForm(forms.Form):
	email = forms.EmailField(max_length=254)
	password = forms.CharField(max_length=100)
 

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if ' ' in email :
			raise forms.ValidationError("Spaces not allowed in email")
		if not validate_email(email):
			raise forms.ValidationError("Email in Invalid")
		new_email = email.split('@')
		if len(new_email[0]) < 3:
			raise forms.ValidationError("Email length is Invalid") 
		exist = User.objects.filter(email=email).exists()
		if not exist:
			raise forms.ValidationError("Email is not registerd, try to Create Account")
		return email
	
	def clean_password(self):
		password = self.cleaned_data.get('password')
		email = self.cleaned_data.get('email')
		pattern = r"[~`+=\-/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, password)
		if matches:
			raise forms.ValidationError("Password Format is not allowed")
		return password


class UserSignUpForm(forms.Form):
	username = forms.CharField(max_length=150)
	email = forms.CharField(max_length=150)
	first_name = forms.CharField(max_length=150)
	last_name = forms.CharField(max_length=150)
	idnumber  = forms.CharField(max_length=13)
	phone = forms.CharField(max_length=10)
	password = forms.CharField(max_length=128)


	def validate_names(self,name):
     
		pattern = r"[~`+!@#$%^&*()=\-/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, name)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		if len(name) < 3:
			raise forms.ValidationError(f"Name:{name} is too short")
		try:
			str(name)
		except Exception as e:
			raise forms.ValidationError(e)
		return name

	def clean_first_name(self):
		first_name = self.cleaned_data.get('first_name')
		return self.validate_names(first_name)

	def clean_last_name(self):
		last_name = self.cleaned_data.get('last_name')
		return self.validate_names(last_name)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		exist = User.objects.filter(username=username).exists()
		if exist:
			raise forms.ValidationError(f"Username:{username} is already taken")
		return self.validate_names(username)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if ' ' in email :
			raise forms.ValidationError("Spaces not allowed in email")
		if not validate_email(email):
			raise forms.ValidationError(f"Email: {email} in Invalid")
		new_email = email.split('@')
		if len(new_email[0]) < 3:
			raise forms.ValidationError("Email length is Invalid") 
		exist = User.objects.filter(email=email).exists()
		if exist:
			raise forms.ValidationError(f"Email: {email} is already taken")
		return email

	def clean_password(self):
		
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		first_name = self.cleaned_data.get('first_name') 
		# username = self.cleaned_data.get('username')
		
		
		pattern = r"[~`+=\-/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, password)

		if matches:
			
			raise forms.ValidationError("Password Format is not allowed")
		
		if len(password) < 6:
			raise forms.ValidationError("Password is too short")

		char = [char for char in password if char.isdigit()]
		if len(char) < 1:
			raise forms.ValidationError("Password must contain at least one Number")
		
		if first_name in password: #or username in password:
			raise forms.ValidationError("Password cannot contain username of first name")  
		return password

	def clean_phone(self):
		phone = self.cleaned_data.get('phone')
		exist = User.objects.filter(profile__phone=phone).exists()
		if exist:
			 raise forms.ValidationError("phone Number Already taken")
		
		if not validate_south_african_phone_number(phone):
			raise forms.ValidationError("Phone number is not a valid south african number")
		return phone

	def clean_idnumber(self):
		idnumber = self.cleaned_data.get('idnumber')
		validate = ValidateIdNumber(idnumber)
		is_valid = validate.validateSAID()
		exist = User.objects.filter(profile__idnumber=idnumber).exists()
		if exist:
			raise forms.ValidationError("Id Number Already taken")
			
		if not is_valid:
			raise forms.ValidationError("Provide ID Number is not a valid South African ID Number")
		return idnumber

class PersonalInformationForm(forms.Form):
	linkedin_profile = forms.CharField(max_length=225)
	personal_website = forms.CharField(max_length=225)
	job_title = forms.CharField(max_length=225) 
	current_employer =  forms.CharField(max_length=225)
	years_of_expreince = forms.CharField(max_length=6)
	industry = forms.CharField(max_length=225)
	carear_level = forms.CharField(max_length=20)
	desired_job = forms.CharField(max_length=225)
	job_location = forms.CharField(max_length=225)


	def validate_names(self,name):
     
		pattern = r"[~`+!@#$%^&*()=\-/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, name)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		if len(name) < 3:
			raise forms.ValidationError(f"Name:{name} is too short")
		try:
			str(name)
		except Exception as e:
			raise forms.ValidationError(e)
		return name

	def clean_linkedin_profile(self):
		linkedin_profile = self.cleaned_data.get('linkedin_profile')
		if linkedin_profile == "none":
			return linkedin_profile
		pattern = re.compile(r'^(https?:\/\/)?(www\.)?linkedin\.com\/(in|pub|company)\/[A-Za-z0-9_-]+\/?$')
		if not bool(pattern.match(Linkedin_profile)) :
		 	raise forms.ValidationError("linkedin url is invalid")
		return Linkedin_profile

	def clean_personal_website(self):
		personal_website = self.cleaned_data.get('personal_website')
		if personal_website == "none":
			return personal_website
		pattern = re.compile(r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\/[a-zA-Z0-9-]*)*\/?$')
		if not bool(pattern.match(url)):
			raise forms.ValidationError('your personal website url is invalid')
		return personal_website
 	
	def clean_job_title(self):
 		job_title = self.cleaned_data.get('job_title')
 		if job_title == "":
 			raise forms.ValidationError('Job Title cannot be empty ')
 		return self.validate_names(job_title)

	def clean_current_employer(self):
 		current_employer = self.cleaned_data.get('current_employer')
 		if current_employer == "":
 			return current_employer
 		return self.validate_names(current_employer)

	def clean_years_of_expreince(self):
 		years_of_expreince = self.cleaned_data.get('years_of_expreince')
 		if years_of_expreince == "":
 			raise forms.ValidationError("Years of expreince cannot be empty")
 		try:
 			int(years_of_expreince)
 			return str(years_of_expreince)
 		except Exception as e:
 			raise forms.ValidationError('years of expreince must be Numbers only')

	def clean_industry(self):
 		industry = self.cleaned_data.get('industry')
 		if industry == "":
 			raise forms.ValidationError("industry cannot be empty")
 		return self.validate_names(industry)

	def clean_carear_level(self):
 		carear_level = self.cleaned_data.get('carear_level')
 		if carear_level == "":
 			raise forms.ValidationError("carear_level cannot be empty")
 		return self.validate_names(carear_level)

	def clean_desired_Job(self):
 		desired_job = self.cleaned_data.get('desired_Job')
 		if desired_job == "":
 			return desired_job
 		return self.validate_names(desired_job)

	def clean_job_location(self):
 		job_location = self.cleaned_data.get('job_location')
 		if job_location == "":
 			return job_location
 		return self.validate_names(job_location)

class AddressInformationForm(forms.Form):

	street_address_line = forms.CharField(max_length=225)
	street_address_line1 = forms.CharField(max_length=225)
	city = forms.CharField(max_length=225)
	province = forms.CharField(max_length=225)
	postal_code = forms.CharField(max_length=6)

	def validate_names(self,name):
     
		pattern = r"[~`+!@#$%^&*()=\-/\*\\|}{\[\];'\?.,]"
		matches = re.findall(pattern, name)
		if matches:
			raise forms.ValidationError("No special characters allowed")
		if len(name) < 3:
			raise forms.ValidationError(f" Address :{name} is too short")
		return name

	def clean_street_address_line(self):
		street_address_line = self.cleaned_data.get('street_address_line')
		return self.validate_names(street_address_line)

	def clean_street_address_line1(self):
		street_address_line = self.cleaned_data.get('street_address_line')
		return self.validate_names(street_address_line)

	def clean_city(self):
		city = self.cleaned_data.get('city')
		return self.validate_names(city)

	def clean_province(self):
		province = self.cleaned_data.get('province')
		return self.validate_names(province)

	def clean_postal_code(self):
		postal_code = self.cleaned_data.get('postal_code')
		if len(postal_code) < 3 :
			raise forms.ValidationError("Postal code is too short")
		try:
			int(postal_code)
		except:
			raise forms.ValidationError("Postal code must integers")