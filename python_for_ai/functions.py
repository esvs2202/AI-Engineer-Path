def greet():
    print("Hello !!!")
    pass

greet()


def check_weather(temperature = 20):
    if temperature > 25:
        print("It's hot! ")
    else:
        print("It's a nice weather")

check_weather(15)
check_weather(26)    


def calculate_total(price, tax_rate, discount_rate):
    discounted_price = price * discount_rate
    taxed_amt = price * tax_rate
    total_price = price + taxed_amt - discounted_price
    return f"Total price  = {total_price}"

calculate_total(100,0.25,0.4)


    