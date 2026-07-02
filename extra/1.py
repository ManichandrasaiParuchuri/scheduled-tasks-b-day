# Your code goes here
import datetime as dt
import random
from linecache import getline

now = dt.datetime.now()
with open("quotes.txt", mode="r", encoding="utf-8") as quotes:
    quote = quotes.readlines()
my_quote = random.choice(quote)
print(my_quote)
print(now.date())

