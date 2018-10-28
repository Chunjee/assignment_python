# /--\--/--\--/--\--/--\--/--\--/--\
#  Description
# \--/--\--/--\--/--\--/--\--/--\--/
#  Generates 2 types of usable passwords

# ~~~~~~~~~~~~~~~~~~~~~
# imports
# ~~~~~~~~~~~~~~~~~~~~~
from random import sample



# ~~~~~~~~~~~~~~~~~~~~~
# global vars
# ~~~~~~~~~~~~~~~~~~~~~
alphanumeric = (
    'abcdefghijklmnopqrstuvwxyz' + \
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
    '01234567890'
)

tupl1 = ("attractive","agreeable","angry","big","bald","ambitious","colossal","brave","clumsy","gigantic","scruffy")
tupl2 = ("apple","eagle","knight","landlord","cashier","phone")
tupl3 = ("0","1","2","3","4","5","6","7","8","9")
tupl4 = ("!","@","#","$","%","^","&","*","-","+")



# ~~~~~~~~~~~~~~~~~~~~~
# functions
# ~~~~~~~~~~~~~~~~~~~~~
def fn_characterpassgen(length=12, chars=alphanumeric):
    return "".join(sample(alphanumeric, length))

def fn_humanpassgen():
    return sample(tupl1, 1)[0] + sample(tupl2, 1)[0] + sample(tupl3, 3)[0] + sample(tupl3, 1)[0] + sample(tupl4, 1)[0]



# /--\--/--\--/--\--/--\--/--\--/--\
#  MAIN
# \--/--\--/--\--/--\--/--\--/--\--/
print "Enter 1 for a human readable password or 2 for a randomized character password"
selection = input("Enter choice: ")

if selection == 1:
    print fn_characterpassgen()

if selection == 2:
    print fn_humanpassgen()
