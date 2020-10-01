# Function to check for valid number or integer
def test_num(input_num):

    # Iterate through each character of string
    for i in range(len(input_num)):
        
        # Return False, if error found
        if input_num[i].isdigit() == False:
            return False

    # Return True, if no error found
    return True
