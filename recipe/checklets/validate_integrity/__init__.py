from mtrchk.org.momotor.base.checklet import Checklet
from mtrchk.org.momotor.base.checklet.meta import OptionDefinition
from mtrchk.org.momotor.base.checklet.result import CheckletResult, Outcome

from waterproof_momotor import load_file

FILE_REF_OPTION = 'input-file-ref'

MASTER_NOTEBOOK_OPTION = 'master-notebook-file-ref'

class ValidateProperNotebook(Checklet):
    class Meta:
        options = (
            OptionDefinition(
                FILE_REF_OPTION,
                multiple=False,
            ),
            OptionDefinition(
                MASTER_NOTEBOOK_OPTION,
                multiple=False,
            )
        )

    def run(self) -> CheckletResult:
        student_file_ref = self.resolve_option(FILE_REF_OPTION)
        student_file = self.find_files(student_file_ref)
        student_nb = load_file(student_file, extention="wpe")

        master_notebook_file_ref = self.resolve_option(MASTER_NOTEBOOK_OPTION)
        master_notebook_file = self.find_files(master_notebook_file_ref)
        master_nb = load_file(master_notebook_file, extention="wpe")

        SAME_NB = master_nb.non_input_equals(student_nb)

        master_codes = master_nb.input_code()
        student_codes = student_nb.input_code()

        SAME_CODES = len(master_codes) == len(student_codes)

        # binary result.
        # If False, then the student handed in a faulty notebook. Automatically zero points.
        # But we should instruct students what is wrong with their notebook.
        RESULT = SAME_NB and SAME_CODES

        if RESULT:
            message = "The correct notebook was handed in."
        else:
            message = "The incorrect notebook was handed in, or the notebook is corrupted."

        return CheckletResult(
            outcome = Outcome.PASS if RESULT else Outcome.FAIL,
            properties = {'report': message},
        )