from ..util._notebook import Notebook
from .checklet import CheckletReport

def CheckletSingleCellText(student_nb: Notebook, cell: int):
    """
    Will check the text in the `cell`-th input block's code.

    Parameters
    ----------
    student_nb : Notebook
        The student notebook.
    cell : int
        cell number to check.
    """
    student_codes = student_nb.input_code()
    
    if cell < 0 or cell >= len(student_codes):
        raise Exception("Some error on our side...")

    student_code = student_codes[cell]

    admitted_in_text = 'dmitted' in student_code
    valid_code = not admitted_in_text # and other stuff.

    return CheckletReport(result=valid_code)
