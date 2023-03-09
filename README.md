# codility_
## What is the purpose of the project?

It aims to capture my solutions and insights gained from completing Codility Developer Training challenges.

## Tools and Technologies

- The code is written in Python.
- IDE: [Visual Studio Code](https://code.visualstudio.com/docs)  in combination with the Ubuntu distribution running on WSL2.
- Package management tool: [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Unit tests:  [pytest](https://docs.pytest.org/en/7.2.x/).

## FAQ

### How to deal with the error message: "ModuleNotFoundError: No module named 'pytest'"?
In vscode "use the Python: Select Interpreter command from the Command Palette (Ctrl+Shift+P)" to activate interpereper of proper environements.

For more information read the [vscode documentation](https://code.visualstudio.com/docs/python/environments).

# Solutions
## L12.1 ChocolatesByNumbers 
### Task
A certain number of chocolates are arranged in a circle, and you start eating chocolates by taking specific steps around the circle. After each chocolate is eaten, it is replaced by a wrapper. You are asked to determine how many chocolates you can eat before you encounter the first wrapper.
### Ideas
A) Rememmber where the wrappers are; on each step check if there is already one.

B) Find an application of the Euclidean algorithm.

#### B
First thing to notice is the fact that the first wrapper encountered will be from the first eaten chocolate. Therefore, we aim to land in the start position.

Second, for the given number of chocolates L and the step increment S, the next candidate chocolate to be eaten is given by the equation (0 + i*S) mod L, where i is the current turn.

This gives us an equation to solve: (0 + iS) mod L = 0, which simplifies to iS = k*L, where k is a positive integer.

Now, there are two important constraints: i must be an integer, and i must be minimal. The only factor we can control is k.

We could set k to be equal to S, which would make i to be integer. However, i would be maximized, instead, we aim to keep the denominator as large as possible. For that reason, assuming S = s*gcd(S, L), we set k = s.  i = (sL)/(sgcd(S, L)), which leads to i = L/gcd(S, L) to be an integer and minimal.

Instead of setting k equal to S, which would result i to be maximal integer, we want to maximize the denominator while still ensuring that i is an integer. To do this, we substitute S with s * gcd(S, L). We then set k = s and substitute into the equation i = (kL)/S to get:

i = (sL)/(s * gcd(S, L))

Simplifying, we get:

i = L/gcd(S, L)

This value of i is guaranteed to be an integer and is also minimal, making it the smallest value of i that satisfies the condition (i*S) mod L = 0.


## L14.2  NailingPlanks
### Task
The task is to determine the minimum number of nails needed to mount all the given planks according to the provided nailing sequence. You are given two lists that specify the starting and ending positions of each plank, as well as a list that specifies the order in which the planks should be nailed.

### Ideas
The goal is to use the Binary Search(BS) algorithm to optimize the solution. Here are some possible options:
A) Use BS to search for the exact number of nails required. The problem with this approach is that validating each candidate number will result in repeated calculations.
B) Use BS to find a nail that matches an interval and has the smallest position among all other nails matching the interval. Then, iterate through the nails sequentially to find the one with the smallest id.

### Conclusion
I implemented option B and achieved a score of 62%. However, one correctness test is still failing. I suspect that I may have missed something and do not fully understand the requirements(my unit tests are working fine).
