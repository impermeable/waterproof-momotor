from ..util._notebook import Notebook
from ..util._formatting import wp_formatter
from ..util._coqc import coqc, CoqcOutput
from .checklet import CheckletReport

def CheckletFullCoqc(student_nb: Notebook, expected_result: CoqcOutput, post_amble : str = ''):
    """
    Will run the student_nb and check the complete output

    Parameters
    ----------
    student_nb : Notebook
        The student notebook and worked out solution notebook respectively.
    cell : int
        cell number to replace.
    """
    student_code = wp_formatter(student_nb, post_amble=post_amble)
    student_result = coqc(student_code)
    
    # do stuff with student_result?
    return CheckletReport(result = student_result == expected_result)