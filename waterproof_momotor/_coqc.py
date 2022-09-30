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

    return CoqcOutput(completed_process)

class CoqcOutput:
    """
    We will need something to understand coqc output but it's not entirely sure
    how this should look.
    """
    def __init__(self, completed_process: subprocess.CompletedProcess):
        # TODO:
        # - copy these values?
        # - parse the streams
        # - I think it should be combined with the post-amble or something
        self.returncode = completed_process.returncode
        self.stdout = completed_process.stdout #.decode('utf8', errors='ignore').encode('utf8')
        self.stderr = completed_process.stderr #.decode('utf8', errors='ignore').encode('utf8')

    def __eq__(self, other):
        # So, this of course has to be more flexible. Output needn't match so precisely.
        equal = self.returncode == other.returncode \
            and self.stdout == other.stdout \
            and self.stderr == other.stderr
        return equal

    @property
    def has_error(self):
        return b'Error:' in self.stderr

    @property
    def has_warning(self):
        return b'Warning:' in self.stderr