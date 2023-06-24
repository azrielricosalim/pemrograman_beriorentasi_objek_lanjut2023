def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
        product = total * 2
    print(product)
    
calculate_sum([1, 2, 3, 4])