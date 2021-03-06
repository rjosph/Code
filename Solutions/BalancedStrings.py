'''
Problem Statement 	
The instability of a string is the number of pairs of consecutive characters that are distinct. For example, the instability of "aafcccca" is 3
and the instability of "aaaaaaaaa" is 0. The total instability of a sequence of strings is the sum of instabilities of the individual strings.
The similarity between two strings s1 and s2 is the number of pairs of equal characters. In other words, it is the number of pairs of indices (i,j) such that s1[i] = s2[j]. 
For example, the similarity between "aaaabc" and "xba" is 5 and the similarity between "xxx" and "xxxx" is 12.


The total similarity of a sequence of M strings is computed as follows: For each of the M*(M-1)/2 possible pairs of strings you compute the similarity between them, 
and then you sum those M*(M-1)/2 numbers.

Limak needs some balance in his life. He asked you to find a sequence of exactly N strings satisfying the following conditions:

The total instability of the sequence is equal to the total similarity of the sequence.
Each string contains between 1 and 100 characters, inclusive.
Each string contains only lowercase English letters ('a' - 'z').
For the given constraints a solution always exists. If there are many solutions, you may return any one of them.

 
Definition
Class:	BalancedStrings
Method:	findAny
Parameters:	int
Returns:	String[]
Method signature:	String[] findAny(int N)
(be sure your method is public)
    
 
Constraints
-	N will be between 1 and 100, inclusive.
 
Examples:
0)	3
Returns: {"eertree", "topcoder", "arena" }
We have:
instability("eertree") = 4
instability("topcoder") = 7
instability("arena") = 4
Thus, the total instability is 4 + 7 + 4 = 15. 

We also have:
similarity("eertree","topcoder") = 7
similarity("eertree","arena") = 6
similarity("topcoder","arena") = 2
Thus, the total similarity is 7 + 6 + 2 = 15, which is the same as the total instability.

1)	4
Returns: {"hello", "little", "polar", "bear" }
In the provided answer, the total instability and the total similarity are both equal to 14.

2)	5
Returns: {"abbbbbbbbbbbbczaaaaaao", "c", "zz", "c", "xxxyyyzvvv" }
Note that the returned sequence may contain multiple copies of the same string. Each of those is counted separately.

3)	1
Returns: {"kkkkkkkkkkkkkkkkkkk" }

4)	10
Returns: 
{"asdflkjhsdfsfffkdhjfdlshlfds",
"pudelek",
"xo",
"xo",
"mnbvmnmbbr",
"plox",
"qqwwrrttyyy",
"you",
"are",
"awesome" }

'''



