import pygal.maps.world as wd

def get_country_code(country_name):
	"""rreturn the two chart country code used in pygal according to the specified country"""
	for code,name in wd.COUNTRIES.items():
		if name==country_name:
			return code
	#if the specified country not found, return none
	
