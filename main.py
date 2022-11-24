#1. Are you there? We’ve opened up a communications link to The Fender‘s secret computer. We need you to write a program that will read in the compromised usernames and passwords that are stored in a file called "passwords.csv".
#First import the CSV module, since we’ll be needing it to parse the data.
#2. We need to create a list of users whose passwords have been compromised, create a new list and save it to the variable compromised_users.
#3. Next we’ll need you to open up the file itself. Store it in a file object called password_file.
import csv
import json
compromised_users = []
with open('passwords.csv') as password_file:
#4. Pass the password_file object holder to our CSV reader for parsing. Save the parsed csv.DictReader object as password_csv.
  password_csv = csv.DictReader(password_file)
# #5. Now we’ll want to iterate through each of the lines in the CSV.
# # Create a for loop and save each row of the CSV into the temporary variable password_row.
# # 6. Inside your for loop, print out password_row['Username']. This is the username of the person whose password was compromised.
# Run your code, do you see a list of usernames?
  for password_row in password_csv:
    compromised_users.append(password_row['username'])
#Remove the print statement. We want to add each username to the list of compromised_users. Use the list’s .append() method to add the username to compromised_users instead of printing them.
#
with open('compromised_users.txt', 'w') as compromised_user_file:
   for compromised_user in compromised_users:
     compromised_user_file.write(compromised_user)
#Notifying the Boss
# 12. Your boss needs to know that you were successful in retrieving that compromised data. We’ll need to send him an encoded message over the internet. Let’s use JSON to do that.
# First we’ll need to import the json module.
# 13. Open a new JSON file in write-mode called boss_message.json. Save the file object to the variable boss_message.
# 14. Create a Python dictionary object within your with statement that relays a boss message. Call this boss_message_dict.
# Give it a "recipient" key with a value "The Boss".
# Also give it a "message" key with the value "Mission Success".
# 15. Write out boss_message_dict to boss_message using json.dump().
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
  json.dump(boss_message_dict, boss_message)
#16. Now that we’ve safely recovered the compromised users we’ll want to remove the "passwords.csv" file completely.
# Create a new with block and open "new_passwords.csv" in write-mode. Save the file object to a variable called new_passwords_obj.

# 17. Enemy of the people, Slash Null, is who we want The Fender to think was behind this attack. He has a signature, whenever he hacks someone he adds this signature to one of the files he touches.
with open('new_password.csv', 'w') as new_password_obj:
  slash_null_sig = """
_  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
_  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \
) __ (/    \( (__  )  (  ) _)  ) D (
\_)(_/\_/\_/ \___)(__\_)(____)(____/
        ____  __     __   ____  _  _
___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
__ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  """

#18. Write slash_null_sig to new_passwords_obj. Now we have the file to replace passwords.csv with!
# 19. What an incredible success! We’ll take care of moving the new passwords file over the old one in case you want to practice hacking The Fender in the future.
  new_password_obj.write(slash_null_sig)
  
  
      