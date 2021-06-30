while True:
  try:
    bound = int(input("What number would you like to print the fib sequence up to?"))
  except:
    print("Please only input a whole number")
    continue
  x = 0
  y = 1
  z = 1
  print("0")
  while(y <= bound):
    print(y)
    z = x + y
    x = y
    y = z
  break 