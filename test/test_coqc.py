from pathlib import Path
from waterproof_momotor._formatting import wp_formatter, lemmas
from waterproof_momotor.io._import import load
from waterproof_momotor._coqc import coqc

def test_coqc_tutorial():
    test_file = Path(__file__).parent / 'io' / 'test_porting' / 'tutorial.wpe'
    notebook = load(test_file)
    v = wp_formatter(notebook)
    result = coqc(v)
    assert result.returncode == 1

    print(result.stdout.decode('utf8', errors='ignore').encode('utf8'))
    print(result.stderr)

def test_lemmas_tutorial():
    test_file = Path(__file__).parent / 'io' / 'test_porting' / 'tutorial.wpe'
    notebook = load(test_file)
    lmms = lemmas(notebook)
