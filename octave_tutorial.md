A = [1, 2; 3, 4; 5, 6]
A =

   1   2
   3   4
   5   6

>> size(A)
ans =

   3   2

>> sz = size(A)
sz =

   3   2

>> size(sz)
ans =

   1   2

>> size(A, 1)
ans =  3
>> v = [1 2 3 4]
v =

   1   2   3   4

>> length(v)
ans =  4
>> length(A)
ans =  3
>> pwd
ans = E:\Tools\octave\octave-4.4.1-w64\octave-4.4.1-w64
>> cd 'c:\Users\Loqx\Desktop'
>> pwd
ans = c:\Users\Loqx\Desktop
>> cd 'c:\Users\Loqx\Desktop\ex1'
>> ls
 Volume in drive C has no label.
 Volume Serial Number is 18E2-DF5C

 Directory of c:\Users\Loqx\Desktop\ex1

[.]                      ex1data2.txt             normalEqn.m
[..]                     ex1_multi.m              plotData.m
computeCost.m            featureNormalize.m       submit.m
computeCostMulti.m       gradientDescent.m        warmUpExercise.m
ex1.m                    gradientDescentMulti.m
ex1data1.txt             [lib]
              13 File(s)         18,692 bytes
               3 Dir(s)  179,356,258,304 bytes free
>> who
Variables in the current scope:

A    I    V    a    ans  sz   v    w

>> load ex1data1.txt
>> who
Variables in the current scope:

A         I         V         a         ans       ex1data1  sz        v         w

>> ex1data1
ex1data1 =

    6.11010   17.59200
    5.52770    9.13020
    8.51860   13.66200
    7.00320   11.85400
    5.85980    6.82330
    8.38290   11.88600
    7.47640    4.34830
    8.57810   12.00000
    6.48620    6.59870
    5.05460    3.81660
    5.71070    3.25220
   14.16400   15.50500
    5.73400    3.15510
    8.40840    7.22580
    5.64070    0.71618
    5.37940    3.51290
    6.36540    5.30480
    5.13010    0.56077
    6.42960    3.65180
    7.07080    5.38930
    6.18910    3.13860
   20.27000   21.76700
    5.49010    4.26300
    6.32610    5.18750
    5.56490    3.08250
   18.94500   22.63800
   12.82800   13.50100
   10.95700    7.04670
   13.17600   14.69200
   22.20300   24.14700
    5.25240   -1.22000
    6.58940    5.99660
    9.24820   12.13400
    5.89180    1.84950
    8.21110    6.54260
    7.93340    4.56230
    8.09590    4.11640
    5.60630    3.39280
   12.83600   10.11700
    6.35340    5.49740
    5.40690    0.55657
    6.88250    3.91150
   11.70800    5.38540
    5.77370    2.44060
    7.82470    6.73180
    7.09310    1.04630
    5.07020    5.13370
    5.80140    1.84400
   11.70000    8.00430
    5.54160    1.01790
    7.54020    6.75040
    5.30770    1.83960
    7.42390    4.28850
    7.60310    4.99810
    6.33280    1.42330
    6.35890   -1.42110
    6.27420    2.47560
    5.63970    4.60420
    9.31020    3.96240
    9.45360    5.41410
    8.82540    5.16940
    5.17930   -0.74279
   21.27900   17.92900
   14.90800   12.05400
   18.95900   17.05400
    7.21820    4.88520
    8.29510    5.74420
   10.23600    7.77540
    5.49940    1.01730
   20.34100   20.99200
   10.13600    6.67990
    7.33450    4.02590
    6.00620    1.27840
    7.22590    3.34110
    5.02690   -2.68070
    6.54790    0.29678
    7.53860    3.88450
    5.03650    5.70140
   10.27400    6.75260
    5.10770    2.05760
    5.72920    0.47953
    5.18840    0.20421
    6.35570    0.67861
    9.76870    7.54350
    6.51590    5.34360
    8.51720    4.24150
    9.18020    6.79810
    6.00200    0.92695
    5.52040    0.15200
    5.05940    2.82140
    5.70770    1.84510
    7.63660    4.29590
    5.87070    7.20290
    5.30540    1.98690
    8.29340    0.14454
   13.39400    9.05510
    5.43690    0.61705

>> size(ex1data1)
ans =

   97    2

>> load ex1data2.txt
>> size(ex1data2)
ans =

   47    3

>> whos
Variables in the current scope:

   Attr Name          Size                     Bytes  Class
   ==== ====          ====                     =====  =====
        A             3x2                         48  double
        I             6x6                         48  double
        V             1x3                         24  double
        a             1x1                          8  double
        ans           1x2                         16  double
        ex1data1     97x2                       1552  double
        ex1data2     47x3                       1128  double
        sz            1x2                         16  double
        v             1x4                         32  double
        w             1x10                        80  double

Total is 399 elements using 2952 bytes

>> v = exadata1(1:10)
error: 'exadata1' undefined near line 1 column 5
>> v = ex1data1(1:10)
v =

   6.1101   5.5277   8.5186   7.0032   5.8598   8.3829   7.4764   8.5781   6.4862   5.0546

>> whos
Variables in the current scope:

   Attr Name          Size                     Bytes  Class
   ==== ====          ====                     =====  =====
        A             3x2                         48  double
        I             6x6                         48  double
        V             1x3                         24  double
        a             1x1                          8  double
        ans           1x2                         16  double
        ex1data1     97x2                       1552  double
        ex1data2     47x3                       1128  double
        sz            1x2                         16  double
        v             1x10                        80  double
        w             1x10                        80  double

Total is 405 elements using 3000 bytes

>> save hello.txt v
>> clear\
warning: using continuation marker \ outside of double quoted strings is deprecated and will be r
emoved from a future version of Octave, use ... instead

>> clear
>> whos
>> who
>> load hello.txt
>> whos
Variables in the current scope:

   Attr Name        Size                     Bytes  Class
   ==== ====        ====                     =====  =====
        v           1x10                        80  double

Total is 10 elements using 80 bytes

>> save hello.txt v -ascii
>> A = [1 2; 3 4; 5 6]
A =

   1   2
   3   4
   5   6

>> A_32=A(3,2)
A_32 =  6
>> A(2,:)
ans =

   3   4

>> A(:,2)
ans =

   2
   4
   6

>> A([1, 3], :)
ans =

   1   2
   5   6

>> A(:, 2) = [10; 11; 12]
A =

    1   10
    3   11
    5   12

>> A = [A, [100, 101, 102]]
error: horizontal dimensions mismatch (3x2 vs 1x3)
>> A = [A, [100; 101; 102]];
>> AS
error: 'AS' undefined near line 1 column 1
>> A
A =

     1    10   100
     3    11   101
     5    12   102

>> A(:) % put all elements of A into a single vector
ans =

     1
     3
     5
    10
    11
    12
   100
   101
   102

>> A = [1,2; 3, 4; 5, 6];
>> B = [11, 12; 13, 14; 15, 16];
>> C = [A B]
C =

    1    2   11   12
    3    4   13   14
    5    6   15   16

>> C = [A; B]
C =

    1    2
    3    4
    5    6
   11   12
   13   14
   15   16

>> C = [B, A]
C =

   11   12    1    2
   13   14    3    4
   15   16    5    6

>>
