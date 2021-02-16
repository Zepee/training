import second

def fibonachi(number):
    int n=1,cur_numb=0
    while number!=0:
        n+=cur_numb
        cur_numb=n
        number--
    return n
int number = 20
int n = fibonachi(number)
second.repeater(n,10)