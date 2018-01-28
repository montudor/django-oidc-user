def userinfo(claims, user):
	claims['name'] = '{0} {1}'.format(user.first_name, user.last_name)
	claims['given_name'] = user.first_name
	claims['family_name'] = user.last_name
	claims['preferred_username'] = user.username
	claims['website'] = user.website
	claims['zoneinfo'] = user.zoneinfo
	claims['locale'] = user.locale

	claims['email'] = user.email
	claims['email_verified'] = user.email_verified

	claims['phone_number'] = user.phone
	claims['phone_number_verified'] = user.phone_verified

	return claims
