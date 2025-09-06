def multiplication(num1 , num2):
    multiplica = num1 * num2
    if(multiplica < 100):
        print("the result is:",multiplica)
        return multiplica
    else:
        multiplica = num1 + num2
    print("the result is:",multiplica)
multiplication(20,3)
