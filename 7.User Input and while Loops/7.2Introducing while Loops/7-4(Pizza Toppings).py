prompt = "\nPlease enter pizza toppings"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print("We will add " + message + " topping to the pizza.")
