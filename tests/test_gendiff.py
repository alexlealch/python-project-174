import pytest
from gendiff.src.generate_diff import generate_diff

def test_generate_diff_flat_json():
    # Define paths to fixtures
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"
    expected_content = open("tests/fixtures/expected.txt", "r").read()

    result = generate_diff(file1, file2)
    assert result == expected_content
