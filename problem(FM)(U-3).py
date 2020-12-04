#calculating the force on the ball

def result(cd,md,v,d,dv):
    r=cd*((md*0.785*d*d*v*v)/2)
    return r
def reynolds_number(md,v,d,dv):
    re=(md*v*d)/dv
    return re


print('calculating the Weight of body\nEnter all the values in m')
md=float(input("Enter the 'Mass Density' of the fluid: "))
v=float(input("Enter the 'Velocity' of the fluid stream: "))
d=float(input("Enter the 'Diameter' of the ball: "))
dv=float(input("Enter the 'Dynamic viscosity' of the fluid: "))


flag=0
flag=int(input("enter 1 if value of 'coffecient of drag' is give else press 0:  "))
if flag==1:
    cd=float(input("enter the value of 'Coffecient of drag': "))
    r=result(cd,md,v,d,dv)
    print('force: '+ str(r))
elif flag==0:
    re=reynolds_number(md,v,d,dv)
    print('Reynolds number: '+ str(re))
    if re<=0.2:
        cd=(24/re)
    elif 0.2<re<=5:
        cd=(24/re)(1+(0.1875/re))
    elif 5<re<=1000:
        cd=0.4
    elif 1000<re<=100000:
        cd=0.5
    elif re>100000:
        cd=0.2
    r=result(cd,md,v,d,dv)
    print('weight of the ball: '+str(r)+'N')
print('Thanks')