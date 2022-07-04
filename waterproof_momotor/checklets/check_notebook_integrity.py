from ..util._notebook import Notebook
from .checklet import CheckletReport

def CheckletNotebookIntegrity(student_nb: Notebook, solution_nb: Notebook):
    """
    If this checklet fails, other checklets should be discarded.
    """
    solution_codes = solution_nb.input_code()
    student_codes = student_nb.input_code()

    integrity = len(solution_codes) == len(student_codes)
    # possible more...

    return CheckletReport(result=integrity)
