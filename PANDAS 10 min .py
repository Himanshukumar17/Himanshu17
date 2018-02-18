Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> 
>>> s = pd.Series([1,3,5,np.nan,6,8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> dates = pd.date_range('20130101', periods=6)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
>>> dates = pd.date_range('20130101', periods=10)
>>> dates
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06', '2013-01-07', '2013-01-08',
               '2013-01-09', '2013-01-10'],
              dtype='datetime64[ns]', freq='D')
>>> df2 = pd.DataFrame({ 'A' : 1.,
			 'B' : pd.Timestamp('20130102'),
			 'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
			 'D' : np.array([3] * 4,dtype='int32'),
			 'E' : pd.Categorical(["test","train","test","train"]),
			 'F' : 'foo' })
>>> df2
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df2.dtypes
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
>>> df.head(10)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    df.head(10)
NameError: name 'df' is not defined
>>> df2.head(10)
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df.tail(6)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    df.tail(6)
NameError: name 'df' is not defined
>>> df2.tail(6)
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
>>> df.index
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    df.index
NameError: name 'df' is not defined
>>> df2.index
Int64Index([0, 1, 2, 3], dtype='int64')
>>> df2.columns
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
>>> df2.values
array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']],
      dtype=object)
>>> df2.describe()
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
>>> df2.describe(10)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    df2.describe(10)
  File "C:\Users\Himanshu\AppData\Local\Programs\Python\Python36-32\lib\site-packages\pandas\core\generic.py", line 6755, in describe
    percentiles = list(percentiles)
TypeError: 'int' object is not iterable
>>> df2.describe()
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
>>> 
KeyboardInterrupt
>>> df2.T
                     0                    1                    2  \
A                    1                    1                    1   
B  2013-01-02 00:00:00  2013-01-02 00:00:00  2013-01-02 00:00:00   
C                    1                    1                    1   
D                    3                    3                    3   
E                 test                train                 test   
F                  foo                  foo                  foo   

                     3  
A                    1  
B  2013-01-02 00:00:00  
C                    1  
D                    3  
E                train  
F                  foo  
>>> df.sort_index(axis=1, ascending=False)

