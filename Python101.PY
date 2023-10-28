# First project is To create a Phone book.
# Requirements:
# Build a program that resembles a phone book, 
# so that it receives the phone number and returns the name of the owner of the number.


# 1st step: creating the phone book as a directory: 
Tele_directory= { '1111111111': "Amal",
                  '2222222222': "Mohammed",
                  '3333333333': "Khadijah",
                  '4444444444': "Abdullah",
                  '5555555555': "Rawan",
                  '6666666666': "Faisal",
                  '7777777777': "Layla"
}

# 2nd step: print the message to the user:

print("Welcome To The Phone Directory! We Are Happy To Help You!")

# 3rd step: The user is going to enter the phone number 

number = input("Please Enter the Phone Number: ")
name = Tele_directory.get(number) 

# 4th step: searching for the user number under specific conditions:

if number in Tele_directory:
    print("This phone number belongs to:" , name )
elif len(number) != 10:
    print("This is invalid number, Please try again")
else:
    print("Sorry, the number is not found, Try again")