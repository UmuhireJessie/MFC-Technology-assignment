print('-Find the root of function f(x)= 4x²+10x+6, and also plot its graph.')
print('solution')

#Defining the fuction and it variables; x,a,b, and c
def f(x,a,b,c):
        return a*(x)**2+b*(x)+c

print('-The function f(x) is a qudratic equation hence the form: f(x)= ax²+bx+c',
      '-So, to proceed with the calculation, first enter the value of a, b, c from the function f(x)')

#User entering the values of a,b, and c to get the function
a = input( "Enter the value of a")
a = int(a)
b = input( "Enter the value of b")
b = int(b)
c = input( "Enter the value of c")
c = int(c)
print('-Therefore, the values of a,b, and c are:')
print(f'a= {a}')
print(f'b= {b}')
print(f'c= {c}')
print('-Let us find the roots of f(x) by first finding delta',
      '-By formula delta= b²-4ac')
delta = (b*b) - (4*a*c)
delta =int(delta)
print(f'So, delta is {delta}')

import cmath
sqrtdelta= cmath.sqrt(delta)
print(f'The squareroot of delta is {sqrtdelta}')

if delta > 0:
    print(" We have two real roots of the function which are", "x1 = ((-b + sqrtdelta) / (2a))",
    "x2 = ((-b - sqrtdelta) / (2a)))")
    x1 = ((-b + sqrtdelta) / (2 * a))
    x2 = ((-b - sqrtdelta) / (2 * a))
    print('So,', f'x1= {x1}', f'x2= {x2}')

    print('-Let us find the intercept of the function f(x)')
    print('-The x-intercept will be:', f'x-intercept:{(x1,0) , (x2,0)}')
    print("-The y-intercept (i.e x=0) will be:")
    print(f'y-intercept:{0,(a*(0**2) + b*0 + c)}')
    print('-let us find the the vertex (or turning point) of the graph')

    # We can first define the vertex of the graph or the turning point
    print('-The vertex, V, will have have coordinates (Xv,Yv), where:',
          'Xv = -b/2a',
          'Yv = f(Xv) = f(-b/2a)')
    Xv = (-b / 2 * a)
    Yv = (a * ((-b / 2 * a) ** 2) + b * (-b / 2 * a) + c)
    print('Then:')
    V = (print(f'vertex= {Xv, Yv}'))
    print('-After finding the all necessary things to understand the process, we can use python (a tool) to graph the solution')


    import numpy as np
    import matplotlib.pyplot as plt

    xvals = np.linspace(-30, 30, num=1000) #means -30 to 30 with 1000 values in between
    yvals = f(xvals, a, b, c)

    plt.figure(dpi=500)
    plt.plot(xvals, yvals)
    plt.title('graph of equation f(x)= 4x²+10x+6')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.show()

elif delta == 0:
    print(" The roots of the functions are real and same roots")
    print(f'x1=x2={(-b / (2 * a))}')

else:
    print("The function does not have the root in real numbers")

