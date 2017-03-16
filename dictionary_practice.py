#Module 6, Part 5: Practice with dictionaries here


my_phonebook={"Statue of Liberty":2125555555, "Ghostbusters":2125551234}

###
#Assign the value of the Statue of Liberty's phone number to the variable, num
###
num = my_phonebook["Statue of Liberty"]
###
#Print the variable, num
###
print(str(num))
###
#Change the value of the Ghostbusters' phone number to 2125559876
###
my_phonebook["Ghostbusters"] = 2125559876
#Here's an empty dictionary
your_phonebook={}

###
#Add 5 values to it like this
#your_phonebook['key']=value
###
your_phonebook["Police"]=100
your_phonebook["Ambulance"]=101
your_phonebook["FireFighters"]=102
your_phonebook["George"]=324
your_phonebook["Meet"]=345
###
#Use the keys() method: your_phonebook.keys()
#It will produce a sequence of all the keys

#Loop over this sequence with a for loop
#using syntax like

#for key in sequence_of_keys :
#    #Do stuff

#Use the loop to print to the shell the key and value
#of every element in the dictionary
###
for key in your_phonebook.keys():
    print(key+" : "+str(your_phonebook[key]))
    
