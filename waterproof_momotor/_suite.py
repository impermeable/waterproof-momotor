from . import load_file, wp_formatter, coqc, lemma_names, lemmas, insert_lemma

def valid_code(code: str):
    return not 'dmitted' in code

def full_rapport(student_file, solution_file):
    student_nb = load_file(student_file)
    solution_nb = load_file(solution_file)

    # Full-run test
    student_full_code = wp_formatter(student_nb)
    result = coqc(student_full_code)
    print(
        "===> Student notebook:"
        "\nFull compilation: " + "successful" if result.returncode == 1 else "failed",
        "\nOutput:\n",
        result.stdout.decode('utf8', errors='ignore').encode('utf8'),
        "\nErrors:\n",
        *[s+"\n" for s in result.stderr.decode('utf8').splitlines()]
    )

    solution_full_code = wp_formatter(solution_nb)
    solution_result = coqc(solution_full_code)
    print(
        "\n===> Solution notebook:"
        "\nFull compilation: " + "successful" if result.returncode == 1 else "failed",
        "\nOutput:\n",
        result.stdout.decode('utf8', errors='ignore').encode('utf8'),
        "\nErrors:\n",
        *[s+"\n" for s in result.stderr.decode('utf8').splitlines()]
    )

    print(
        "\n===> Full test",
        "\nThe same non-input blocks: " + str(solution_nb.non_input_equals(student_nb)),
        "\nOutputs are equal: " + str(result.stdout == solution_result.stdout),
        "\nErrors are equal: " + str(result.stderr == solution_result.stderr)
    )


    # Single-lemma test
    print("\n===> Single Lemma tests\n")
    solution_codes = solution_nb.input_code()
    student_codes = student_nb.input_code()

    if len(solution_codes) != len(student_codes):
        print("FATAL ERROR?")
        return

    for i, student_code in enumerate(student_codes):
        # NOTE: Lemma definitions are outside of input blocks, so don't need this.
        # required_lemmas = lemma_names(solution_codes[i])
        # student_lemmas = lemmas(student_code)
        # has_required_lemmas = set(required_lemmas).issubset(set(student_lemmas))

        has_valid_code = valid_code(student_code) # To do some checks, like if it contains Admitted or so.

        replaced_nb = solution_nb.copy()
        replaced_nb.replace_input_code(i, student_code)
        replaced_code = wp_formatter(replaced_nb)
        student_result = coqc(replaced_code)

        result_valid = student_result.returncode == 1 \
            and student_result.stdout == solution_result.stdout \
            and student_result.stderr == solution_result.stderr

        print(
            "\nInput block " + str(i),
            # "\nRequired lemmas present: " + str(has_required_lemmas),
            "\nValid code: " + str(has_valid_code),
            "\nValid result: " + str(result_valid),
        )
    return True