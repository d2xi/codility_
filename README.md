# codility_
## What is the purpose of the project?

It aims to capture my solutions and insights gained from completing Codility Developer Training challenges.

## Tools and Technologies

- The code is written in Python.
- IDE: [Visual Studio Code](https://code.visualstudio.com/docs)  in combination with the Ubuntu distribution running on WSL2.
- Package management tool: [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Unit tests:  [pytest](https://docs.pytest.org/en/7.2.x/).
- [Mardown Tables generator](https://www.tablesgenerator.com/)

## FAQ

### How to deal with the error message: "ModuleNotFoundError: No module named 'pytest'"?
In vscode "use the Python: Select Interpreter command from the Command Palette (Ctrl+Shift+P)" to activate interpereper of proper environements.

For more information read the [vscode documentation](https://code.visualstudio.com/docs/python/environments).

# Solutions
## L12.1 ChocolatesByNumbers 
### Task
A certain number of chocolates are arranged in a circle, and you start eating chocolates by taking specific steps around the circle. After each chocolate is eaten, it is replaced by a wrapper. You are asked to determine how many chocolates you can eat before you encounter the first wrapper by applying the Euclidean algorithm.
### Ideas and Solution
First thing to notice is the fact that the first wrapper encountered will be from the first eaten chocolate. Therefore, we aim to land in the start position.

Second, for the given number of chocolates L and the step increment S, the next candidate chocolate to be eaten is given by the equation `(0 + i*S) mod L`, where `i` is the current turn. This gives us an equation to solve: `(0 + i*S) mod L = 0`, which simplifies to `i*S = k*L`, where k is a positive integer. Now, there are two important constraints: `i` must be an integer value, and it also must be minimal. The only factor we can control is `k`.

We could set `k` to be equal to `S`, which would make `i` to be integer; However, it would be maximized. Instead, we aim to keep the denominator as large as possible. For that reason, assuming `S = s*gcd(S, L)`, we set `k = s`.  `i = (s*L)/(s*gcd(S, L))`, which leads to `i = L/gcd(S, L)` to be an integer and minimal.

## L12.2 CommonPrimeDivisors
### Task
The task is to calculate the number of pairs that have the exact same set of prime factors by using either the greatest common divisor (gcd) or the least common multiple (lcm).
### Ideas and Solution
The first thing to notice is that for the given two numbers, the gcd is the product of all common prime factors for the numbers taken with the smallest power. For example, for `(2**2 * 3**11)` and `(2**4 * 3**2)`, the gcd is `(2**2 * 3**2)`.

The ideas is to "fully exclude" common factors out of the given numbers and then check if there is some uncommon part left. Devision enables us to exclude common minimum,, but there is potentially some rest left. Considert the example, `a=(2**1 * 3**2)` and `b=(2**2 * 3**1)`, then the `gcd(a,b)=(2**1 * 3**1)`, the devision by `gcd(a,b)` leaves us with `ra=3` anb `rb=2`. Even if the given numbers have common set of prime factors, we cannot conclude that yet.

To overcome this problem, we need to take an additional step and exclude the common factors between `rest`, the remainder of the division, and `gcd(a,b)` by finding the `gcd(rest, g)`. We repeat this step until the remainder is 1, which means that `gcd(a,b)` has included all the factors that were part of the number, or until `gcd(rest>1, g)` is greater than 1, which means that the original number (a and/or b) contains some uncommon factors that were not present in `gcd(a,b)`. This process must be done for both numbers.

### Conclusion
- The gcd is the product of common prime factors taken with the smallest power. 
- To completely exclude common factors "hidden" in `g=gcd(a,b)`, we need to use devision along with the gcd between the remainder of the division and g.

## L14.2  NailingPlanks
### Task
The task is to determine the minimum number of nails needed to mount all the given planks according to the provided nailing sequence. You are given two lists that specify the starting and ending positions of each plank, as well as a list that specifies the order in which the planks should be nailed.

### Ideas
The goal is to use the Binary Search(BS) algorithm to optimize the solution. Here are some possible options:
A) Use BS to search for the exact number of nails required. The problem with this approach is that validating each candidate number will result in repeated calculations.
B) Use BS to find a nail that matches an interval and has the smallest position among all other nails matching the interval. Then, iterate through the nails sequentially to find the one with the smallest id.

### Conclusion
- Solution B. Score: 62%. =(

## L15.1 AbsDistinct
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
