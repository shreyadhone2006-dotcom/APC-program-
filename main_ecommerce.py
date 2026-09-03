from Products.product import display_product
from Products.category import display_category

from Customers.customer import display_customer
from Customers.address import display_address

from Orders.order import place_order
from Orders.cart import add_to_cart

from Payments.payment import make_payment
from Payments.invoice import generate_invoice


display_product()
display_category()

display_customer()
display_address()

add_to_cart()
place_order()

make_payment()
generate_invoice()