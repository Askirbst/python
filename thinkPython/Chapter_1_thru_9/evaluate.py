import math

def eval_loop():
    last_prompt = ''
    while True:
        prompt = input("Enter a string to be evaluated\n: ")
        if prompt == 'done':
            print(eval(last_prompt))
            break
        else:
            last_prompt = prompt  
        
eval_loop()