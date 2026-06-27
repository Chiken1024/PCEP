def input_int() -> None:
  # try:
  #   num: int = int(input("Enter an integer: "))
  # except ValueError:
  #   raise ValueError("Invalid input for type 'int'")
  num: int = int(input("Enter an integer: "))

# input_int()

def input_2_nums() -> None:
  try:
    num1, num2 = int(input("Enter a number: ")), int(input("Enter a second number: "))
  except ValueError:
    raise ValueError("One or both of the inputs invalid for type 'int'")

# input_2_nums()

def add_1(nums: list[int], index: int) -> None:
  try:
    nums.add(index)
  except AttributeError:
    print("The element you attempted to index does not exist")



def divide(f1: float, f2: float) -> float:
  try:
    return f1 / f2
  except ZeroDivisionError:
    print("Cannot divide by zero")

divide(5.0, 0.0)