import datetime
from faker import Faker
fake = Faker(locale=['en_CA', 'en_US'])

app = 'Advantage Shopping Cart'
adshopcart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_homepage_title = 'Advantage Shopping'
adshopcart_register_url = 'https://advantageonlineshopping.com/#/register'
adshopcart_account_url = 'https://advantageonlineshopping.com/#/myAccount'
adshopcart_orders_url = 'https://advantageonlineshopping.com/#/MyOrders'

username = fake.user_name()[0:14]
email = fake.email()
password = fake.password()
confirm_password = password
firstname = fake.first_name()
lastname = fake.last_name()
fullname = f'{firstname} {lastname}'
phonenum = fake.phone_number()
country = fake.current_country()
city = fake.city()
address = fake.street_address()
province = fake.province_abbr()
postalcode = fake.postalcode()
description = f'Please send me any promotion about laptop HP Chromebook 14 G1(ENERGY STAR) to {email}. Thank you!'

lst_items = ['SPEAKERS', 'TABLES', 'HEADPHONES', 'LAPTOPS', 'MICE']
lst_id = ['speakersTxt', 'tabletsTxt','headphonesTxt', 'laptopsTxt', 'miceTxt']
lst_link = ['SPECIAL OFFER', 'POPULAR ITEMS', 'CONTACT US']
lst_link_id = ['special_offer_items', 'popular_items', 'supportCover']