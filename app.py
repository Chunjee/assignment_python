from random import sample

alphanumeric = (
    'abcdefghijklmnopqrstuvwxyz' + \
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
    '01234567890'
)

strings_array = ("bleh")

print "Enter 1 for a human readable password or 2 for a randomized character password"
selection = input("Enter choice: ")


if selection == 1:
    print fn_characterpassgen()

if selection == 2:
    print fn_humanpassgen()

def fn_characterpassgen(length=12, chars=alphanumeric):
    return "".join(sample(chars, length))

def fn_humanpassgen(strings_array=):
    return "".join(sample(chars, length))
