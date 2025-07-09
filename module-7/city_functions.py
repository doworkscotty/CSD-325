#Scott Anderson Module 7.2 Assignment


def city_country(city, country, population=None, language=None):
  result = f"{city.title()}, {country.title()}"
  if population:
      result += f" - population {population}"
  if language:
      result += f", {language.title()}"
  return result

# Final function calls
print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan", 14000000))
print(city_country("berlin", "germany", 3769000, "german"))




