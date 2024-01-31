import math
import os
import random
import re
import sys

if __name__ == '__main__':
  n = int(input())
  print(("Not " if n%2==0 and (n<=4 or n>20) else "") + "Weird")

