#Zhada Eaves
#No collaborators

#PSEUDOCODE
#This Python program calculates the Veteran's disability compensation including
    #the financial compensation plus benefits (such as dental service)
#Import dictionaries for 2024 financial compensation rates
    #including any additional compensation per child
    #and a dictionary for additional benefits that are not monetary
#Prompt the user to input the number of dependent child,
    #dependent parents, and if he or she has a spouse
#If the user inputs rating 0, 10, or 20, display the benefits and calculations.
#Ask the user if they would like to learn more about the benefits on my blog post or input another rating.
#Ratings of 0, 10, or 20 have flat rates and benefits. They do not change.
#Display the calculated financial compensation rate along with benefits
#Redirect the user to my blog post about how to file a VA Disability Claim

import va_disability_dictionary #File where dictionaries are located

#Import dictionaries
compensation_table = va_disability_dictionary.compensation_table
additional_compensation = va_disability_dictionary.additional_benefits
additional_benefits = va_disability_dictionary.additional_benefits


#Function to calculate VA Compensation
def calculate_va_compensation(rating, children_under_18=0, children_over_18=0, has_spouse=False, spouse_needs_aid=False, parents=0):
    #Determine compensation using base_keys
    if children_under_18 > 0 or children_over_18 > 0:
        if has_spouse:
            if parents == 1:
                base_key = "Veteran with 1 child, spouse, and 1 parent"
            elif parents == 2:
                base_key = "Veteran with 1 child, spouse, and 2 parents"
            else:
                base_key = "Veteran with 1 child and spouse (no parents)"
        else:
            if parents == 1:
                base_key = "Veteran with 1 child and 1 parent (no spouse)"
            elif parents == 2:
                base_key = "Veteran with 1 child and 2 parents (no spouse)"
            else:
                base_key = "Veteran with 1 child only (no spouse or parents)"
    elif has_spouse:
        if parents == 1:
            base_key = "Veteran with spouse and 1 parent"
        elif parents == 2:
            base_key = "Veteran with spouse and 2 parents"
        else:
            base_key = "Veteran with spouse(no parents or children)"
    else:
        if parents == 1:
            base_key = "Veteran with 1 parent (no spouse or children)"
        elif parents == 2:
            base_key = "Veteran with 2 parents (no spouse or children)"
        else:
            base_key = "Veteran. No spouse or dependents"

    #Base compensation
    base_comp = compensation_table.get(base_key, {}).get(rating, 0)

    #Define base child compensation
    child_comp = 0

    #Add additional compensation for each additional child (excluding the first)
    if children_under_18 > 1:
        child_comp += (children_under_18 - 1) * additional_compensation["Each additional child under the age of 18"].get(rating, 0)
    if children_over_18 > 1:
        child_comp += (children_over_18 - 1) * additional_compensation["Each additional child over the age of 18 in a qualifying school program"].get(rating, 0)


    #Additional compensation for spouse requiring aid
    spouse_comp = additional_compensation["Spouse receiving aid and attendance"].get(rating, 0) if has_spouse and spouse_needs_aid else 0

    #Total compensation
    total_comp = base_comp + child_comp + spouse_comp

    return total_comp

#Function to display additional benefits
def display_benefits(rating):
    benefits = additional_benefits.get(rating, [])
    if benefits:
        print(f"Additional benefits for {rating}% rating:")
        for benefit in benefits:
            print(f"- {benefit}")
    else:
        print("No additional benefits available.")


#Main function
def main():
    #Create a loop
       while True:
        #Prompt user to input rating and other details with error handling
        while True:
            try:
                rating = int(input("What is your disability rating (Example: 30)? "))
                break  #Exit loop if valid input
            except ValueError:
                print("Please enter a valid number for the disability rating. (Example: 0 or 80)")

        has_spouse = input("Do you have a spouse? (yes/no): ").lower() == "yes"
        
        while True:
            try:
                children_under_18 = int(input("How many dependent children UNDER the age of 18 do you have? "))
                break
            except ValueError:
                print("Please enter a valid number for children under 18. (Example: 2)")

        while True:
            try:
                children_over_18 = int(input("How many dependent children OVER the age of 18 do you have? "))
                break
            except ValueError:
                print("Please enter a valid number for children over 18. (Example: 0)")

        while True:
            try:
                parents = int(input("How many of your parents depend on you (0, 1, 2)? "))
                if parents not in [0, 1, 2]:
                    raise ValueError  #Only 0, 1, or 2 are allowed
                break
            except ValueError:
                print("Please enter 0, 1, or 2 for the number of dependent parents. (The VA does not calculate more than 2.)")

        aid_attendance = input("Does your spouse require Aid & Attendance? (yes/no): ").lower() == "yes"
   

        #Calculate and display the result
        monthly_compensation = calculate_va_compensation(rating, children_under_18, children_over_18, has_spouse, aid_attendance, parents)
        print(f"\nYour estimated monthly VA compensation is: ${monthly_compensation:,.2f}")

        print("\n")
        #Display additional benefits
        display_benefits(rating)
    
        blog_link = "https://www.zhadaray.com/post/va-disability-guide"
        #Allow the user to choose whether to enter another rating or read my blog post
        next_action = input("\nWould you like to input another rating or learn more about filing a VA disability claim? (another/learn more): ").lower()

        if next_action == "learn more":
            print(f"\nGreat! You can learn more about VA disability compensation and claims here: {blog_link}")
        elif next_action == "another":
            continue  #Restart the loop
        else:
            print("\nThank you for using the VA Disability Calculator! I hope it helped.")
        break


#Call the program
if __name__ == "__main__":
    main()


