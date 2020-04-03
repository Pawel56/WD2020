import sys
print("podaj dwie wartosci")
a=sys.stdin.readline()
b=sys.stdin.readline()
a=int(a)
b=int(b)
a*=b
a=str(a)
sys.stdout.write(a)
