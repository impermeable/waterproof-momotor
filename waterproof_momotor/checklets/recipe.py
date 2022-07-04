from typing import List, Optional

from .check_notebook_integrity import CheckletNotebookIntegrity
from .full_run_coqc import CheckletFullCoqc
from .single_cell_coqc import CheckletSingleCellCoqc
from .single_cell_manual_checks import CheckletSingleCellText
from ..util._import import load_file
from ..util._coqc import coqc
from ..util._formatting import wp_formatter

def recipe(solution_file: str, student_files: List[str], post_amble: Optional[str] = ''):
    solution_nb = load_file(solution_file)
    N_blocks = len(solution_nb.input_code())
    solution_code = wp_formatter(solution_nb, post_amble=post_amble)
    expected_result = coqc(solution_code)

    for student_file in student_files:
        student_nb = load_file(student_file)

        integrity_report = CheckletNotebookIntegrity(student_nb, solution_nb)


        if integrity_report.result:
            report_full = CheckletFullCoqc(student_nb, expected_result, post_amble=post_amble)
            for input_block in range(N_blocks):

                report_single_txt = CheckletSingleCellText(student_nb, input_block)
                report_single_coq = CheckletSingleCellCoqc(student_nb, solution_nb, input_block, expected_result, post_amble=post_amble)

        # TODO doing something with reports...

    return True