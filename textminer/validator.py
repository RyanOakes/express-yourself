import re


def binary(value):
    return re.match(r'[01]', value)

def binary_even(value):
    return re.match(r'^[01]+0$', value)

def hex(value):
    return re.match(r'^[\d,A-F]+$', value)

def word(value):
    return re.match(r'^[\w-]*[^\d]$', value)

# def words(value):
    #return value

def phone_number(value):
    return re.findall(r'\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}', value)

def money(value):
    return re.match(r'[$]((\d{1,3},)*\d{3}|\d+)(\.\d{2})?$', value)

def zipcode(value):
    return re.match(r'^\d{5}(?:[-\s]\d{4})?$', value)

def date(value):
    return re.match(r'[\d/-]+', value)

 # @xfail
 # def test_date():
 #     assert v.date("9/4/1976")
 #     assert v.date("1976-09-04")
 #     assert v.date("2015-01-01")
 #     assert v.date("02/15/2004")
 #     assert not v.date("9/4")
 #     assert not v.date("2015")






# # ## HARD MODE BEGINS
# #
# #
# # @xfail
# # def test_hard_date():
# #     assert v.date("2014 Jan 01")
# #     assert v.date("2014 January 01")
# #     assert v.date("Jan. 1, 2015")
# #     assert not v.date("07/40/2015")
# #     assert not v.date("02/30/2015")
# #
# #
# # @xfail
# # def test_email():
# #     """Some of the emails listed as invalid are actually valid according to
# #     the email spec, but we will not accept them."""
# #
# #     assert v.email("stroman.azariah@yahoo.com")
# #     assert v.email("viola91@gmail.com")
# #     assert v.email("eathel.west@example.org")
# #     assert v.email("dwehner@harley.us")
# #     assert v.email("malcolm.haley@hotmail.com")
# #     assert v.email("ezzard90@hotmail.com")
# #     assert v.email("legros.curley@gmail.com")
# #     assert v.email("leatha75@mertz.net")
# #     assert v.email("bonita43@yahoo.com")
# #     assert not v.email("")
# #     assert not v.email("legros.curley")
# #     assert not v.email("mertz.net")
# #     assert not v.email("bonita43@")
# #
# #
# # @xfail
# # def test_address():
# #     """This must be a full address with street number, street, city, state,
# #     and ZIP code. Again, US-only."""
# #     assert v.address("""368 Agness Harbor
# #     Port Mariah, MS 63293""")
# #     assert v.address("""96762 Juluis Road Suite 392
# #     Lake Imogenemouth, AK 20211""")
# #     assert v.address("""671 Tawnya Island Apt. 526
# #     Clementeburgh, AK 82652""")
# #     assert v.address("""568 Eunice Shoals
# #     Parishaven, AK 09922-2288""")
# #     assert v.address("8264 Schamberger Spring, Jordanside, MT 98833-0997")
# #
# #     assert not v.address("")
# #     assert not v.address("99132 Kaylah Union Suite 301")
# #     assert not v.address("Lake Joellville, NH")
# #     assert not v.address("35981")
