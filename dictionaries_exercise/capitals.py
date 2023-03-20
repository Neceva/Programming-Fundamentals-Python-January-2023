countries = input().split(', ')
capitals = input().split(', ')
final_results = {countries[index]: capitals[index] for index in range(len(countries))}
for country, capital in final_results.items():
    print(f"{country} -> {capital}")
