try:
    x = int(input("Enter a number: "))
except EOFError:
    print("End of file reached")
except ValueError:
    print("Invalid input")