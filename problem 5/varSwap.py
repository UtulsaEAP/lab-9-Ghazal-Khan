def swap_values(user_val1, user_val2, user_val3, user_val4):   
   user_val1, user_val2 = user_val2, user_val1
   user_val3, user_val4 = user_val4, user_val3
    
   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':
    user_input1 = int(input())
    user_input2 = int(input())
    user_input3 = int(input())
    user_input4 = int(input())
    
    # Call swap_values and store the swapped values
    swapped_val1, swapped_val2, swapped_val3, swapped_val4 = swap_values(user_input1, user_input2, user_input3, user_input4)
    
    # Print the swapped values on a single line separated by spaces
    print(swapped_val1, swapped_val2, swapped_val3, swapped_val4)
