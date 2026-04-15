
import pytest
from string_utils import (count, reverse_string, is_palindoram,
                          world_count, capatilize_words, remove_duplicate)

# ── count_vowels ──────────────────────────────────────────
def test_count_vowels_normal_string():
    assert count("hello") == 2


def test_count_vowels_case_insensitive():
    assert count("AEIOU") == 5

def test_count_vowels_empty_string():
    assert count("") == 0

def test_count_vowels_no_vowels():
    assert count("bcd") == 0

def test_count_vowels_none_raises_type_error():
    with pytest.raises(TypeError):
        count(None)

# ── reverse_string ────────────────────────────────────────
def test_reverse_string_normal():
    assert reverse_string("abc") == "cba"

def test_reverse_string_single_character():
    assert reverse_string("a") == "a"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_none_raises_type_error():
    with pytest.raises(TypeError):
        reverse_string(None)

# ── is_palindrome ─────────────────────────────────────────
def test_is_palindrome_simple_true():
    assert is_palindoram("racecar") is True

def test_is_palindrome_with_spaces():
    assert is_palindoram("A man a plan a canal Panama") is True

def test_is_palindrome_false():
    assert is_palindoram("hello") is False

def test_is_palindrome_single_character():
    assert is_palindoram("a") is True

def test_is_palindrome_none_raises_type_error():
    with pytest.raises(TypeError):
        is_palindoram(None)

# ── world_count ────────────────────────────────────────────
def test_world_count_two_words():
    assert world_count("Hello World") == 2

def test_world_count_extra_spaces():
    assert world_count(" spaces  ") == 1

def test_world_count_empty_string():
    assert world_count("") == 0

def test_world_count_none_raises_type_error():
    with pytest.raises(TypeError):
        world_count(None)

# ── capatilize_words ──────────────────────────────────────
def test_capatilize_words_normal():
    assert capatilize_words("hello world") == "Hello World"

def test_capatilize_words_already_capitalised():
    assert capatilize_words("Hello World") == "Hello World"

def test_capatilize_words_empty():
    assert capatilize_words("") == ""

def test_capatilize_words_none_raises_type_error():
    with pytest.raises(TypeError):
        capatilize_words(None)

# ── remove_duplicates ─────────────────────────────────────
def test_remove_duplicates_normal():
    assert remove_duplicate("aaabbbcc") == "abc"

def test_remove_duplicates_long_run():
    assert remove_duplicate("aaaaaabc") == "abc"

def test_remove_duplicates_no_duplicates():
    assert remove_duplicate("abc") == "abc"

def test_remove_duplicates_empty():
    assert remove_duplicate("") == ""

def test_remove_duplicates_single_character():
    assert remove_duplicate("a") == "a"

def test_remove_duplicates_none_raises_type_error():
    with pytest.raises(TypeError):
        remove_duplicate(None)





