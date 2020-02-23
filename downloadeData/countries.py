import pygal.maps.world as wd
for country_code in sorted(wd.COUNTRIES.keys()):
	print(country_code,wd.COUNTRIES[country_code])
