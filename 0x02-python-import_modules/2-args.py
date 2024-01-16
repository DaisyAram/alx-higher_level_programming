#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arglen = len(sys.argv)
    if arglen == 1:
        print('{} arguments.'.format(arglen - 1))
    elif arglen == 2:
        print('{} arguments.'.format(arglen - 1))
    else:
        print('{} arguments:'.format(arglen - 1))
        for i in range(1, arglen):
            print('{}:{}'.format(i, sys.argv[i]))
