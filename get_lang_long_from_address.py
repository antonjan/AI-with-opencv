import geocoder
address = "Ekbatan Town"
coordinates = geocoder.arcgis(address)
geo = geocoder.arcgis(address)
print(geo.latlng)
location = geocoder.arcgis([35.70959, 51.30901], method="reverse")
print(location)
