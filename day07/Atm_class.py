class Atm :
    def __init__(self):

        self.pin = ''
        self.balance = 0
        
        self.menu()

    
    def menu(self) :
        user_input = input("""

                             Hello
                            How would you like to proceed
                           1. enter 1 to create pin
                           2. enter 2 to deposit
                           3. enter 3 to withdraw
                           4. enter 4 to check balance
                           5. enter 5 to exit
                           >>
                           """)

        if user_input ==  '1' :
            self.create_pin()
        
        elif user_input == '2' :
            self.deposit()
        
        elif user_input == '3' :
            self.withdraw()

        elif user_input == '4' :
            self.check_balance()

        elif user_input == '5' :
            print('thank you')
    
    def create_pin(self) :
        self.pin = input('create your pin ')
        print('pin set sucessfully')

    def deposit(self) :
        temp = input('enter your pin for deposit')
        if temp == self.pin :
            ammount = int(input('enter the ammount to deposit'))
            self.balance = self.balance + ammount
            print('Deposit successfully')
        else :
            print('Invalid pin')

    def withdraw(self) :
        temp = input('enter your pin for withdrawing ')
        if temp == self.pin :
            ammount = int(input('enter the ammount to withdraw'))
            if ammount <= self.balance :
                self.balance = self.balance - ammount
                print('withdrawn successfully')
            else :
                print('insufficient fund')
        else :
            print('invalid pin')

    def check_balance(self) :
        temp = input('enter your pin to check balance')
        if temp == self.pin :
            print(self.balance)
        else :
            print('invalid pin')

sbi = Atm()
sbi.create_pin()          
sbi.deposit()
sbi.withdraw()
sbi.check_balance()

