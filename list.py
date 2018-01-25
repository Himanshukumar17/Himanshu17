Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> country =['India',1,'agf',2]
>>> country
['India', 1, 'agf', 2]
>>> len(country)
4
>>> list1=[1,2,3,4,5,6,7,8,9,10]
>>> list[1:10] [1:2:3]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list[1:10] [1:2:3]
TypeError: 'type' object is not subscriptable
>>> list1[1:10]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list[:10]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list[:10]
TypeError: 'type' object is not subscriptable
>>> list1[:8]
[1, 2, 3, 4, 5, 6, 7, 8]
>>> list1[1:2]
[2]
>>> list1[:5]
[1, 2, 3, 4, 5]
>>> list1[1:9]
[2, 3, 4, 5, 6, 7, 8, 9]
>>> list1[0:9]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list1[1:2:3]
[2]
>>> list1[1:3:5]
[2]
>>> list1[1:8:2]
[2, 4, 6, 8]
>>> list1[1:6:2]
[2, 4, 6]
>>> list1[1:5:2]
[2, 4]
>>> #In this 1 to 5 is string and last 2 number is spacing
>>> list2=[1,2,3,4,5,6,7,8,9]
>>> list1+list2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list2-list1
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list2-list1
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> 
list4=[1+2,2+3,3+5]
>>> list4
[3, 5, 8]
>>> list4=[1-2,2-3,3-5]
>>> list4
[-1, -1, -2]
>>> list4=[2*5,3*6,6*2]
>>> list4
[10, 18, 12]
>>> 
