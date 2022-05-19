class Robot:
    '''Представляет робота с именем.'''
    # Переменная класс, содержащаяся количество роботов
    population = 0

    def __init__(self, name):
        '''Инициализаци данных'''
        self.name = name
        print('(Инициализаци {0})'.format(self.name))

        Robot.population += 1

    def __del__(self):
        '''Я умираю'''
        print('{0} уничтожается!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов'.format(Robot.population))
    def sayHi(self):
        '''Приветствую робота.
        Да, они это могут'''
        print('Приветствую. Мои хозяева называют меня {0}.'.format((self.name)))
    def howMany():
        '''Выводит численность роботов'''
        print('У нас {0:d} роботов'.format(Robot.population))
    howMany = staticmethod(howMany)
droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C3-PO')
droid2.sayHi()
Robot.howMany()
print("\nЗдесь роботы могут проделать какую то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их")
del droid1
del droid2

Robot.howMany()