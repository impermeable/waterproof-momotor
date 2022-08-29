from mtrchk.org.momotor.base.checklet import Checklet
from mtrchk.org.momotor.base.checklet.meta import OptionDefinition
from mtrchk.org.momotor.base.checklet.result import CheckletResult, Outcome, CheckletResultPropsType, \
    CheckletResultFilesType, NameClass

import html
from waterproof_momotor import load_file, wp_formatter, coqc

FILE_REF_OPTION = 'input-file-ref'

MASTER_NOTEBOOK_OPTION = 'master-notebook-file-ref'

FORBIDDEN_TERMS = ['Admitted']

class ValidateContent(Checklet):
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

        student_codes = student_nb.input_code()

        # TODO split checklet up so that we check 1 cell per checklet?
        RESULTS = []
        report = ""
        for cell in range(0, len(student_codes)):
            report += f"Exercise {cell+1}:\t"

            student_code = student_codes[cell]

            # Pre-coq checks
            non_empty = len(student_code.strip()) > 0
            FORBIDDEN_TERM_IN_TEXT = False
            for term in FORBIDDEN_TERMS:
                if term in student_code:
                    FORBIDDEN_TERM_IN_TEXT = True
            VALID_CODE = non_empty and (not FORBIDDEN_TERM_IN_TEXT) # and other stuff.

            if VALID_CODE:
                replaced_nb = master_nb.copy()
                replaced_nb.replace_input_code(cell, student_code)
                # TODO: only extract code cells up until this point?
                replaced_code = wp_formatter(replaced_nb)
                student_result = coqc(replaced_code)

                COMPILATION_ERRORS = student_result.has_error
                RESULT = VALID_CODE and (not COMPILATION_ERRORS)
                report += f"Compilation was {'not ' * (not RESULT)}successful.\n"
            else:
                RESULT = False
                report += "Invalid code.\n"
            RESULTS.append(RESULT)

        # TODO: better report test_report: typing.Sequence[typing.Dict]
        # I would like to use https://gitlab.tue.nl/momotor/checklet/mtrchk-org-momotor-lti-testreport/-/tree/version-2/src/mtrchk/org/momotor/lti/testreport
        # report: typing.Sequence[typing.Dict] = [
        #   blocks
        # ]
        # block: typing.Dict = {
        #   cases
        # }
        # CASE is :
        #   VALID_CODE, or
        #   COMPILATION_ERROR


        return CheckletResult(
            outcome = Outcome.PASS if any(RESULTS) else Outcome.FAIL,
            properties = {
                'report': report,
                'score': sum(RESULTS),
                'reason': 'No points earned' if sum(RESULTS)==0 else '',
            },
        )