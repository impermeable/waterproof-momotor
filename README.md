# waterproof_momotor
Bridges the gap between waterproof's exercise sheets and momotor's automated grading

## Installation

Install with `pip install [root]`.

## Intended use
This repository contains:
- recipe and checklets to give to momotor, located in `/recipe/checklets/`
- utility functions to interact with waterproof and coqc, located in `/waterproof_momotor/` 

## Example use of utility functions
We start by importing our code.
```
from waterproof_momotor import *
```
Then, we import the notebook with worked out solutions and the student's submission.
```
master_notebook = load_file('some/waterproof/file.wpn')
student_notebook = load_file('some/waterproof/file.wpe')
```

You can extract the Coq code from this notebook in various ways, for instance
by calling `notebook.code_blocks()`. These can be manually checked for illegal
syntax such as `Admitted.`.

The first check we can do can be whether the student's submission actually
corresponds to the exercises in the master notebook. One way to check this is by
evaluating whether the student notebook is the same as the master notebook
*outside* of input blocks, as the student should not have been able to change this:
```
master_notebook.non_input_equals(student_notebook)
```

Then, moving on to more interesting checks involving Coq code compilation using
coqc, we can run the code of a notebook, for instance `master_notebook`, through
coqc as follows: 
```
master_code = wp_formatter(master_notebook, post_amble='')
result = coqc(master_code)
```

## Full API

