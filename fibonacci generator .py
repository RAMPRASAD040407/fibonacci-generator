def fibonacci_generator():
    
    first_number = 0
    second_number = 1

    
    while True:
        
        yield first_number

        
        next_number = first_number + second_number

        
        first_number = second_number
        second_number = next_number

fibonacci = fibonacci_generator()


count = 0
while count < 10:
    number = next(fibonacci)  
    print(number)
    count += 1
