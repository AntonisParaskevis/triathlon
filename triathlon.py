while True:
    try:
        # Prompt the user to enter the number of hours spent running
        hours_running = float(input("Enter the number of hours spent running\n"))
        
        # If the user has entered either zero or a negative number, prompt them to enter a valid input
        if hours_running <= 0:
            print("Invalid entry, please enter a number greater than zero.")
            continue
        break
    except ValueError:
        # If the user has entered a non-numerical input, prompt them to enter a valid input
        print("Invalid entry, please enter a number greater than zero.")

# Same for the hours spent swimming and biking, respectively
while True:
    try:
        hours_swimming = float(input("Enter the number of hours spent swimming\n"))
        
        if hours_swimming <= 0:
            print("Invalid entry, please enter a number greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid entry, please enter a number greater than zero.")

while True:
    try:
        hours_biking = float(input("Enter the number of hours spent biking\n"))
        
        if hours_biking <= 0:
            print("Invalid entry, please enter a number greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid entry, please enter a number greater than zero.")

# Calculate the weight loss, using the user's input
lost_weight = ((hours_biking * 200) + (hours_running * 475) + (hours_swimming * 275)) / 3500

# Display the weight loss in pounds, rounded to 2 decimals
print("Weight loss: " + str(round(lost_weight, 2)) + " pounds.")

# In the end, prompt the user to press Enter, in order to exit the program

input("Press Enter to exit the program")
