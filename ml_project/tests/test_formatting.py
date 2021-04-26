import subprocess


def test_formatting_with_black(src_path: str, tests_path: str):
    src_formatting_result = subprocess.run(
        ["black", "--diff", src_path], capture_output=True
    ).stderr.decode()
    assert src_formatting_result.startswith("All done!")
    tests_formatting_result = subprocess.run(
        ["black", "--diff", tests_path], capture_output=True
    ).stderr.decode()
    assert tests_formatting_result.startswith("All done!")
