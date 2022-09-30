from waterproof_momotor import Notebook, load_file
from pathlib import Path


def test_notebook():
    test_file = Path(__file__).parent / "io" / "test_porting" / "tutorial.wpe"
    nb = load_file(test_file)
    assert len(nb.input_code()) > 0
    assert len(nb.code_blocks()) > 0
