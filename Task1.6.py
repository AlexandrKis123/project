#6. Спортсмен занимается ежедневными пробежками. В первый день его результат
#составил a километров. Каждый день спортсмен
#увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня,
#на который общий результат спортсмена составить не менее b километров.
#Программа должна принимать значения параметров a и b и
#выводить одно натуральное число — номер дня.

sportsman = float(input('Введите сколько пробежали км: '))
end_result = float(input('Введите желаемый результат км: '))
answer = 1
while sportsman <= end_result:
    print(f"В {answer} день : {sportsman:.02f}")
    sportsman = sportsman + (sportsman * 0.1)
    answer += 1
    print(f"В {answer} день : {sportsman:.02f}")
    print(f"Бегун должен бегать дней: , {answer}")
