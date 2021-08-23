import math
import os


class scientific_calculator():
    def sqrt(self, num):
        print(math.sqrt(float(num)))
        return math.sqrt(float(num))


class base_calculator():
    def __init__(self, obj=None):
        self.obj = obj

    def __getattribute__(self, name):
        obj = object.__getattribute__(self, 'obj')
        try:
            return object.__getattribute__(self, name)
        except:
            return object.__getattribute__(obj, name)

    def add(self, *args):
        print(sum([float(_) for _ in args if _]))


def help_message():
    return "usage fun *args\t case: add 1 2 3"


def main():
    full_calculator = base_calculator(scientific_calculator())
    print('[ python3 calculator ]')
    title = '\t'.join(['[a]dd', '[s]qrt', '[q]uit', '[h]elp'])
    print(title)
    while True:
        want = input('>')
        os.system('clear')
        fun, args = want.split(' ')[0], want.split(' ')[1:]
        if "add" == fun.lower():
            full_calculator.add(*args)
        elif "sqrt" == fun.lower():
            full_calculator.sqrt(args[0])
        elif 'quit' == fun.lower():
            os.system('clear')
            break
        else:
            print(help_message())
        print(title)


if __name__ == "__main__":
    main()
