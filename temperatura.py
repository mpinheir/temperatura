
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




def menu():
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        pick = int(input("Enter a choice: "))
        return pick
def toCelsius(f):
        return int((f - 32) * 5.0 / 9.0)
def tofahrenheit(c):
        return int((9.0 / 5.0) * c + 32)
def main():
        choice = menu()
        
        while choice != 3:
                if choice == 1:
                        #convert C to F
                        c = eval(input("Enter degrees Celsius: "))
                        print(str(c) + "C= " + str(toFahrenheit(c)) + "F")
                elif choice == 2:
                        #convert F to C
                        f = eval(input("Enter degrees Fahrenheit: "))
                        print(str(f) + "F = " + str(toCelsius(f)) + "C")
                else:
                        print("Invalid entry")
                choice = menu()
main()

# """Rotinas de conversao de temperatura"""

# def c2f(celsius):
#     '''Conversao de Celsius para Farenheint'''
#     return (9.0 / 5.0) * celsius + 32

