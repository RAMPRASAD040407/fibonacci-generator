# fibonacci-generator
The generator function uses Python’s yield keyword to lazily return the next Fibonacci number in the sequence each time it is called.

Fibonacci Sequence:
Copy
Edit
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Each number is the sum of the two preceding ones.

📦 Requirements
Python 3.x
No external libraries are needed.

▶️ Usage
Clone or download the repository.

Run the fibonacci.py file:

bash
Copy
Edit
python fibonacci.py
Sample output (first 10 Fibonacci numbers):

Copy
Edit
0
1
1
2
3
5
8
13
21
34
🧠 How the Code Works
python
Copy
Edit
def fibonacci_generator():
    first_number = 0
    second_number = 1
    while True:
        yield first_number
        next_number = first_number + second_number
        first_number = second_number
        second_number = next_number
Initializes the first two numbers: 0 and 1

Uses yield to return values one at a time

Updates the numbers on each iteration to generate the next in the sequence

✅ Benefits of Using a Generator
Memory efficient: Doesn't store the entire sequence

Scalable: Can be used to generate as many numbers as needed

Simple & clean syntax

 
