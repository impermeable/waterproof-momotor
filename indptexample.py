from waterproof_momotor.util._formatting import wp_formatter, lemma_names, lemmas, insert_lemma
from waterproof_momotor.util._coqc import coqc
from waterproof_momotor.util._import import load_file
from pathlib import Path

test_file = Path(__file__).parent / "test" / "io" / "test_porting" / "tutorial.wpe"
FILE_REF_OPTION = test_file
#MASTER_NOTEBOOK_OPTION = Path(__file__).parent / "test" / "io" / "test_porting" / "Tutorial-student-perfect-master-copy.wpe"

# =========
# notebook object
notebook = load_file(test_file)

print(f"Loaded notebook with {len(notebook.blocks)} blocks")

# =========
# running a test suite is easy
import check_integrity, check_content

# Run a full report, using the same (empty) file as submission and solution
#recipe(solution_file=test_file, student_files=[test_file])

# =========
# other functions

# extract code and add post_amble
print("code is extracted.")
extracted_code = wp_formatter(notebook, post_amble="")

# print does not work on some chars in the notebook
print(f"Extracted code: \n==========\n{extracted_code[:20]} ... {extracted_code[-20:]}\n==========\n") 

# we can send the code through coqc manually
coqc_output = coqc(extracted_code) # is a CompletedProcess object
# you can use coqc_output.stdout, .stderr, .returncode, to extract information from the CompletedProcess
print(f"coqc output:\n\t{coqc_output.stdout}\n")

# We can also extract information from notebooks!
# This has to be double checked for correctness
lemma_names_in_file = lemma_names(extracted_code)
print("Lemma's: " + ", ".join(lemma_names_in_file) + "\n")

lemmas_in_file = lemmas(extracted_code)
some_lemma = lemmas_in_file[lemma_names_in_file[2]]
print("Some random lemma:\n==========\n" + some_lemma)
# as before, some chars can't be `print`-ed, so we choose lemma 2 because it
# does not contain, \reals, \forall, etc.