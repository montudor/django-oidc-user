from django.db import models
from django.utils import timezone
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
import re
import pytz

from django_oidc_user.timezones import TIMEZONES
from django_oidc_user.locales import LOCALES

class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(_('username'), max_length = 20, unique = True,
		help_text=_('Required. 20 characters or fewer. Letters, numbers and '
					'underscore characters'),
		validators=[
			validators.RegexValidator(re.compile('^[\w]+$'), 
			_('Enter a valid username.'), 'invalid username')
		])
	first_name = models.CharField(_('first name'), max_length = 254, blank = True)
	last_name = models.CharField(_('last name'), max_length = 30, blank = True)
	
	email = models.EmailField(_('email address'), max_length = 254, unique = True, null = True)
	email_verified = models.BooleanField(_('email verified'), default = False)

	phone = models.CharField(_('phone number'), validators = [validators.RegexValidator(regex=r'^\+?1?\d{9,15}$', message="The number must be entered in the format: '+999999999' with up to 15 digits.")], max_length = 16, blank = True)
	phone_verified = models.BooleanField(_('phone verified'), default = False)

	is_staff = models.BooleanField(_('staff status'), default = False,
		help_text=_('Designates whether the user can log into the admin '
					'site.'))
	is_active = models.BooleanField(_('active'), default = True,
		help_text=_('Designates whether this user should be treated as '
					'active. Unselect this instead of deleting accounts.'))
	is_verified = models.BooleanField(_('verified'), default = False)
	date_joined = models.DateTimeField(_('date joined'), default = timezone.now)
	updated_at = models.DateTimeField(_('updated at'), default = timezone.now)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['first_name', 'email']
	
	@property
	def name(self):
		return self.get_full_name()

	def get_full_name(self):
		if self.last_name.lstrip(" ") == "":
			return self.first_name
		return "%s %s" % (self.first_name, self.last_name)

	def get_short_name(self):
		return self.first_name

	website = models.CharField(_('website'), max_length = 254,
		validators = [
			validators.URLValidator()
		])

	zoneinfo = models.CharField(_('time zone'), max_length = 254, choices = TIMEZONES, default = "Europe/London")
	locale = models.CharField(_('locale'), max_length = 254, choices = LOCALES, default = "en-US")