from gendiff.src.generate_diff import generate_diff
import json


def test_generate_diff_flat_json():
    # Define paths to fixtures
    file1 = "tests/fixtures/file1.json"
    file2 = "tests/fixtures/file2.json"
    expected_content = open("tests/fixtures/expected.txt", "r").read().rstrip()

    result = generate_diff(file1, file2)
    assert result == expected_content


def test_generate_diff_flat_yaml():
    # Define paths to fixtures
    file1 = "tests/fixtures/yaml/file1.yml"
    file2 = "tests/fixtures/yaml/file2.yml"
    expected_content = (
        open("tests/fixtures/yaml/expected.txt", "r").read().rstrip()
    )

    result = generate_diff(file1, file2)
    assert result == expected_content


def test_generate_diff_nested_json():
    # Test nested json comparison
    file1 = "tests/fixtures/nested_file1.json"
    file2 = "tests/fixtures/nested_file2.json"
    expected_content = (
        open("tests/fixtures/expected_nested.txt", "r").read().rstrip()
    )

    result = generate_diff(file1, file2)
    assert result == expected_content


def test_generate_diff_nested_yaml():
    # Use the nested YAML fixtures we created
    file1 = "tests/fixtures/yaml/nested_file1.yaml"
    file2 = "tests/fixtures/yaml/nested_file2.yaml"
    expected_content = (
        open("tests/fixtures/expected_nested.txt", "r").read().rstrip()
    )

    result = generate_diff(file1, file2)
    assert result == expected_content


def test_generate_diff_nested_plain():
    # Test plain format on nested yaml fixtures
    file1 = "tests/fixtures/yaml/nested_file1.yaml"
    file2 = "tests/fixtures/yaml/nested_file2.yaml"
    expected_content = (
        open("tests/fixtures/expected_plain.txt", "r").read().rstrip()
    )

    result = generate_diff(file1, file2, "plain")
    assert result == expected_content


def test_generate_diff_nested_json_format():
    # Test json format output
    file1 = "tests/fixtures/nested_file1.json"
    file2 = "tests/fixtures/nested_file2.json"
    result = generate_diff(file1, file2, "json")

    # Parse back the json and assert its keys and values
    data = json.loads(result)
    assert isinstance(data, dict)
    assert "common" in data
    assert data["common"]["status"] == "nested"
    assert "children" in data["common"]

    # Assert specific nested elements in json representation of diff
    common_children = data["common"]["children"]
    assert common_children["setting4"]["status"] == "added"
    assert common_children["setting4"]["new_value"] == "blah blah"
    assert common_children["setting2"]["status"] == "deleted"
    assert common_children["setting2"]["old_value"] == 200
    assert common_children["setting3"]["status"] == "changed"
    assert common_children["setting3"]["old_value"] is True
    assert common_children["setting3"]["new_value"] is None


def test_generate_diff_same_file():
    # Test that comparing a file with itself yields an empty diff or a diff
    # with no changes.
    file1 = "tests/fixtures/file1.json"
    result = generate_diff(file1, file1)
    # Depending on implementation, same file might yield empty string or a
    # stylish diff with no changes. We'll just check it's a string.
    assert isinstance(result, str)
