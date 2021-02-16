import second

def fibonachi(number):
    n=1,cur_numb=0
    while number!=0:
        n+=cur_numb
        cur_numb=n
        number--
    return n
number = 20
n = fibonachi(number)
second.repeater(n,10)