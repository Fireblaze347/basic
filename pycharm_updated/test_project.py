import project
import pytest

def test_get_topic_list():
    with pytest.raises(FileNotFoundError):
        project.get_topic_list("1", "cat.json")

    assert project.get_topic_list("1", "word_list.json") == ["Snow Leopard", "Leopard", "Cheetah", "Falcon", "Tiger", "Anteater", "Frog", "Elephant", "Horse", "Wolf", "Snake", "Bears", "Human", "Raccoon", "Giraffe", "Goat", "Deer", "Sheep", "Shark", "Otter", "Camel", "Gorilla", "Llama", "Platypus", "Squirrel", "bison", "fox", "beaver", "sperm whale", "bat", "beluga whale", "grizzly bear", "polar bear", "black bear", "bobcat", "lion","jaguar", "hyena", "dolphin", "moose", "chimpanzee", "panda", "giraffe"]

def test_find_elements_in_list():
    assert project.find_elements_in_list(["Mark", "Rob", "Rob"], "Rob") == [1, 2]
    assert project.find_elements_in_list("extreme", 'e') == [0, 4, 6]

def test_make_word_blanks():
    assert project.make_word_blanks("cat", [0]) == ["c", "_", "_"]
    assert project.make_word_blanks("snow leopard", [3, 5]) == ['_', '_', '_', 'w', ' ', 'l', '_', '_', '_', '_', '_', '_']
    assert project.make_word_blanks("extreme", []) == ['_', '_', '_', '_', '_', '_', '_']