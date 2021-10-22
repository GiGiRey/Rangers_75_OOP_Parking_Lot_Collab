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
    
    def __init__(self, capacity = [False, False, False, False, False], tickets = {}, ticket_num = (1)):
        self.capacity = capacity
        self.tickets = tickets
        self.ticket_num = ticket_num
        
    def takeTicket(self):
        if False not in self.capacity:
            print("Sorry we have not parking available today")
        
        else:
            print(f"You are number {self.ticket_num} ")
            self.tickets[self.ticket_num] = False
            self.capacity.remove(False)
            self.capacity.append(True)
            self.ticket_num += 1

    
def run():
    
    jonlissa = Garage()

    while True:
        response = input("what would you like to do? park/pay/leave/quit: ")
        
        if response.lower() not in ['park','pay','leave','quit']: #membership check
            response = input('Please enter a VALID choice park/pay/leave or quit:')     
        
        if response.lower() == 'quit':
            print('Thanks for visiting Jonlissa Parking Systems !')
            break
        
        elif response.lower() == 'park':
            jonlissa.takeTicket()
            
        # elif response.lower() == 'pay':
        #     # mage_bag.addToInventory()

        # elif response.lower() == 'leave':
        #     # mage_bag.showInventory()

run()