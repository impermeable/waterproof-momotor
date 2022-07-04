from waterproof_momotor import recipe
from pathlib import Path
test_file = Path(__file__).parent / 'io' / 'test_porting' / 'tutorial.wpe'

def test_recipe():
    assert recipe(solution_file=test_file, student_files=[test_file])
