# waterproof_momotor
Bridges the gap between waterproof's exercise sheets and momotor's automated grading

### Installation

Install with `pip install [root]`.

### Intended use
This repository contains pieces of code that can be used in momotor to automatically verify waterproof notebooks using coqc. These pieces of code are called 'checklets', and can be found in `/checklets`.

Additionally, checklets are combined in a recipe to handle both flow of data and generating nice output.

### Example
Some (example) checklets can be found in `/checklets`.
A full notebook verification example can be found in `checklets/recipe.py`.
The example file `EXAMPLE.py` contains example uses of utility code.
