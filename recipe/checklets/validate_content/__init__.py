from mtrchk.org.momotor.base.checklet import Checklet
from mtrchk.org.momotor.base.checklet.meta import OptionDefinition
from mtrchk.org.momotor.base.checklet.result import (
    CheckletResult,
    Outcome,
    CheckletResultPropsType,
    CheckletResultFilesType,
    NameClass,
)

from waterproof_momotor import load_file, wp_formatter, coqc

FILE_REF_OPTION = "input-file-ref"

MASTER_NOTEBOOK_OPTION = "master-notebook-file-ref"

FORBIDDEN_TERMS = ["Admitted"]


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
            ),
        )

    # Should use https://gitlab.tue.nl/momotor/checklet/mtrchk-org-momotor-lti-testreport/-/tree/version-2/src/mtrchk/org/momotor/lti/testreport

    def run(self) -> CheckletResult:
        student_file_ref = self.resolve_option(FILE_REF_OPTION)
        student_file = self.find_files(student_file_ref)
        student_nb = load_file(student_file, extention="wpe")

        master_notebook_file_ref = self.resolve_option(MASTER_NOTEBOOK_OPTION)
        master_notebook_file = self.find_files(master_notebook_file_ref)
        master_nb = load_file(master_notebook_file, extention="wpe")

        student_codes = student_nb.input_code()

        REPORT = []
        for cell in range(0, len(student_codes)):
            # to store results.
            CASES = []
            SKIPPED = []

            # =========== Pre-coq validation testcase ===========
            student_code = student_codes[cell]
            non_empty = len(student_code.strip()) > 0
            has_forbidden_term = False
            for term in FORBIDDEN_TERMS:
                if term in student_code:
                    has_forbidden_term = True
            has_valid_code = non_empty and (not has_forbidden_term)  # and other stuff.

            CODE_PRECHECK_CASE = {
                "description": "Check if the input block contains illegal syntax.",
                "passed": has_valid_code,
                "skipped": False,
                "message": "",
                "score": 0,
                "max_score": 0,
            }
            CASES.append(CODE_PRECHECK_CASE)

            # =========== Actual code testcase ===========
            if has_valid_code:
                replaced_nb = master_nb.copy()
                replaced_nb.replace_input_code(cell, student_code)
                # NOTE: Or do we only extract code cells up until this point?
                replaced_code = wp_formatter(replaced_nb)
                student_result = coqc(replaced_code)

                has_compilation_errors = student_result.has_error

                CODE_VALID_CASE = {
                    "description": "Run coq code.",
                    "passed": not has_compilation_errors,
                    "skipped": False,
                    "message": "Success!",
                    "score": 1,
                    "max_score": 1,
                }
                CASES.append(CODE_VALID_CASE)
            else:
                CODE_VALID_CASE = {
                    "description": "Run Coq code.",
                    "passed": False,
                    "skipped": True,
                    "message": "Skipped because the precheck failed.",
                    "score": 0,
                    "max_score": 1,
                }
                SKIPPED.append(
                    CODE_VALID_CASE
                )  # FIXME or does this need to be added to CASES instead?

            # =========== Finalize block for report ===========
            BLOCK = {
                "description": f"Exercise (input cell) {cell+1}",
                "cases": CASES,
                "skipped": SKIPPED,
                "max_score": 1,
                "score": sum(case["score"] for case in CASES),
            }
            REPORT.append(BLOCK)

        return CheckletResult(
            outcome=Outcome.PASS
            if any(block["score"] == 0 for block in REPORT)
            else Outcome.FAIL,
            properties={
                "report": REPORT,  # FIXME FIX TYPE? do we need to dump to json? Report type is string?
                "score": sum(block["score"] for block in REPORT),
                "reason": "",
            },
        )
