#Note: Needs latest version of coq and 1.2.0 version files installed to work
#import html
from pathlib import Path
from waterproof_momotor.util import load_file, wp_formatter, coqc

FILE_REF_OPTION = Path(__file__).parent / "test" / "io" / "test_porting" / "Tutorial-student-perfect-1.2.0.wpe"

MASTER_NOTEBOOK_OPTION = Path(__file__).parent / "test" / "io" / "test_porting" / "Tutorial-master_1.2.0.wpn"


class ValidateContent:
        #student_file_ref = self.resolve_option(FILE_REF_OPTION)
        #student_file = self.find_files(student_file_ref)
        #student_nb = load_file(student_file, extention="wpe")
        student_nb = load_file(FILE_REF_OPTION, extention="wpe")
        print("check1")
        #master_notebook_file_ref = self.resolve_option(MASTER_NOTEBOOK_OPTION)
        #master_notebook_file = self.find_files(master_notebook_file_ref)
        #master_nb = load_file(master_notebook_file, extention="wpe")
        master_nb = load_file(MASTER_NOTEBOOK_OPTION, extention="wpe")
        print("check2")
        student_codes = student_nb.input_code()
        print("check3")
        # TODO split checklet up so that we check 1 cell per checklet?
        RESULTS = []
        report = ""
        for cell in range(0, len(student_codes)):
            report += f"Exercise {cell+1}:\t"

            student_code = student_codes[cell]

            # Pre-coq checks
            non_empty = len(student_code.strip()) > 0
            admitted_in_text = 'dmitted' in student_code
            VALID_CODE = non_empty and (not admitted_in_text) # and other stuff.

            if VALID_CODE:
                replaced_nb = master_nb.copy()
                replaced_nb.replace_input_code(cell, student_code)
                replaced_code = wp_formatter(replaced_nb)
                student_result = coqc(replaced_code)
            
                COMPILATION_ERRORS = student_result.has_error 
                RESULT = VALID_CODE and (not COMPILATION_ERRORS)

                print(RESULT )
                print(VALID_CODE) 
                print(COMPILATION_ERRORS)
                report += f"Compilation was {'not ' * (not RESULT)}successful.\n"
            else:
                RESULT = False
                report += "Invalid code.\n"
            RESULTS.append(RESULT)

## as we could not return in the momotor modules, added print statements to indicate if results were right/wrong
            if RESULTS: print("Content check passed.")
            else: print("Content check failed.")

            resultsum = sum(RESULTS)

##shows test report, and points earned by student
        if resultsum == 0:
            print(report, "No points earned")
        else:
            print (report, resultsum)

## basically import student file and master file, run both, copy student file into master file, compare errors...?
