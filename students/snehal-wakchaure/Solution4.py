def add_item(total, price):
    return total + price


def apply_tax(total):
    return total * 1.05


def main():
    total = 0

    total = add_item(total, 40)
    total = add_item(total, 25)
    total = add_item(total, 15)

    print("Cart total:", total)
    print("With tax:", apply_tax(total))


main()



def rectangle(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter



def circle(r)
 a=π*(r**2) pi=3.14
 return (a)
