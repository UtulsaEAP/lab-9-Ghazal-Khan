def feet_to_steps(user_feet):
   #write your code here
    return int(user_feet / 2.5)
15
if __name__ == '__main__':
    # Take input for feet walked
    user_feet = float(input())
    
    # Call the feet_to_steps function and store the result
    steps = feet_to_steps(user_feet)
    
    # Print the number of steps as an integer
    print(steps)
