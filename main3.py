import random
a=['almas','appel','banana']
def spin():
    return [random.choice(a) for i in range(3)]
def check_jacpot(spin_result):
    return spin_result[0]== spin_result[1]==spin_result[2]
while 1:
    result=spin()
    print(''.join(result))
    if check_jacpot(result):
        print("win")
    game=input("makhahy edame bdahy (yes or no:)") 
    if game=="no":
        break  
