def paperwork(n, m):
    if n < 0 or m <0 :
        print('0')
    else:
        print(n*m)

paperwork(5 , -5 )


def rental_car_cost(d):
    cost = d * 40
    if d >= 7 :
        print(cost - 50)
    elif d >= 3:
        print(cost - 20)

rental_car_cost(40)


def remove_url_anchor(url):
    print(url.split('#')[0])

remove_url_anchor('www.codewars.com#about')

a ="yes#yes#yes".split("#")[0]
print(a)