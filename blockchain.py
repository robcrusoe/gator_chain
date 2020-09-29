# Initializes our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    """ Appends a new value as well as the last blockchain value to the current blockchain

    Arguments:
        :param transaction_amount: The amount that should be added
        :param last_transaction: The last blockchain transaction (default [1.0])
    """
    if last_transaction == None:
        last_transaction = [1.0]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float """
    return float(input('Your transaction amount please: '))


def get_user_choice():
    """ Returns the choice of the user to either add a new transaction or view the existing blockchain """
    user_input = input('Your choice: ')
    return int(user_input)


def print_blockchain_elements():
    """ Prints all the elements present in our 'main' blockchain """
    for block in blockchain:
        print('Outputting Block')
        print(block)


while True:
    print('Please Choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('3: Quit current operation')
    user_choice = get_user_choice()

    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == 2:
        # Output the blockchain list to the console
        print_blockchain_elements()
    elif user_choice == 3:
        break
    else:
        print('Input was invalid! Please output from the list')


print('Done!')