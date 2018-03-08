#!/usr/bin/env python3

def op_pow(a, b):
    return a ** b

def op_add(a, b):
	return a + b

ops = {
	'^': op_pow,
	'+': op_add,
}


def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)

        except ValueError:
            arg2 = stack.pop()
            arg1 = stack.pop()
            if token in ops:
        	    return ops[token](arg1, arg2)

def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()

