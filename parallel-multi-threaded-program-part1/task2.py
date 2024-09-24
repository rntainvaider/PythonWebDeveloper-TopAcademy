from random import randint
from threading import Thread
import time

class Task:
    def __init__(self):
        self.rand_numbers = list()
        self.prime_numbers = list()

    def fill_with_random_numbers(self, name_file: str):
        with open(name_file, 'w+') as file:
            for _ in range(10):
                ran_num = randint(1, 10)
                file.write(f"{str(ran_num)}\n")
                self.rand_numbers.append(ran_num)
                print(f"Заполняем файл случайными числами - {ran_num}")
                time.sleep(1)

        print(f"Сформированный список {self.rand_numbers}")

    def get_prime_numbers(self):      
        for item in self.rand_numbers:
            if int(item) > 0:
                k = 0
                for i in range(1, item + 1):
                    if item % i == 0:
                        k += 1
                if k == 2:
                    self.prime_numbers.append(i)

        with open("prime_numbers.txt", 'w') as file:
            for item in self.prime_numbers:
                file.write(f"{str(item)}\n")

        print(f"Все простые числа - {self.prime_numbers}")       

    def get_factorial_numbers(self):
        ...


name_file = input("Введите название файла с расширением\n")

task = Task()

t1 = Thread(target=task.fill_with_random_numbers(name_file))
t2 = Thread(target=task.get_prime_numbers)

t1.start()
t1.join()

t2.start()




 # def get_prime_numbers(self):
    #     with open(name_file, 'r') as file:
    #         for item in file:
    #             if int(item) > 0:
    #                 k = 0
    #                 for i in range(1, int(item) + 1):
    #                     if int(item) % i == 0:
    #                         k += 1
    #                 if k == 2:
    #                     self.prime_numbers.append(i)

    #     with open("prime_numbers.txt", 'w') as file:
    #         for item in self.prime_numbers:
    #             file.write(f"{str(item)}\n")

    #     print(f"Все простые числа - {self.prime_numbers}")