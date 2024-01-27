#Modules for number generators
import random

#Functions

#Coin Toss

def coinToss():
    
    result = random.randint(1,2)
    
    if result == 1:
        
        return 'Heads'
    
    else:
        
        return 'Tails'

#Dice Roll

def diceRoll():
    
    result = random.randint(1,6)
    
    return result

#Cards

def cardShuffle():
    
    cardNumber = random.randint(1,52)
    
    deck = [
        "Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs"
        "Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades"
        "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts"
        "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds"
        ]
    
    return deck[cardNumber]

#User Input Generator

def userGenerator():
    
    print('The maximum number of outcomes for a dice roll is 6 and for a coin flip it is 2')
    
    while True:
        
        try:
    
            maxNum = int(input('Enter the maximum number outcomes for your custom generator: '))
            
            break
        
        except ValueError:
            
            print('\nOnly enter numbers!')
        
        except KeyboardInterrupt:
            
            print("\nDon't interrupt me!")
        
        except Exception as e:
            
            print(e)
    
    result = random.randint(1, maxNum)
    
    return ("\n" + str(result))
    
#Menu
menu = '''Welcome to Random Number Generator!\n
1. Coin Flip (Flips a coin once for you)
2. Dice Roll (Rolls a dice once for you)
3. Card Shuffle (A random card from a deck of 52 cards is given to you)
4. Custom Generator (Create your own odds!)
5. Exit\n
'''
#User Interaction
print(menu)
while True:
    
    while True:
    
        try:
        
            userChoice = int(input('\nEnter the number of the item you wish to choose: '))
            
            print("")
            
            if userChoice == 1:
                
                print(coinToss())
            
            elif userChoice == 2:
                
                print(diceRoll())
            
            elif userChoice == 3:
                
                print(cardShuffle())
            
            elif userChoice == 4:
                
                print(userGenerator())
            
            elif userChoice == 5:
                
                break
            
            else:
                
                raise Exception('\nNot a choice!')
            
            break
        
        except ValueError:
            
            print('\nOnly enter numbers!')
        
        except KeyboardInterrupt:
            
            print("\nDon't interrupt me!")
        
        except Exception as e:
            
            print(e)

    while True:
        
        if userChoice == 5:
            
            userContinue = 'n'
            
            break
        
        try:
        
            userContinue = input('\nWould you like to use a generator again? (y/n): ').lower() #Asks user whether they want to continue playing
            
            if userContinue == 'y':
                
                break
            
            elif userContinue == 'n':
                
                break
            
            else:
                
                raise Exception('\nOnly y or n!')
            
        except KeyboardInterrupt:
                    
                    print('\nDo not interrupt me!')
                
        except Exception as e:
            
            print(e)
    
    if userContinue == 'y':
        
        continue
    
    else:
        
        break

print('\nGoodbye!')
