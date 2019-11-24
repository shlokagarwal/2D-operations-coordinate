import matplotlib.pyplot as plt  
import math
print('Enter space separated initial coordinates. For example x=6 and y=9, type 6,9')

a,b = input().split(',')
a=int(a)
b=int(b)

A = [[a, b, 1]] 
result = [[0, 0, 0]] 

print('Which operation do you want to do on this coordinate?\n1.Translation\n2.Scaling\n3.Rotation about X-axis(Anti-Clockwise)\n4.Rotation about Y-axis(Anti-Clockwise)\n5.Rotation about Z-axis(Anti-Clockwise)\n6.Reflection about X-axis\n7.Reflection about Y-axis\n')

choice = input()
choice = int(choice)
if(choice==1):
    print('Enter Tx and Ty (comma separated)\n')
    tx,ty = input().split(',')
    tx=int(tx)
    ty=int(ty)
    B = [[1, 0, 0], 
         [0, 1, 0], 
         [tx, ty, 1]] 
elif(choice ==2):
    print('Enter Sx and Sy (comma separated)\n')
    sx,sy = input().split(',')
    sx=int(sx)
    sy=int(sy)
    B = [[sx, 0, 0], 
         [0, sy, 0], 
         [0, 0, 1]]
elif(choice == 3):
    print('Enter theta in degrees')
    theta = input()
    theta = int(theta)
    cos = math.cos(math.radians(theta))
    sin = math.sin(math.radians(theta))
    B = [[1, 0, 0], 
         [0, cos, sin], 
         [0, float(-1*sin), cos]]
elif(choice == 4):
    print('Enter theta in degrees')
    theta = input()
    theta = int(theta)
    cos = math.cos(math.radians(theta))
    sin = math.sin(math.radians(theta))
    B = [[cos, 0, float(-1*sin)], 
         [0, 1,0], 
         [sin, 0, cos]]
elif(choice == 5):
    print('Enter theta in degrees')
    theta = input()
    theta = int(theta)
    cos = math.cos(math.radians(theta))
    sin = math.sin(math.radians(theta))
    B = [[cos, sin, 0], 
         [float(-1*sin), cos,0], 
         [0, 0, 1]]    
elif(choice ==6):
    B = [[1, 0, 0], 
         [0, -1, 0], 
         [0, 0, 1]] 
elif(choice ==7):
    B = [[-1, 0, 0], 
         [0, 1, 0], 
         [0, 0, 1]]     
else:
    print('Please try again.')    
    
  
# iterating by row of A 
for i in range(len(A)): 
  
    # iterating by coloum by B  
    for j in range(len(B[0])): 
  
        # iterating by rows of B 
        for k in range(len(B)): 
            result[i][j] += A[i][k] * B[k][j] 
  

c = result[0][0]
d = result[0][1]    
print('The new points are x='+str(c)+' and y='+str(d))


plt.title('Old -> Red, New -> Blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.scatter(a,b,color='red')
plt.grid(True)
plt.scatter(c,d,color='blue')
plt.show()