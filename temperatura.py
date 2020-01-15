# """Programa para converter temperatura em Celsius para Farenheit"""

# def c2f(celsius):
#     '''Conversao de Celsius para Farenheint'''
#     return (9.0 / 5.0) * celsius + 32

# def exib_f(celsius):
#     '''imprime conversao de temperatura'''
#     print (celsius, "celsius =", c2f(celsius), 'Farenheit')

# # executa funcao para converter 40, 20 e -40 Celsius para o equivalente em Farenheit
# exib_f(40)
# exib_f(20)
# exib_f(-40)

temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")