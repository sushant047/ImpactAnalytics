
# Impact Analytics Coding Challenge

  

This codebase gives solution to the cascading rectangular cardboard boxes levelled on X-axis.

>**Note**: Cardboard boxes can subsume **partially or completely too**.

  
  

## rectangles (python script)

  

### Approach

- The given input is sorted on basis of *x1*, if equal then on basis of *x2*, if equal then on basis of *h*

- Input is then preprocessed by checking if the cardboard boxes are subsuming or not (single pass)

- The result is created by iterating (single pass) over the preprocessed data

  

### Time and Space Complexity

  

**Time Complexity:** O(N log N) <br/>
**Space Complexity:** O(N)

  

### Input

  

First line contains ***n*** a number that denotes the number of cardboard boxes followed by ***n*** lines where each line contains **x1**, **x2** and **h** for each cardboard box

  

**Sample Input:** (*for [(1,10,5), (7,11,6), (8,10,8)]*)

  

>3 <br/>1 10 5<br/>7 11 6<br/>8 10 8<br/>

  

**Sample Output:** (*prints to console*)

  

>[(1, 5), (7, 6), (8, 8), (10, 6), (11, 0)]

  

**Constraints:**

  

*x1*, *x2* and *h* should be in the range of INT (in general $2^{-31}$ to $2^{31}$ but depends on the machine's word size).

  

## Alternate approach

  

If the range of ***x*** (x1,x2) is pre defined and the sample size (number of cardboard boxes) is larger than the range of x then below approach is more efficient as time complexity is O(N) and space complexity is O(1).

  

- A list is maintained to store height at each integer (say '***heights***') co-ordinate of the entire range of ***x***

- Height of each co-ordinate is modified by iterating over the input (cardboard box positions). Simultaneously two variables ***start*** and ***end*** are maintained which will denote the lowest and highest index of the cardboard boxes on the number line

- Output is generated by iterating over the ***heights*** array/list whenever there is a change incurred
