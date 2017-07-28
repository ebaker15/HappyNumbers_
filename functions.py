
def convercelciustofehrenheits():
    c = float(input("Please Enter Celsius                     :       "))
    f = (9/5)*c + 32
    print(f)
howmanytimes = int(input("How Many Times Do You Want To Run This Program To Find Fehrenheit From Celcius   :"))

for howmanytimes in range (0,howmanytimes):
    convercelciustofehrenheits()

'''
def happynumbers(n):
     seen = set()
     while True:
           digits = [int(c) for c in str(n)]
           n = sum(digit**2 for digit in digits)
           if n == 1:
                return true
'''
