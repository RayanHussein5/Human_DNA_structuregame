#Asaad Husein
#101238276

#importing random
import random

#def function
#This will allow us to see if the answer of the player is that of complememnt 1 if they choose or pick option 1 in regards to the game
def complement(dna_strand,player_1):
        #input statment that asks the user the following
        answer = input(f"what is the complement of {dna_strand}? ").upper()
        #this variable has no strings
        #we will use this to create the complement of the DNA
        complement = ""
        #for loop
        for let in dna_strand:
            #if the letter A apears in the variable letter, then C will be stored in the variable complement. 
            if let == "A":
                complement = complement + "C"
            #if the letter appears as C in the variable letter, then A will be stored in teh variable complement.
            elif let == "C":
                complement = complement + "A"
            #if the letter appears as T in the variable letter, then G will be stored in the variable complement.
            elif let == "T":
                complement = complement + "G"
            #if the letter appears as G in the variable letter, then G will be stored in the variable complement
            elif let == "G":
                complement = complement + "T"
        #if the answer is equal to the complement of the DNA strip, the following will occur
        if answer == complement:
            #2 points will be added
            player_1.update_score(2)
            #print statment that will print the following
            print(f"You got the right answer, you have {player_1.score}. Play again? ")
        #if the above condition is not met, print the following
        else:
            #prints the follwoing
            print(f"That is wrong, the correct answer is {complement}. Play Again?")




def reverse(dna_strand,player_1):

    #input variable that asks the following
    answer = input(f"What is the reverse of {dna_strand}").upper()
    #this variable is assigned the reverse of the DNA strip
    reverse = dna_strand[::-1]
    #if the answer is equal to that of the reverse DNA strip, print the following
    if answer == reverse:
        #add to the points
        player_1.update_score(2)
        #print the following
        print(f"You got the right answer, you have {player_1.score}. Play again? ")
    #if the above condition is not met, print the following
    else:
        #print statemt that prints the following
        print(f"That is wrong, the correct answer is {reverse}. Play Again?")




def get_length(name):
    
        int_input = input(f"Hi {name}, please enter a positive integer for the DNA length ")
        #while loop 
        while True:
            #if statement
            #if the number given by the user is not an integer, the what comes after this if statment will not occur
         if int_input.isdigit():
                #this gets one out of the while loop
                break
            #else-statment
            #if the number is other than an integer, the following will occur
         else:
                #while loop
                while True:
                    #asks user for the integer again
                    print("Invalid input, please try again..")
                    int_input = input("Please enter an integer ")
                    #if statment
                    #if the input inputted is anything other than an integer, then this loop will not break
                    if int_input.isdigit():
                        #break, this allows us to exist the loop
                        break
        #returns int_input                
        return int_input




def display_options():
        #print statment that prints the following
        print("Select an option of [1-4] to answer a question or 5 to quit the game.\nWin the game by scoring at least 10 points! ")
        select = input("1.Complement [2 points]\t2.Reverse [2 points]\t3. Compress [3 points]\t4. Expand [3 points]\t5. Quit ")
        #input statement that prints the following
        while True:
            #if statement
            #if the number given by the user is not an integer, the what comes after this if statment will not occur
         if select.isdigit():
                #this gets one out of the while loop
                break
            #else-statment
            #if the number is other than an integer, the following will occur
         else:
                #while loop
                while True:
                    #asks user for the integer again
                    print("Invalid input, please try again..")
                    select = input("1.Complement [2 points]\t2.Reverse [2 points]\t3. Compress [3 points]\t4. Expand [3 points]\t5. Quit ")
                    #if statment
                    #if the input inputted is anything other than an integer, then this loop will not break
                    if select.isdigit():
                        #break, this allows us to exist the loop
                        break   
        
        #return select
        return select


def compressed(dna_strand,player_1):
    answer = input(f"What is the compressed of {dna_strand}").upper()
        #creating a variable called compressed
        #this will be used to store the compressed strings in the future
        #If the answer will be equal to the compressed version of "letter" then the user will get the answer right
    compressed = ""
        #variable that starts with the first letter in "letter"
        #this variable stores the first letter in the variable "letter"
    current_char = dna_strand[0]
        #variable set to zero
        #this will help us as it will keep track of how many letters there are of the same letter
    current_char_count = 0
        #for loop
    for lett in dna_strand:
            #if-statment
            #if "lett" does not equal current char, then it will not be executed
        if lett != current_char:
                #if current_char_count equals 1, then the compressed variable that had one sting will be added to. The current character will be added to it and therfore getting us closer to our goal
            if current_char_count == 1:
                compressed += current_char
                #else-statment
                #if the above condtion is not satsified then this will occur
            else:
                compressed = str(current_char_count) + current_char
                #the current character count is brought to 0
            current_char_count = 0
                #current character will be that of what lett is on. 
            current_char = lett
            #current_character count is added to by 1
            #this will eventually help us in not messing up between the letters. Ie. If I have an A, I will know when I have reached the letter G for example. 
        current_char_count += 1
        #if the current charachter count is equal to 1, then the following will occur
    if current_char_count == 1:
        compressed += current_char
        #if the above condition is not met, the follwoing will occur
    else:
            #the compressed variable will bascially have the current count which will be displayed in string, then on top of that the current character will be added, thefore, this allows us to see the follwoing for example: 3A
        compressed += str(current_char_count) + current_char

        #if answer is equal to the comperssed version of the DNA strand, do the following
    if answer == compressed:
        #add three points to points
        player_1.update_score(3)
        print(f"You got the right answer, you have {player_1.score}. Play again? ")
        #if the above condition is not met, do the following
    else:
        print(f"That is wrong, the correct answer is {compressed}. Play Again?")




def welcome():
        #print statment that prints the following
        print("Welcome to the DNA quiz game!")
        print("Select an option [1-4] to answer a question or 5 to quit the game.")
        #print statment that prints the following
        print("Win the game by scoring at least 10 points!")
        name = input("Please Enter your Username ")
        return name

def expand(dna_strand,player_1):
        #input variable
        #the .upper() in the end will allow the user to enter anything lowercase and it will switch it to upper case no matter what
    answer = input(f"What is the Decompressed version of {dna_strand}").upper()
        #variable with only one string
        #this will hold the decompressed DNA. If the answer is like the decompressed variable, then the user will get 3 points
    decompressed = ""
        #variable that equals the length of the DNA strand
    letter_length = len(dna_strand)
        #the current character is set to the first character on the string (ie. the DNA strand that the variable "letter" houses)
    current_char = dna_strand[0]
        #variable that equals zero
    current_index = 0
        #for loop in range of the lengh of the DNA strand
    for i in range(0, letter_length):
            #if statment
            #What comes after the if-statment will occur if the following condtion is met
            #if the following is a integer than the following will occur. Ie "222" and not "strign"
        if dna_strand[i].isdigit():
                #the decompresed variable is added to
                #the following calcuation is done
            decompressed += (int(dna_strand[i])-1) * dna_strand[i+1]
            #elif-statment
            #if the following character that i is assigned to (for now) is not an integer (ie. 344), then the following will occur
        elif not dna_strand[i].isdigit():
                #decompressed is added to by the current letter which is encomed by i (ie. 
            decompressed += dna_strand[i]
            #this variable will be equal to a character
        current_char = dna_strand[i]
        #if answer is equal to the comperssed version of the DNA strand, do the following
    if answer == decompressed:
        #add three points to points
        player_1.update_score(3)
        print(f"You got the right answer, you have {player_1.score}. Play again? ")
    #if the above condition is not met, do the following
    else:
        print(f"That is wrong, the correct answer is {decompressed}. Play Again?")


class DNA:

    def __init__(self,length,strand=""):
            self.length=length
            self.strand=strand
       
        
    
    def generate_dna(self,length):
        length_of_dna = int(length) + 1
        four_letter = ["A", "T", "C", "G"]
        #setting this varible to have an empty string.
        #This will be used to help ge
        letter = ""
        #for loop
        #this loop will allow us to generage dna that is 5 letters long
        for i in range(1, length_of_dna,1):
            #this will generate a randam letter that is of the list four_letter
            letters = random.choice(four_letter)
                #as the loop repeats, the letter will be added until the final DNA is created
            letter += letters
        self.strand=letter


class Player:
    def __init__(self,name,score):
            self.name=name
            self.score=score
        

    def update_score(self,new_score):
        self.score+=new_score


def main():
    name = welcome()
    length_of_dna = int(get_length(name))
    dna_1= DNA(length_of_dna)
    player_1 = Player(name,0)
    
    while True:
        dna_1.generate_dna(dna_1.length)
        options = int(display_options())
        if options == 1:
            complement(dna_1.strand,player_1)
        elif options == 2:
            reverse(dna_1.strand,player_1)
        elif options == 3:
            compressed(dna_1.strand,player_1)
        elif options == 4:
            expand(dna_1.strand,player_1)
        elif options == 5:
            if player_1.score >= 10:
                print("Great Job "+ player_1.name + " you won the game with " + str(player_1.score) + "points! Congrats!",)
            else:
                print("you lose the game " +player_1.name)
            break
            
        

main()