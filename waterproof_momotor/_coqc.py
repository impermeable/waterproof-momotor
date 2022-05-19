from pathlib import Path
import subprocess

coqc_location = r"C:\\cygwin_coq_platform\\home\\runneradmin\\.opam\\coq_for_waterproof\\bin\\coqc.exe"

temp_file = str(Path(__file__).parent / 'temp.v')

def coqc(txt):
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(txt)
    completed_process = subprocess.run([coqc_location, temp_file], capture_output=True)
    return completed_process