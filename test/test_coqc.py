from pathlib import Path
from waterproof_momotor import wp_formatter, lemmas, load_file, coqc


def test_coqc_tutorial():
    test_file = Path(__file__).parent / "io" / "test_porting" / "tutorial.wpe"
    notebook = load_file(test_file)
    v = wp_formatter(notebook)
    result = coqc(v)
    assert result.returncode == 1

    print(result.stdout.decode("utf8", errors="ignore").encode("utf8"))
    print(result.stderr)
    assert result.has_error


def test_lemmas_tutorial():
    test_file = Path(__file__).parent / "io" / "test_porting" / "tutorial.wpe"
    notebook = load_file(test_file)
    v = wp_formatter(notebook)
    lmms = lemmas(v)
    assert len(lmms) > 0
