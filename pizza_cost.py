#!/usr/bin/env python3
# Created by Marc Coffi
# Created in March 2022
# This is a program that calculates
# the total price of a pizza based
# on the diameter given by the user

def main():
    print("Welcome")
    diameter = float(input("What is the diameter of your pizza? "))
    subtotal = 4.25+(1.50*diameter)
    tax = subtotal*0.13
    total_cost = subtotal+tax
    print("The Subtotal is ${:.2f}".format(subtotal))
    print("The total cost is ${:.2f}".format(total_cost))


if __name__ == "__main__":
    main()
