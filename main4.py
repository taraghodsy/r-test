import random 
user=input("sang,kaghaz,ghechi")
cpu1=['sang','kaghaz','ghechi']
cpu=random.choices(cpu1)
cpu_score=0
user_score=0
print("cpu=",cpu)
print("user=",user)
if cpu=="sang" or user=="ghechi" or cpu=="kaghaz" or user=="sang" or cpu=="ghechi" or user=="kaghaz":
    print("cpu win")
    cpu_score+=1
    print("cpu_score",cpu_score)
elif user=="sang" or cpu=="ghechi" or user=="kaghaz" or cpu=="sang" or user=="ghechi" or cpu=="kaghaz":
    print("cpu win")
    user_score+=1
    print("user_score",user_score)
else:
    print("msavi")    
      


