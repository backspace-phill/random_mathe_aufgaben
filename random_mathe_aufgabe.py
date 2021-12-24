import argparse
from random import randint
parser = argparse.ArgumentParser()
parser.add_argument("Menge", type=int)
parser.add_argument("-a", help="Additionsaufgaben (STANDARD)", action="store_true")
parser.add_argument("-m", help="Minusaufgaben Überschreibt -a", action="store_true")
parser.add_argument("-d", help="Divisionsaufgaben Überschreibt -a&-m", action="store_true")
parser.add_argument("-p", help="Multiplikationsaufgaben Überschreibt alle anderen Flags", action="store_true")
parser.add_argument("-u", help="Unteres Limit der Zahlen", type=int, default=1)
parser.add_argument("-o", help="Zahl Oberlimit der Zahlen", type=int, default=100)
args= parser.parse_args()
def set_operation():
    """ Diese Funktion überprüft die Argumente und wandelt sie ihn in einen Char um der später in den Aufgaben verwendet wird
    """
    operator = ""
    if args.p:
        operator = "*"
    elif args.d:
        operator = "/"
    elif args.m:
        operator = "-"
    elif args.a:
        operator = "+"
    else:
        operator = "+"
    return operator
''' Main for Loop für das erstellen der Aufgaben
'''
for i in range(args.Menge):
    operator = set_operation()
    zahlen = randint(args.u,args.o), randint(args.u,args.o)
    zahlen = sorted(zahlen)
    zahlen.reverse()
    zahlen.insert(1, operator)
    aufgabe = zahlen
    print(str(aufgabe[0])+aufgabe[1]+str(aufgabe[2]))
