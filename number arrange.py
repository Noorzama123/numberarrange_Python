a=input('enter the number')
num=""
n=""
for x in a:
    print(x)
    match x:
        case '0':
            num="zero"
        case '1':
            num="one"
        case '2':
            num="two"
        case '3':
            num="three"
        case '4':
            num="four"
        case '5':
            num="five"
    n=n+num   
print("final number 2 text:" , a, "->", n)    