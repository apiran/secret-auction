def clear_screen():
    """
    Clear the console screen using ANSI escape codes.
    This works on Unix-based systems and Windows 10+.
    """
    print("\033[H\033[J", end="")

def get_bid():
    """
    Prompt the user for a valid bid amount and return it.
    Handles invalid inputs by prompting again.
    """
    while True:
        try:
            bid_amount = int(input("What's your bid?: $"))
            return bid_amount
        except ValueError:
            print("Please enter a valid number.")

def main():
    """
    Main function to run the secret auction program.
    """
    print("Welcome to the secret auction program")

    # Dictionary to store the bidders and their respective bids
    bids = {}
    continue_bidding = True

    while continue_bidding:
        bidder_name = input("What is your name?: ")
        bid_amount = get_bid()
        bids[bidder_name] = bid_amount
        
        # Check if there are more bidders
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if more_bidders == 'no':
            continue_bidding = False
        elif more_bidders == 'yes':
            clear_screen()  # Clear the screen for the next bidder
        else:
            print("Invalid input, please type 'yes' or 'no'.")

    if bids:
        # Find the bidder with the highest bid
        highest_bidder = max(bids, key=bids.get)
        highest_bid = bids[highest_bidder]
        clear_screen()
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
    else:
        print("No bids were placed.")

# Run the main function
if __name__ == "__main__":
    main()