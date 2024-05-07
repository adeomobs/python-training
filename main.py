MAX_LINES = 5
MIN_BET = 1
MAX_BET = 100

def deposit():
    while True:
        amount = input('Enter amount to deposit $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Input must be a number')
    return amount


deposit()


def get_lines_to_bet_on():
    while True:
        lines = input('Enter the number of lines to bet on (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines')
        else:
            print('Please enter a number')
    return lines

get_lines_to_bet_on()



def get_bets():
    while True:
        amount = input('How much would you like to bet on each line $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}')
        else:
            print('Input must be a number')
    return amount

get_bets()


def main():
    balance = deposit()
    lines = get_lines_to_bet_on()
    while True:
        bet = get_bets()
        total_bets = bet * lines
        if total_bets > balance:
            print(f'You do not have enough balance to play this bet. Your balance is ${balance}')
        else:
            break
        
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bets}')


main()