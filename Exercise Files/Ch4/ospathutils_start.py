#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  # print(os.name)


  # Check for item existence and type
  # print("Item exists: " + str(path.exists("textfile")))
  # print("Item is a file: " + str(path.isfile("textfile")))
  # print("Item is a directory: " + str(path.isdir("textfile")))

  
  # Work with file paths
  # print("Item path: " + str(path.realpath("textfile")))
  # print("Item path and name: "+ str(path.split(path.realpath("textfile"))))

  
  # Get the modification time
  # t = time.ctime(path.getmtime("textfile"))
  # print(t)
  # print(datetime.datetime.fromtimestamp(path.getatime("textfile")))

  
  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile"))
  print("It has been " + str(td) + " Since the file was modified")
  print("or, " + str(td.total_seconds())+ " seconds")

  
if __name__ == "__main__":

  main()
