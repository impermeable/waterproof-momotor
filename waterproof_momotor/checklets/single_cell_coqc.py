from ..util._notebook import Notebook
from ..util._formatting import wp_formatter
from ..util._coqc import coqc, CoqcOutput
from .checklet import CheckletReport

def CheckletSingleCellCoqc(student_nb: Notebook, solution_nb: Notebook, cell: int, expected_result: CoqcOutput, post_amble: str =''):
    """
    Will place the `cell`-th input block of student_nb into (a copy of) the
    solution_nb, pass it to coqc, and collect the output.

    Parameters
    ----------
    student_nb, solution_nb : Notebook
        The student notebook and worked out solution notebook respectively.
    cell : int
        cell number to replace.
    """
    student_codes = student_nb.input_code()

    if cell < 0 or cell >= len(student_codes):
        raise Exception("Some error on our side...")

    student_code = student_codes[cell]
    replaced_nb = solution_nb.copy()
    replaced_nb.replace_input_code(cell, student_code)
    replaced_code = wp_formatter(replaced_nb, post_amble=post_amble)
    student_result = coqc(replaced_code)
    
    # do stuff with student_result?
    return CheckletReport(result = student_result == expected_result)