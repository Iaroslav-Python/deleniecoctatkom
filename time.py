while True:
    q = input('Напишите свое число: ')
    q = int(q)
    w = input('Напишите число на которое делим: ')
    w = int(w)
    a = q//w
    c = q%w
    print(a,"Ост:",c )