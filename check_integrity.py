from waterproof_momotor.util._import import load_file
from pathlib import Path

FILE_REF_OPTION = Path(__file__).parent / "test" / "io" / "test_porting" / "Tutorial-student-perfect-1.2.0.wpe"

MASTER_NOTEBOOK_OPTION = Path(__file__).parent / "test" / "io" / "test_porting" / "Tutorial-master_1.2.0.wpn"
print ("hi")
class ValidateProperNotebook:  
        print("hello")
        #def run(self):
        print("check1")
                #student_file_ref = self.resolve_option(FILE_REF_OPTION)
                #student_file = self.find_files(student_file_ref)
        student_nb = load_file(FILE_REF_OPTION, extention="wpe")

        print("check2")
                #master_notebook_file_ref = self.resolve_option(MASTER_NOTEBOOK_OPTION)
                #master_notebook_file = self.find_files(master_notebook_file_ref)
        master_nb = load_file(MASTER_NOTEBOOK_OPTION, extention="wpn")

        print("check3")
        SAME_NB = master_nb.non_input_equals(student_nb)

        print("check4")
        master_codes = master_nb.input_code()
        student_codes = student_nb.input_code()

        SAME_CODES = len(master_codes) == len(student_codes)

        print("check5")
        # binary result.
        # If False, then the student handed in a faulty notebook. Automatically zero points.
        # But we should instruct students what is wrong with their notebook.
        RESULT = SAME_NB and SAME_CODES
                
        if RESULT: print("Integrity check passed.")  # added print statement as momotor return type not supported
        else: print("Integrity check failed.")

