# Homework 04b: Static Code Analysis
[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/YBMEBAqhQKNrvTPDbdRbap/Uzcx6xoX9zwJYNYQd7TPgS/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/YBMEBAqhQKNrvTPDbdRbap/Uzcx6xoX9zwJYNYQd7TPgS/tree/main)

The purpose of this assignment was to use a static code analysis (i.e. PyLint) and a code coverage (i.e. coverage) tools on our preexisting triangle classification code from hw00b. While it's a small python script, it's a good introduction into static testing for later on larger projects.

One thing I found particularly interesting from the static code analysis was it's conformity to specific standards that hard hard for a human to notice, like trailing whitespace. While it was somewhat helpful in giving suggestions on how to improve the organization and clenliness of the code, it became somewhat annoying to use as there were still a few lingering issues at the end that didn't affect the functionality of the program. While I didn't agree with everything it pointed out, I did make some of those changes jsut to get a better score.

As for code coverage, while I wasn't able to fully use it without getting rid of my preexisting test cases I made, I do see how helpful it would be later on for large projects that require a lot of testing. The coverage program offers a lot of insight as to what is already covered by test cases and what is not. Again, I see this being really useful later on when building out a large slate of test cases in order to test every part of my code.

## Static Code Analyzer: PyLint

### Before
```bash
$   pylint triangleClassification.py 
```

```
************* Module triangleClassification
triangleClassification.py:6:1: C0303: Trailing whitespace (trailing-whitespace)
triangleClassification.py:8:80: C0303: Trailing whitespace (trailing-whitespace)
triangleClassification.py:9:76: C0303: Trailing whitespace (trailing-whitespace)
triangleClassification.py:10:75: C0303: Trailing whitespace (trailing-whitespace)
triangleClassification.py:28:0: C0303: Trailing whitespace (trailing-whitespace)
triangleClassification.py:32:0: C0303: Trailing whitespace (trailing-whitespace)
triangleClassification.py:34:31: C0303: Trailing whitespace (trailing-whitespace)
triangleClassification.py:38:0: C0303: Trailing whitespace (trailing-whitespace)
triangleClassification.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
triangleClassification.py:47:0: C0304: Final newline missing (missing-final-newline)
triangleClassification.py:1:0: C0114: Missing module docstring (missing-module-docstring)
triangleClassification.py:1:0: C0103: Module name "triangleClassification" doesn't conform to snake_case naming style (invalid-name)
triangleClassification.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
triangleClassification.py:20:23: C0103: Argument name "a" doesn't conform to snake_case naming style (invalid-name)
triangleClassification.py:20:26: C0103: Argument name "b" doesn't conform to snake_case naming style (invalid-name)
triangleClassification.py:20:29: C0103: Argument name "c" doesn't conform to snake_case naming style (invalid-name)
triangleClassification.py:22:4: R1703: The if statement can be replaced with 'var = bool(test)' (simplifiable-if-statement)
triangleClassification.py:30:4: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
triangleClassification.py:34:9: R0916: Too many boolean expressions in if statement (6/5) (too-many-boolean-expressions)
triangleClassification.py:20:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)

-----------------------------------
Your code has been rated at 0.00/10
```
### After
```bash
$   pylint triangle_classification_fixed.py
```
*Notice how it even had me change the naming of my python program.*

```
************* Module triangle_classification_fixed
triangle_classification_fixed.py:24:4: R1703: The if statement can be replaced with 'var = bool(test)' (simplifiable-if-statement)
triangle_classification_fixed.py:36:7: R0916: Too many boolean expressions in if statement (6/5) (too-many-boolean-expressions)
triangle_classification_fixed.py:11:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)

------------------------------------------------------------------
Your code has been rated at 7.00/10
```

## Code Coverage: Coverage.py
```bash
$   coverage run test_triangle.py
$   coverage report -m
```

### Before
```
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
test_triangle.py               21      0   100%
triangleClassification.py      10      0   100%
---------------------------------------------------------
TOTAL                          31      0   100%
```

### After
```
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
test_triangle_fixed.py                21      0   100%
triangle_classification_fixed.py      10      0   100%
----------------------------------------------------------------
TOTAL                                 31      0   100%
```
Note that nothing was changed in `triangleClassification.py` and `triangle_classification_fixed.py` since coverage was already at 100%

## Screenshots
|       | Before           | After |
| ------------- |:-------------:| -----:|
| Static Analysis      | ![Before Static Analysis](https://github.com/carsonblee/SSW567/blob/main/hw04/hw04b/Before/StaticAnalysisBefore.png) | ![After Static Analysis](https://github.com/carsonblee/SSW567/blob/main/hw04/hw04b/After/StaticAnalysisAfter.png) |
| Code Coverage      | ![Before Code Coverage](https://github.com/carsonblee/SSW567/blob/main/hw04/hw04b/Before/CodeCoverageBefore.png)     |   ![After Code Coverage](https://github.com/carsonblee/SSW567/blob/main/hw04/hw04b/After/CodeCoverageAfter.png) |
