# Stock Sim 2

from math import floor
from os import remove, system, name # Study!
import random
import threading
import time
from enum import Enum

# Allow for multiple portfolios as well as the viewing and loading of them
#   - File handling will be important
# Create multiple formulas to competently simulate market
# Simulate multiple stocks

class INDUSTRIES(Enum):
	TECH = 1
	SCIENCE = 2
	MEDICINE = 3
	TRANSPORT = 4
	AUTOMOTIVE = 5

class Stock:
	rank = 0 # Global rank based on netWorth
	industryType = INDUSTRIES.TECH
	locCur = 'United Kingdom' # Defines both location and currency
	def __init__(self, name = 'DFLT', tVal : float = 100.0) -> None:
		self.totalValue : float = tVal
		self.shareCost : float = tVal
		self.history : float = [self.shareCost]
		self.stockName = name # | Default

	def GetWorth(self) -> float:
		pass

	def Print(self, amount): # Prints current value and history | Specify amount of history to be printed!
		for val in range(len(self.history)-1):
			if self.history[val+1] > self.history[val]:
				print(self.history[val], end='↑')
			elif self.history[val+1] < self.history[val]:
				print(self.history[val], end='↓')
			else:
				print(self.history[val], end='→')

	# Returns an overall score of how well the stock is performing, or if it is bankrupt
	# Affected by industry type
	def CheckState(self):
		pass

# ========================= Stocks/Companies =========================
_Tesla                = Stock("TSLA", 1000.0)
_Apple                = Stock("APPL", 875.0)
_AdvancedMicroDevices = Stock("AMD", 150.0)
_Intel                = Stock("INTL", 75.0)
# ====================================================================

# Global Parameters
simulating = True
tickRate : float = 1.0
location = ['United Kingdom', 'North America', 'Japan', 'Europe'] # Can remove, calculate based on currency
currencies = {'£' : 'GBP',
			  '$': 'USD',
			  '€': 'EUR',
			  '¥' : 'JPY'}
marketHours = [8, 4] # AM - PM | Defaults to UK
# Improve date and time
hour : int = 0
day : int = 1 
month : int = 1
year : int = 2021

class Portfolio: # Person
	percentOwned : float = [0.0] # Matches company index
	moneyAvailable : float = 1000.0
	def __init__(self) -> None:
		self.worth : float = 10.0
		self.curInvestments = {'' : 0} # Market name, current amount invested | Add current amount of shares | Change?

	def PrintPortfolio(self):
		for i in self.curInvestments:
			pass

class Share:
	def __init__(self) -> None: # Inherits parent stocks value
		self.value : float = 0.0

companies : Stock = [_Tesla, _Apple, _AdvancedMicroDevices, _Intel]

def KeyboardParser():
	curInput = input()
	if curInput == '98' or curInput == '66': # b/B
		print("BACK")

# ======================= Simulate =======================
def Simulate(): # Run in own thread | Main function
	while(simulating):
		system('cls')
		# Add opening and closing hours
		print("Hour: ", hour)
		print('Day: ', day, 'Month: ', month, 'Year: ', year)
		for stock in companies:
			print(stock.shareCost, ': ' , '======| ', stock.stockName, ' |======')
			stock.Print()
			print('\n-----------------------------------------------------------')

			# Simulate:
			change = abs(floor((stock.totalValue/100) - (stock.shareCost/1000))) # Improve
			fluctuation = random.randrange(0, 10)
			if fluctuation > 5:
				stock.shareCost += change
			else:
				stock.shareCost -= change
			if stock.shareCost <= 0.0:
				print(stock.stockName, ' went bankrupt on ', day,'/',month,'/',year) # Add date!
				# Delete stock
			stock.history.append(stock.shareCost)
			# Add percent change
	
		time.sleep(tickRate)

		# Date & Time:
		#global hour
		#hour += 1

# ========================================================

def BuySell(curPort):
	if len(companies) == 0:
		print('There are no companies on the market!')
		Interface()
	for stock in companies:
		print(stock.stockName, ' : ', stock.shareCost)
	# Add available options based on amount in bank
	if curPort.moneyAvailable <= 0 and len(curPort.currentInvestments) > 0:
		print('Warning: You currently have no money in your account, sell existing stocks')
	elif curPort.moneyAvailable <= 0 and len(curPort.currentInvestments) <= 0:
		print('Warning: You currently have no money in your account and no stocks to sell')
		print('Closing portfolio!...')
		time.sleep(2)
	print("1) BUY  2) SELL")


def Interface():
	print("|=====STOCK SIM 2=====|")
	print("What would you like to do:")
	print("1) View Stocks  2) Buy/Sell  3) Quit")
	print("Enter: ", end='') 
	# Replace with custom keyboard parser to allow for constant threaded input
	choice = input()
	if choice == '1': # TEMP!!!
		Simulate()
	elif choice == '2':
		BuySell()
	elif choice == 3:
		return

def main() -> int:
	random.seed() # Check!

	inputThread = threading.Thread(target=KeyboardParser(), daemon=True)
	inputThread.start()
	Interface()

	return 0

if __name__ == "__main__":
	main()