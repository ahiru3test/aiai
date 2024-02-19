import random
n1,n2=random.randint(1,10),random.randint(1,10)
c=input(f"My number is {n1}. Your number is High:(Push 6) or Low:(Push 4) ? : ")
print(f"Your choice is {'Low' if c=='4' else 'High'}. Your number is {n2}.")
print("You win!" if (c=="6" and n1<n2) or (c=="4" and n1>n2) else "You lose...")
