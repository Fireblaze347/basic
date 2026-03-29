import project
import pytest

def test_get_topic_list():
    with pytest.raises(FileNotFoundError):
        project.get_topic_list("1", "cat.json")

    assert project.get_topic_list("1", "word_list.json") == ["Snow Leopard", "Leopard", "Cheetah", "Falcon", "Tiger", "Anteater", "Frog", "Elephant", "Horse", "Wolf", "Snake", "Bears", "Human", "Raccoon", "Giraffe", "Goat", "Deer", "Sheep", "Shark", "Otter", "Camel", "Gorilla", "Llama", "Platypus", "Squirrel", "bison", "fox", "beaver", "sperm whale", "bat", "beluga whale", "grizzly bear", "polar bear", "black bear", "bobcat", "lion","jaguar", "hyena", "dolphin", "moose", "chimpanzee", "panda", "giraffe"]

def test_find_topic_choice():
    assert project.find_topic_choice() = 