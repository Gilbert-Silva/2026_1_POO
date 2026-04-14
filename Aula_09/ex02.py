x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}
for item in x.items(): print(item)
for key, value in x.items(): print(key, value)

for key in x: print(key)

x = { "RN" : "Natal"}
y = x.copy()
z = { "PB" : "João Pessoa", "PE" : "Recife"}
y.update(z)
print(x)
print(y)
print(z)

