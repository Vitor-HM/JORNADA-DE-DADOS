
name = input("digite seu nome:  ")

salary = float(input("digite se salario:  "))

bonus = float(input("digite o valor do bonus recebido:  "))

new_salary = salary * (1 + bonus / 100)

print(f"O usuario {name} com salario de {salary} recebeu um aumento de {bonus}% e seu salario foi para {new_salary}")

