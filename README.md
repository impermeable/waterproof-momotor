# waterproof_momotor
Bridges the gap between waterproof's exercise sheets and momotor's automated grading

## Installation

Install with `pip install [root]`.

## Intended use
This repository contains pieces of code that can be used in momotor to automatically verify waterproof notebooks using coqc. These pieces of code are called 'checklets', and can be found in `/checklets`.

Additionally, checklets are combined in a recipe to handle both flow of data and generating nice output.


## Example code
We can demonstrate a simple recipe of checklets. We start by importing our code.
```
from waterproof_momotor import *
```
Then, we import the notebook with worked out solutions and the student's submission.
```
master_notebook = load_file('some/waterproof/file.wpn')
student_notebook = load_file('some/waterproof/file.wpe')
```
The first check we can do can be whether the student's submission actually
corresponds to the exercises in the master notebook using the `CheckletNotebookIntegrity`
checklet. 
```
integrity_report = CheckletNotebookIntegrity(master_notebook, student_notebook)
```
The result of calling a Checklet will return a `CheckletReport` object, which
does not contain a lot of information at the moment, but it does contain the 
boolean attribute `result`, which indicates success or failure. 
```
if integrity_report.result == True:
    print("Success!")
```

Or, we can
check whether the 10th input cell does not contain illegal text (such as "Admitted.")
```
report_single_txt = CheckletSingleCellText
    student_notebook,
    cell=10
)
```
Then, moving on to more interesting checks involving Coq code compilation using
coqc, we start by computing the expected output of the `master_notebook`. 
```
master_code = wp_formatter(master_notebook, post_amble='')
result = coqc(master_code)
```
We do this separate from compiling the student's notebook for efficiency reasons,
as we will be using the expected output of `master_notebook` in multiple checklets.

Now, we could check the entire notebook's output at once.
```
report_full = CheckletFullCoqc(student_notebook, expected_result=result, post_amble='')
```

Or, we could check the correctness of the code in, for instance, the 10th input
cell.
```
report_single_coq = CheckletSingleCellCoqc(
    student_notebook,
    master_notebook,
    cell=10,
    expected_result=result,
    post_amble='')
```
Note that `CheckletSingleCellCoqc` even though we pass the expected result, the
master notebook is still required as we fill in the code in the student's 10th
input block into the master notebook.


## Example files
Some (example) checklets can be found in `/checklets`.
A full notebook verification example can be found in `checklets/recipe.py`.
The example file `EXAMPLE.py` contains example uses of utility code.

