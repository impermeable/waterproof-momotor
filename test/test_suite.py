from waterproof_momotor import full_rapport
from pathlib import Path
test_file = Path(__file__).parent / 'io' / 'test_porting' / 'tutorial.wpe'

def test_suite():
    assert full_rapport(student_file=test_file, solution_file=test_file)
