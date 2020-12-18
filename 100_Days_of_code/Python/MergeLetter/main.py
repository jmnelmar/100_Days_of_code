content =""

with open("./Input/Names/invited_names.txt") as file:
    lines = file.readlines()
    for line in lines:
        name = line.rstrip("\n")
        
        with open("./Input/Letters/starting_letter.docx") as file:
            content = file.read()
        content = content.replace("[name]",name)
        file2 = open(f"./Output/ReadyToSend/letter_for_{name}.docx", "w") 
        file2.write(content)
        file2.close()
        #print(content) 