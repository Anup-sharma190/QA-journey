#Create a variable ItemsInCart and initialize it to 0.

#Write a function called add_to_cart that accepts an integer parameter items_to_add.

#If items_to_add is less than 0, raise an exception with the message "Cannot add a negative number of items."

#If the total count of items after addition exceeds 5, raise an exception with the message "Cart limit exceeded."
# Initialize the cart
ItemsInCart = 0

# Define the function
def add_to_cart(items_to_add):
    global ItemsInCart  # To modify the global variable

    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")

    if ItemsInCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    ItemsInCart += items_to_add
    print(f"Items successfully added. Total items in cart: {ItemsInCart}")

# Example usage:
try:
    add_to_cart(1)
    add_to_cart(1)
    add_to_cart(3)  # This will raise an exception
except Exception as e:
    print(f"Error: {e}")
