from waterproof_momotor import load_file, coqc, wp_formatter, lemma_names, lemmas

from pathlib import Path

test_file = Path(__file__).parent / "test" / "io" / "test_porting" / "tutorial.wpe"

# notebook object
notebook = load_file(test_file)

print(f"Loaded notebook with {len(notebook.blocks)} blocks")

# wp_formatter is an ugly name
extracted_code = wp_formatter(notebook, post_amble="")

# print does not work on some chars in the notebook
print(f"Extracted code: \n==========\n{extracted_code[:20]} ... {extracted_code[-20:]}\n==========\n")

coqc_output = coqc(extracted_code) # is a CompletedProcess object

# formatting is weird here, some unicode? stuff isnt decoded?
print(f"coqc output:\n\t{coqc_output.stdout}\n")

# We can also extract information from notebooks!
# This has to be double checked for correctness
lemma_names_in_file = lemma_names(notebook)
print("Lemma's: " + ", ".join(lemma_names_in_file) + "\n")

lemmas_in_file = lemmas(notebook)
some_lemma = lemmas_in_file[lemma_names_in_file[2]]
print("Some random lemma:\n==========\n" + some_lemma)
# as before, some chars can't be `print`-ed, so we choose lemma 2 because it
# does not contain, \reals, \forall, etc.