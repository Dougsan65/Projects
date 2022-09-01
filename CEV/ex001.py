x = input("Digite algo: ")

print(f'{x}, é do tipo', type(x))
print(f'{x}, é do tipo alfanumerico? {x.isalnum()}')
print(f'{x}, é do tipo alfabetico? {x.isalpha()}')
print(f'{x}, esta em minusculo? {x.islower()}')
print(f'{x}, esta em maiusculo? {x.isupper()}')
print(f'{x}, é do tipo numerico? {x.isnumeric()}')