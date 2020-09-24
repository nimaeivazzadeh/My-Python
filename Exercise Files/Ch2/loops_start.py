#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop 
  # while(x < 5):
  #   print(x)
  #   x += 1


  # define a for loop
  # for i in range(5, 10):
  #   print(i)


  # use a for loop over a collection
  # days = ["Sat", "Sun", "Mon"]
  # for d in days:
  #   print(d)

  # use the break and continue statements
  # for i in range(5, 10):
  #   # if (i == 7): break
  #   if (i % 2 == 0): continue
  #   print(i)

  #using the enumerate() function to get index
  days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
  for i, d in enumerate(days):
    print(i, d)

if __name__ == "__main__":
  main()
