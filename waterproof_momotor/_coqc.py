from pathlib import Path
import subprocess

# For now, we assume coqc is at the default location when Coq was installed
# using waterproof's dependency-installer.
# FIXME check if location exists.
coqc_location = r"C:\\cygwin_coq_platform\\home\\runneradmin\\.opam\\coq_for_waterproof\\bin\\coqc.exe"

# For now, we use a temporary file "temp.v" placed in the current directory as
# the input file for coqc.
temp_file = str(Path(__file__).parent / 'temp.v')

def coqc(txt: str) -> str:
    """
    Run coqc on given text. Returns the output as text.
    """
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(txt)
    completed_process = subprocess.run([coqc_location, temp_file], capture_output=True)
    return completed_process