#escape from the maze problem
X = 0
Y = 0
command_string = input("Enter command string: ")
for cmd in command_string:
    if cmd == 'L':
     X -= 1 
    elif cmd == 'R':
             X += 1  
    elif cmd == 'U':
           Y += 1  
    elif cmd == 'D':
        Y -= 1
print(X, Y)
