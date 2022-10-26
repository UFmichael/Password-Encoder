# Written by Michael Yao
# last modified 10-26-2022

running = True

def encode(password):
  password = str(password)
  for i in range(len(password)):
    if (int(password[i])+3) < 10:
      password[i] = password[i] + 3
    else:
      password[i] = password[i] - 7

def decode(password):
  password = str(password)
  for i in range(len(password)):
    if (int(password[i])-3) >= 0:
      password[i] = password[i] - 3
    else:
      password[i] = password[i] + 7

while running:
  print("Menu")  
  print("-------------") 
  print("1. Encode")  
  print("2. Decode")  
  print("3. Quit") 
  
  choice = input("Please enter an option: ")  
  
  if choice == 1:
    password = input("Please enter your password to encode: ") # 12345555 
    password = password + 1
    print("Your password has been encoded and stored!")
  elif choice == 2:
    password_u = password
    print(f"The encoded password is {password}, and the original password is {password_u}")  
  else:
    running = False
