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

## L14.2  NailingPlanks
### Task:
The task is to determine the minimum number of nails needed to mount all the given planks according to the provided nailing sequence. You are given two lists that specify the starting and ending positions of each plank, as well as a list that specifies the order in which the planks should be nailed.

### Ideas:
The goal is to use the Binary Search(BS) algorithm to optimize the solution. Here are some possible options:
A) Use BS to search for the exact number of nails required. The problem with this approach is that validating each candidate number will result in repeated calculations.
B) Use BS to find a nail that matches an interval and has the smallest position among all other nails matching the interval. Then, iterate through the nails sequentially to find the one with the smallest id.

### Conclusion:
I implemented option B and achieved a score of 62%. However, one correctness test is still failing. I suspect that I may have missed something and do not fully understand the requirements(my unit tests a working fine).
