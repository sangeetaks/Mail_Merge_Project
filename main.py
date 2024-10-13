#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f = open("Input/Names/invited_names.txt", "r")
list_of_names = f.readlines(-1)
for i in list_of_names:
    x = i.strip()
    file = open(f"Output/ReadyToSend/Angela_invite_{x}", "w")
    file.write(f"Dear {x},\nYou are invited to my birthday this Saturday.\nHope you can make it!\nSangeeta")
