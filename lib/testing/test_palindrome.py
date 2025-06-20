import pytest
from lib.palindrome import longest_palindromic_substring


@pytest.mark.parametrize(
    "input_str, expected_outputs",
    [
        ("babad", {"bab", "aba"}),
        ("cbbd", {"bb"}),
        ("racecar", {"racecar"}),
        ("ac", {"a", "c"}),
        ("a", {"a"}),

        ("", {""}),
        ("z", {"z"}),
        ("abcde", {"a", "b", "c", "d", "e"}),

        ("a" * 1000, { "a" * 1000 }),

        ("abccba", {"abccba"}),

        ("forgeeksskeegfor", {"geeksskeeg"}),

        ("abaxyzzyxf", {"xyzzyx"}),
    ]
)
def test_longest_palindromic_substring(input_str, expected_outputs):
    result = longest_palindromic_substring(input_str)
    assert result in expected_outputs, (
        f"For input '{input_str}', expected one of {expected_outputs} but got '{result}'"
    )


def test_type_error_on_non_string():
    with pytest.raises(TypeError):
        longest_palindromic_substring(None)

    with pytest.raises(TypeError):
        longest_palindromic_substring(123)


def test_empty_string_returns_empty():
    assert longest_palindromic_substring("") == ""


def test_single_character_returns_same():
    assert longest_palindromic_substring("x") == "x"
