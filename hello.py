#!/bin/python3
a1=5;
a2=50;
a3=500;

print ('a1=',a1);
print ('a2=',a2);
print ('a3=',a3);

b1=5;
b2=50;
b3=500;

print ('b1=',b1);
print ('b2=',b2);
print ('b3=',b3);

print ('a1==b1:',a1==b1);
print ('a2==b2:',a2==b2);
print ('a3==b3:',a3==b3);

a4=5;
b4=5.0;
print('a4 == b4:', a4 == b4) # a4 == b4: True
print('a4 is b4:', a4 is b4) # a4 is b4: True
print('a4+1 is b4+1:', a4+1 is b4+1) # a4+1 is b4+1: False