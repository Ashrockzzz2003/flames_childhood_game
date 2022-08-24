import time

def remove_common_letters(name_1, name_2):
    for i in range(len(name_1)):
        for j in range(len(name_2)):
            if(name_1[i] == name_2[j]):
                x = name_1[i]
                name_1.remove(x)
                name_2.remove(x)
                common = name_1 + ["_"] + name_2
                return [common, True]
    
    #Nothing in common
    common = name_1 + ["_"] + name_2
    return [common, False]

# Driver Code

flag = 1

while(flag == 1):

    print("\nWelcome to FLAMES!\n")

    name_1 = str(input("Person 1 name: "))
    name_2 = str(input("Person 2 name: "))

    #Format Name 1
    name_1 = name_1.lower()
    name_1.replace(" ", "")

    name_1 = list(name_1)

    #Format Name 2
    name_2 = name_2.lower()
    name_2.replace(" ", "")

    name_2 = list(name_2)

    flag = True

    while flag: # While there are common letters to be removed
        common_return = remove_common_letters(name_1, name_2)
        common_return_list = common_return[0]
        flag = common_return[1]

        #Identify Separator
        sep_index = common_return_list.index("_")

        #Slice List
        name_1 = common_return_list[:sep_index]
        name_2 = common_return_list[sep_index+1:]

    count = len(name_1) + len(name_2) # Key to Relationship Status

    # FLAMES
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(flames) > 1:
        split_index = ((count % len(flames)) - 1)

        if(split_index >= 0):
            right = flames[split_index+1:]
            left = flames[:split_index]

            flames = right + left
        else:
            flames = flames[:len(flames) - 1]

    print("Relationship Status:", flames[0])

    flag_value = False
    while(flag_value == False):
        flag = int(input("\nDo you want to try out more people?\n[Yes -> 1, No ->0]"))
        if(flag != 0 and flag != 1):
            print("INVALID Choice!. Enter either 1 or 0!!")
            flag_value = False
        else:
            flag_value = True

print("\nDeveloped by,\nAshwin Narayanan S")
time.sleep(3)