# mini game "Magic ball"
import random
answer = ["Undoubtedly", "Without any doubts", "Definitely yes", "It's a foregone conclusion", "You can be sure of it", "I think so", "Most likely", "Good prospects", "The signs say yes", "Yes", "Not sure yet, try again", "Ask later", "Better not tell", "Can't predict right now", "Concentrate and ask again", "Do not even think", "My answer is no", "According to my information, no", "Prospects are not very good", "Highly doubtful", "Google to help you"]

print("Hey! I am a magic ball, and I will help you answer your questions!", "Let's start...", sep='\n')

# Main program loop
while True:
    question = input("Ask a question in such a way that the answer is only 'yes' or 'no'! Enter your question: ")
    print(random.choice(answer))
    again = input("Would you like to ask one more question? y - 'yes', n - 'no' ")
    if again.lower() == 'y':
        continue
    else:
        print("Come back if you have any questions! See you '🔮'")
        break
        
    
    
