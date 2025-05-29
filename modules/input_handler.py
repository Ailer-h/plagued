# Function that gets the user input and converts it into an integer
# It repeatedely asks for input until a valid integer is entered
def get_int_force(msg: str, bounds: dict[str, int] | None = None):
    while True:
        try:
            user_int: int = int(input(msg))
            if bounds is None:
                return user_int
            
            if user_int >= bounds['min'] and user_int <= bounds['max']:
                return user_int
            
            print(f"Please enter a number between {bounds['min']} and {bounds['max']}")
                
        except ValueError:
            print("Invalid input. Please enter a valid option.")

# Function that gets the user input and converts it into an integer
# If the input is not valid it outputs a default value
def get_int_soft(msg: str, bounds: dict[str, int] | None = None, default: int = -1):
    user_input: str = input(msg)
    try:
        user_int: int = int(user_input)

        if bounds is None:
            return user_int
        
        if user_int >= bounds['min'] and user_int <= bounds['max']:
            return user_int
        
        return default

    except ValueError:
        return default

# Function that gets the user input and converts it into an integer
# This function controls which way of getting the input to use
def get_int(msg: str, repeat: bool = False, default: int = -1, bounds: dict[str, int] | None = None) -> int:
    
    if repeat:
        return get_int_force(msg, bounds)
    
    return get_int_soft(msg, bounds, default)