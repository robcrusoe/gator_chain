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

""" A core concept of the Blockchain technology is that individual Blocks should be connected. 
    Each Block knows the Block coming prior to itself. 
    So Block C knows Block B which in turn is aware of Block A.

    
    What does "Know" mean though?
    To ensure data integrity, a hash is calculated for each Block. 
    We're not doing this yet but we'll add this functionality in the future.

    For now, we simply store the complete value of Block B in Block C 
    which then is stored in Block D - and so on.

    This allows us to check whether a certain Block in the Blockchain still looks the way 
    it looked like when the Block after it was added. So if we change Block B after we added Block C, 
    Block C will recognize that because it saved a snapshot of Block B when it (=> Block C) was created.

    This ensures that the Blockchain can't be manipulated by other users. 
    If you change a value, the other Blocks coming after it will recognize that.

    Of course, you could theoretically edit the entire Blockchain. 
    We'll add more security mechanisms in the future to ensure that this also doesn't work. 
    The relation between Blocks is a first important building block though. """
def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        print('Verifying Block: ', block)
        print('blockchain: ', blockchain)
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


while True:
    print('Please Choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('3: Quit current operation')
    print('4: Manipulate the blockchain')
    user_choice = get_user_choice()

    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == 2:
        # Output the blockchain list to the console
        print_blockchain_elements()
    elif user_choice == 3:
        break
    elif user_choice == 4:
        if len(blockchain) > 1:
            blockchain[0] = [2.0]
    else:
        print('Input was invalid! Please output from the list')
    if not verify_chain():
        print('++ Invalid blockchain! ++')
        break


print('Done!')