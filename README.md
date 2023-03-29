# codility_

| :warning: WARNING          |
|:---------------------------|
|Please note that the following repository contains solutions to coding challenges, and it is highly discouraged to copy these solutions without attempting to solve the problem on your own. Additionally, please be aware that following any links provided is done at your own risk.|



## What is the purpose of the project?

It aims to capture my solutions and insights gained from completing [Codility Developer Training challenges](https://app.codility.com/programmers/lessons/).

## Tools and Technologies

- The code is written in Python.
- IDE: [Visual Studio Code](https://code.visualstudio.com/docs)  in combination with the Ubuntu distribution running on WSL2.
- Package management tool: [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Unit tests:  [pytest](https://docs.pytest.org/en/7.2.x/).
- [Mardown Tables generator](https://www.tablesgenerator.com/).
- Code autoformating: [autopep8](https://github.com/hhatto/autopep8). To read about reformating code in VSC refer to the [microsoft manual](https://learn.microsoft.com/en-us/visualstudio/python/formatting-python-code).

## FAQ
<details>
<summary>How to deal with the error message: "ModuleNotFoundError: No module named 'pytest'"? </summary>

In vscode "use the Python: Select Interpreter command from the Command Palette (Ctrl+Shift+P)" to activate interpereper of proper environements. For more information read the [vscode documentation](https://code.visualstudio.com/docs/python/environments).
</details>

<details>
<summary>"! [remote rejected] main -> main (failure) error: failed to push some refs to 'git@github.com:.git'"</summary>

  [Check wheather GitHub services are available](https://www.githubstatus.com/).
</details>

## Solutions
<details>
<summary>L12.1 ChocolatesByNumbers</summary>
  
### Task
A certain number of chocolates are arranged in a circle, and you start eating chocolates by taking specific steps around the circle. After each chocolate is eaten, it is replaced by a wrapper. You are asked to determine how many chocolates you can eat before you encounter the first wrapper by applying the Euclidean algorithm.
  
### Ideas and Solution
First thing to notice is the fact that the first wrapper encountered will be from the first eaten chocolate. Therefore, we aim to land in the start position.

Second, for the given number of chocolates L and the step increment S, the next candidate chocolate to be eaten is given by the equation `(0 + i*S) mod L`, where `i` is the current turn. This gives us an equation to solve: `(0 + i*S) mod L = 0`, which simplifies to `i*S = k*L`, where k is a positive integer. Now, there are two important constraints: `i` must be an integer value, and it also must be minimal. The only factor we can control is `k`.

We could set `k` to be equal to `S`, which would make `i` to be integer; However, it would be maximized. Instead, we aim to keep the denominator as large as possible. For that reason, assuming `S = s*gcd(S, L)`, we set `k = s`.  `i = (s*L)/(s*gcd(S, L))`, which leads to `i = L/gcd(S, L)` to be an integer and minimal.
</details>

<details>
<summary>L12.2 CommonPrimeDivisors</summary>
  
### Task
The task is to calculate the number of pairs that have the exact same set of prime factors by using either the greatest common divisor (gcd) or the least common multiple (lcm).
### Ideas and Solution
The first thing to notice is that for the given two numbers, the gcd is the product of all common prime factors for the numbers taken with the smallest power. For example, for `(2**2 * 3**11)` and `(2**4 * 3**2)`, the gcd is `(2**2 * 3**2)`.

The ideas is to "fully exclude" common factors out of the given numbers and then check if there is some uncommon part left. Devision enables us to exclude common minimum,, but there is potentially some rest left. Considert the example, `a=(2**1 * 3**2)` and `b=(2**2 * 3**1)`, then the `gcd(a,b)=(2**1 * 3**1)`, the devision by `gcd(a,b)` leaves us with `ra=3` anb `rb=2`. Even if the given numbers have common set of prime factors, we cannot conclude that yet.

To overcome this problem, we need to take an additional step and exclude the common factors between `rest`, the remainder of the division, and `gcd(a,b)` by finding the `gcd(rest, g)`. We repeat this step until the remainder is 1, which means that `gcd(a,b)` has included all the factors that were part of the number, or until `gcd(rest>1, g)` is greater than 1, which means that the original number (a and/or b) contains some uncommon factors that were not present in `gcd(a,b)`. This process must be done for both numbers.

### Conclusion
- The gcd is the product of common prime factors taken with the smallest power. 
- To completely exclude common factors "hidden" in `g=gcd(a,b)`, we need to use devision along with the gcd between the remainder of the division and g.
</details>
  
<details>
<summary>L14.2 NailingPlanks</summary>
  
### Task
The task is to determine the minimum number of nails needed to mount all the given planks according to the provided nailing sequence. You are given two lists that specify the starting and ending positions of each plank, as well as a list that specifies the order in which the planks should be nailed.

### Ideas
The goal is to use the Binary Search(BS) algorithm to optimize the solution. Here are some possible options:
A) Use BS to search for the exact number of nails required. The problem with this approach is that validating each candidate number will result in repeated calculations.
B) Use BS to find a nail that matches an interval and has the smallest position among all other nails matching the interval. Then, iterate through the nails sequentially to find the one with the smallest id.

### Conclusion
- Solution B. Score: 62%. =(
</details>
  
<details>
<summary>L15.1 AbsDistinct</summary>
  
### Task
The goal is to apply the caterpillar method to find distinct absolute value in the given sorted list of integers.
### Ideas and Solution
The Caterpillar method (CM) enables traversal of absolute values in a given list from largest to smallest, ensuring that each value is visited exactly once. CM requires two pointers (integers), which I set to point to either end of the list. In each iteration step, exactly one decision is made: whether to count the value with the largest absolute value (which I call "current") or not, if it is a duplicate. Afterward, the pointer for the current value should be adjusted.

The fact that each position is visited exactly once in descending order of absolute values means that dealing with duplicates requires only knowledge of the value of the previous "current" value.

### Example
Given the list:  [-20,5,10,20,20]

| itteration | 0    | 1  | 2   | 3   | 4  |
|------------|------|----|-----|-----|----|
| previous   | None | 20 | 20  | -20 | 10 |
| current    | 20   | 20 | -20 | 10  | 5  |
| counter    | +1   | +0 | +0  | +1  | +1 |

Result: 3

Notice, how the comparison between previous and current influences the counter. Also, the absolute values of "current" are ordered in descending order.

### Conclusion
- The Caterpillar method is a technique that can be used to traverse a sorted list of integers in descending order of absolute value.
- Each step can be abstracted as a pair of integers (a,b); In each step an integere with the biggest absolute value is changed.
</details>

<details>

<summary>L15.2 CountDistinctSlices</summary>

### Task
The objective is to use the caterpillar method to identify distinct slices, which are slices containing only unique numbers. A slice is defined as a pair of indices (a, b) where a < b.

### Ideas and Solution

To keep track of duplicates, a dictionary is used with numbers as keys and the index of their last encounter in the list as values. The dictionary is updated on each encounter. If the latest stored index for the current number is greater than the position of the current caterpillar head, then a duplicate value has been found.

The caterpillar's tail and head start at the beginning of the list. As long as no duplicates are encountered, the head keeps expanding. On encountering a duplicate, the caterpillar's tail is set to the position immediately after the previous duplicate. This ensures that any slice containing both positions with the duplicate at the same time is excluded.

To count the number of possible slices, we use an increment that is equal to the current interval length. This increment increases by one with each expansion step of the caterpillar (head movement). However, when duplicates are encountered (tail movement), the increment must be adjusted to take into account the new length of the caterpillar.

### Example

Below is an adjacency matrix M[i,j], representing slices, where each slice starts at index i and ends at index j.

|    index   |   0   |  1  |  2 |  3 |   4   |  5  |  6 |
|:----------:|:-----:|:---:|:--:|:--:|:-----:|:---:|:--:|
| input list | **2** | _3_ |  4 |  5 | **2** | _3_ |  4 |
|            |   T1  |     |    | H1 |       |     |    |
|            |       |  T2 |    |    |   H2  |     |    |
|            |       |     | T3 |    |       |     | H* |
|  increment |   +1  |  +2 | +3 | +4 |   +4  |  +4 | +5 |
|            |  j=0  |  1  |  2 |  3 |   4   |  5  |  6 |
|     i=0    |   V   |  V  |  V |  V |   X   |  X  |  X |
|      1     |   X   |  V  |  V |  V |   V   |  X  |  X |
|      2     |   X   |  X  |  V |  V |   V   |  V  |  V |
|      3     |   X   |  X  |  X |  V |   V   |  V  |  V |
|      4     |   X   |  X  |  X |  X |   V   |  V  |  V |
|      5     |   X   |  X  |  X |  X |   X   |  V  |  V |
|      6     |   X   |  X  |  X |  X |   X   |  X  |  V |

</details>

<details> 
<summary>L15.3 CountTriangles</summary>

### Task
The goal is to use the caterpillar algorithm to find the number of triangles that can be constructed from a given list of integers.

### Ideas and Solution
To form a triangle, the sum of any two sides must be greater than the third side. This is known as the triangle inequality condition. To find all valid triplets (a, b, c), we need to explore all possible values for a, b, and c.

We can determine the valid interval for b by combining the three triangle conditions into the expression abs(c - a) < b < c + a. If we limit the integers to 1 <= a <= b <= c, then the condition can be simplified to c - a < b < c + a. Since b is less than or equal to c, and a is at least 1, the condition b < a + c is always met. Therefore, we are left with the condition c - a < b.

Now, we need to decide how to traverse a, b, and c and what initial values to select. To do this, we will keep b fixed and search for suitable values of a and c. There are two cases to consider:

   1. If c - a >= b, then we can either increase a or decrease c. By setting c to be the minimum value, we only need to adjust a.

   2. If c - a < b, then any value a', such a<=a'<=b, is suitable too. Thus, we set a to be the minimum value.

By adopting this approach, we can explore all possible triplet values by fixing the middle value of b and adjusting the left and right parts of a and c.
</details>


<details> 
<summary>L15.4 MinAbsSumOfTwo</summary>

### Task
The goal is to use the caterpillar algorithm to find the smallest possible absolute value of the sum of any two elements from a given list of values.

### Ideas and Solution
The first step is to sort the given list of integers in ascending order. The head of the caterpillar points to the maximum value in the list (the last value) and the tail points to the minimum value (the first value). We only need to consider a pair of indexes once, without permutations.

Let posT and posH be the indexes of the numbers in the given list, and valT and valH be their corresponding values. Also, let `sum` be defined as the sum of valT and valH.

By looking at the matrix, one can notice that if the sum > 0 (e.g., (-10, 20)), then it is also minimal for any tail value, because valT <= valT' for posT < posT', so valT + valH < valT' + valH. Therefore we can ignore the value by moving posH one position back(exclude column).

Also, if val < 0, then because valH + valT <= valH' + valT for posT < posT', so the val is the minimal value (row), and we can ignore the rest of the values by moving the posT one position forward(exclude row).

If sum is zero, then we have found the smallest possible result.

In each step we take the minimal value.

### Example
(tail, head)
|         | **-10** | **-8** | **0** | **1** | **8** | **20** |
|:-------:|:-------:|:------:|:-----:|:-----:|:-----:|:------:|
| **-10** |   -20   |   -18  |  -10  |   -9  |   -2  |   10   |
|  **-8** |    X    |   -16  |   -8  |   -7  |   0   |   12   |
|  **0**  |    X    |    X   |   0   |   1   |   8   |   20   |
|  **1**  |    X    |    X   |   X   |   2   |   9   |   21   |
|  **8**  |    X    |    X   |   X   |   X   |   16  |   28   |
|  **20** |    X    |    X   |   X   |   X   |   X   |   40   |

</details>

<details>
<summary>L16.1 MaxNonoverlappingSegments</summary>
  
### Task
  The goal is to apply a greedy method to find the maximum number of non-overlapping segments for a given set of segments sorted by their end positions. Each segment is represented by its beginning and end positions, which are provided in two separate lists - one for beginning positions and another for end positions.

### Ideas and Solution
  
Observations:

- There may be several sets that lead to an optimal solution, and some of them may not necessarily contain the first interval (Example 1).
- Non-overlapping intervals are always a part of an optimal solution.
- Any interval with index j > i that intersects with the interval with index i also intersects with intervals with index k such that j > k > i (Example 2).
  
Initially, I declined the idea of repeatedly picking the first non-overlapping segment from the list. However, after considering possible counterexamples, I realized that the approach might work. One concern was that it seemed to always pick the first given segment, which may not necessarily be part of an optimal solution.  
  
To investigate this further, I asked whether there is always at least one set leading to an optimal solution that includes the first segment. Although it is possible for other sets not to include the first segment and still lead to an optimal solution (Example 1), the answer to the question is "yes." Suppose that neither optimal solution includes the first segment, s0. We can still take any optimal solution {s10, s55, ...} and replace the first element s10 with s0 to obtain another optimal solution {s10, s55, ...} (Contradiction). This replacement is possible because s10 and s55 do not overlap, so s55 is also not overlapping with s0, because it begins later than s10 ends, which ends earlier than s0 does, so the begin of s55 lies later that the end of s0.
  
Given that the first segment in the problem is always part of some optimal solution, we can focus on selecting subsequent non-overlapping segments to construct an optimal solution. This reduces the problem to a subproblem containing only segments that do not overlap with the first segment.To solve this subproblem, we can use the replacement argument mentioned earlier. That is, we can take any optimal solution for the subproblem and construct a new optimal solution that includes the next first non-overlapping segment.By repeatedly applying this replacement argument, we can construct an optimal solution for the entire problem. 
   
### Examples
1. [0,2][1,3][4,5]. Two optimal solutions: {[0,2],[4,5]} and {[1,3],[4,5]}
2. [0,3][4,5][1,6]. The third segement intersects the first and the second segments.
3. [0,6],[1,2],[3,4],[5,6]. Segments are ordered by there begins (wrong). Optimal solution does not include first segement.
</details>
