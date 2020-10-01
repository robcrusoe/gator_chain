# Initializes genesis_block
genesis_block = {'previous_hash': '', 'index': 0, 'transactions': []}
# Initializes our blockchain list
blockchain = [genesis_block]
# Initializes list of open_transactions
open_transactions = []
# Initializes the 'owner' instance of current blockchain
owner = 'Arka'


def get_transaction_value():
    """ Returns the input of the user for transaction details (Tuple) """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Enter the transaction amount: '))
    return (tx_recipient, tx_amount)


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Appends a new value as well as the last blockchain value to the current blockchain

    Arguments:
        :param sender: The sender of the coins.
        :param recipient: The recipient of the coins.
        :param amount: The amount of coins sent with the transaction (default = 1.0).
    """
    # Creates a local dictionary to store transaction details
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)


def mine_block():
    """ Adds a new block to our blockchain
        We want to take all open transactions and include them in a new block
    """
    last_block = blockchain[-1]
    print('** last_block: ', last_block)
    hashed_block = ''
    for key in last_block:
        value = last_block[key]
        hashed_block = hashed_block + str(value)

    print('** hashed_block: ', hashed_block)
    block = {'previous_hash': hashed_block, 'index': len(blockchain), 'transactions': open_transactions}
    blockchain.append(block)


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


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
    is_valid = True
    for block_index in range(len(blockchain)):
        print('++ blockchain ++', blockchain)

        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    else:
        print('*' * 130)

    return is_valid


waiting_for_input = True
while waiting_for_input:
    print('Please Choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Manipulate the blockchain')
    user_choice = get_user_choice()

    if user_choice == 1:
        tx_data = get_transaction_value()
        # Tuple unpacking
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print('** open_transactions: ', open_transactions)
    elif user_choice == 2:
        mine_block()
    elif user_choice == 3:
        # Output the blockchain list to the console
        print_blockchain_elements()
    elif user_choice == 6:
        waiting_for_input = False
    elif user_choice == 4:
        if len(blockchain) > 1:
            blockchain[0] = [2.0]
    else:
        print('Input was invalid! Please output from the list')
    # if not verify_chain():
    #     print('++ Invalid blockchain! ++')
    #     break
else:
    print('User left the room!')

print('Done!')