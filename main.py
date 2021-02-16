from replit import clear
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to Secret auction Program")

bid = {}
bidders = "yes"

while bidders == "yes":

  name = str(input("What is your name? : "))
  bid_amt = int(input("What is your bid? : "))
  bid.update({name: bid_amt})
  bidders = str(input("Are they any other bidders? :  ")).lower()
  clear()

winner = max(bid,key=bid.get)

print(f"the winner is {winner} with bid amount ${bid[winner]}")



