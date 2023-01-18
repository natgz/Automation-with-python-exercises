# Input de costo total
# Input de personas en la mesa
# Input de propina a pagar
# El total de propina que se va a pagar
# La cantidad que le corresponde a cada persona en la mesa a pagar

print('Welcome to the tip calculator!')

while True:
    try:
        bill = float(input('Insert bill without tip:'))
        break
    except ValueError:
        print('Please enter just numbers.')

while True:
    try:
        tip = float (input('Insert tip percentaje you want to give:'))
        break
    except ValueError:
        print('Please enter just numbers.')

while True:
    try:
        qty = int (input('Insert qty of people to split the bill with:'))
        break
    except ValueError:
        print('Please enter a natural number.')


tip_decimal = tip/100
total_tip = bill*tip_decimal
total_bill = (total_tip)+bill

divided_bill = (total_bill)/qty

print('The total tip is ${r:1.2f}'.format(r=total_tip))
print('The total to pay per person is $ {r:1.2f}'.format(r=divided_bill))