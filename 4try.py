def update_vote(poll_number, option_name):
    # Check if the poll_number exists in polls_data
    if poll_number in polls_data:
        poll = polls_data[poll_number]
        options = poll["options"]
        
        # Check if the option_name exists in the poll
        if option_name in options:
            options[option_name] += 1  # Increment the vote count by 1
            print(f"Vote count for {option_name} in poll {poll_number} has been incremented.")
        else:
            print(f"Option {option_name} does not exist in poll {poll_number}.")
    else:
        print(f"Poll {poll_number} does not exist.")


poll_number = 3
option_name = puma
update_vote(poll_number, option_name)