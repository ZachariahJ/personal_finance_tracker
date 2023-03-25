from main import Transactions
from datetime import date
Z = Transactions()

# for i in range(10):
#     Z.write_to_db(date=date(i*856+1,i+1,i+2), type=f"expense{i}", amount=-i*150, detail="f{i}OH! NO!")
Z.clear_all()
# from api import text_formatting as tf

# usrInput = tf(input("Enter a string: "))
# print(usrInput)