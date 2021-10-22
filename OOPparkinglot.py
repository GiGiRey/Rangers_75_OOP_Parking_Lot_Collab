# work breakdown
# 30 min brainstorming
# 1 hr mesliisa coding - init, takeTicket and skeleton of def run() and made 
# 1 hr Jon coding - view items, pay, leave

import os
os.system('cls' if os.name == 'nt' else 'clear')


class Garage():
    """
    The Garage Class will have capacity and items (ie cars) to place inside
    
    Attributes for Garage():
    -capacity: expect an integer which represents the # of spaces
    -items: expected to be a list of Cars
    
    The functions in Garage():
    
    - initialization
    - checking if parking is available
    - if parking is available
        assign car to spot : parkingList (bool)
    - if parking is not available
        print message
        
    - when checking out
        request car information
        calculate rate required to be paid
        mark ticket paid
    """
    
    def __init__(self, capacity = [False, False, False, False, False], tickets = {}, ticket_num = (1), ticket_payment_amount = {}):
        self.capacity = capacity
        self.tickets = tickets
        self.ticket_num = ticket_num
        self.ticket_payment_amount = ticket_payment_amount
        
    def takeTicket(self):
        if False not in self.capacity:
            print("Sorry we have no parking available today")
        
        else:
            print(f"You are number {self.ticket_num} ")
            self.tickets[self.ticket_num] = "False"
            self.capacity.remove(False)
            self.capacity.append(True)
            self.ticket_num += 1

    def viewItems(self):
        print(self.capacity)
        print(self.ticket_num)
        print("Ticket Number    Paid Status")
        for key, value in self.tickets.items():
                print('{0:<17}{1:<4}'.format(key,value))
        print("Ticket Number    Amount Paid")
        for key, value in self.ticket_payment_amount.items():
                print('{0:<17}{1:<4}'.format(key,value))

    def payParking(self):
        parking_spot = input("What is your ticket number? ")
        if parking_spot.isdigit() == False:
            print("Please enter a valid number")
        elif int(parking_spot) not in self.tickets.keys():
            print("This ticket does not exist. Please enter a valid ticket number")
        else:
            payment_ammount = input("What is the cost of your ticket? ")
            try: float(payment_ammount)
            except: 
                print("Please enter a valid dollar amount")
            if float(payment_ammount) < 0:
                print("Please enter a valid dollar amount?")
            else:
                self.tickets[int(parking_spot)] = "True"
                self.ticket_payment_amount[int(parking_spot)] = payment_ammount
                print("Thank you for paying. You have 15 minutes to exit the parking garage")

    def leaveGarage(self):
        leave_number = input("Please enter your ticket number: ")
        if leave_number.isdigit() == False:
            print("Please enter a valid number")
        elif int(leave_number) not in self.tickets.keys():
            print("Please enter a valid number")
        elif self.tickets.get(int(leave_number)) == "False":
            print("Please pay for your ticket.")
        else:
            print("This ticket has been paid for. Please exit the garage and have a nice day!")
            self.capacity.remove(True)
            self.capacity.append(False)


    
def run():
    
    jonlissa = Garage()

    while True:
        response = input("what would you like to do? park/pay/leave/quit: ")
        
        if response.lower() not in ['park','pay','leave','quit','view']: #membership check
            response = input('Please enter a VALID choice park/pay/leave or quit:')     
        
        if response.lower() == 'quit':
            print('Thanks for visiting Jonlissa Parking Systems !')
            break
        
        elif response.lower() == 'park':
            jonlissa.takeTicket()

        elif response.lower() == "view":
            jonlissa.viewItems()
            
        elif response.lower() == 'pay':
            jonlissa.payParking()

        elif response.lower() == 'leave':
            jonlissa.leaveGarage()

run()