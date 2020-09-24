#
# Example file for working with conditional statements
#

def main():
  x, y = 10, 10
  
  # conditional flow uses if, elif, else  
  # if (x < y):
  #   print("x is less that y")
  # elif (x == y):
  #   print("x and y are equal")
  # else:
  #   print(" x is greater than y are equal")

  # conditional statements let you use "a if C else b"
  k = "x is less than y" if (x == y) else "x is greater than y or is same as y"
  print(k)
  
if __name__ == "__main__":
  main()