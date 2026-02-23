class Atm:
    # 1. THE CONSTRUCTOR
    # This runs automatically when you create a new Atm() object.
    # It initializes the machine's memory (pin and balance).
    def __init__(self):

        
        # Instance Variables: Data specific to THIS machine
        self.pin = ""
        self.balance = 0
        
        # We trigger the menu immediately so the user sees options right away
        self.menu()

    # 2. THE MENU (The Interface)
    def menu(self):
        # triple quotes """ allow multi-line strings
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Press anything else to exit
        """)

        # Logic to decide where to go next
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            print("Exiting. Have a nice day!")
            exit() # This kills the program

    # 3. CREATE PIN
    def create_pin(self):
        # We take input as a string because pins like "0012" are valid
        user_pin = input('Enter your new pin: ')
        self.pin = user_pin

        # We convert balance to 'int' because we need to do math with it
        user_balance = int(input('Enter initial balance: '))
        self.balance = user_balance

        print('Pin created successfully')
        
        # Go back to menu so the user can do other things
        self.menu()

    # 4. CHANGE PIN
    # TEACHER NOTE: You originally wrote "def change_pin():"
    # You MUST include 'self' so the function can access self.pin
    def change_pin(self):
        old_pin = input('Enter old pin: ')

        # Verification step
        if old_pin == self.pin:
            # allow him to change the pin
            new_pin = input('Enter new pin: ')
            self.pin = new_pin
            print('Pin change successful')
        else:
            print('Nai karne de sakta re baba (Wrong Pin!)')
            
        self.menu()

    # 5. CHECK BALANCE
    def check_balance(self):
        user_pin = input('Enter your pin: ')
        
        if user_pin == self.pin:
            print('Your balance is: ', self.balance)
        else:
            print('Chal nikal yahan se (Wrong Pin!)')
            
        self.menu()

    # 6. WITHDRAW
    def withdraw(self):
        user_pin = input('Enter the pin: ')
        
        if user_pin == self.pin:
            # Pin is correct, now ask for amount
            amount = int(input('Enter the amount: '))
            
            # Check if they have enough money!
            if amount <= self.balance:
                # Deduct the money
                self.balance = self.balance - amount
                print('Withdrawal successful. Remaining balance is', self.balance)
            else:
                print('Abe garib (Insufficient Funds)')
        else:
            print('Sale chor (Wrong Pin)')
            
        self.menu()

# ---------------------------------------------------------
# HOW TO RUN THIS CODE
# ---------------------------------------------------------
# This logic below checks if we are running this file directly.
if __name__ == "__main__":
    # Create an object (Build the actual machine)
    sbi = Atm() 
    # Because __init__ calls self.menu(), the program starts immediately.