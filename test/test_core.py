from importlib import import_module


TextAnalyzer = import_module(
    "\ub098\uc758_\ud328\ud0a4\uc9c0.subclass"
).TextAnalyzer


def test_word_count():
    analyzer = TextAnalyzer("Python package test")

    assert analyzer.word_count() == 3


def test_char_count():
    analyzer = TextAnalyzer("ab cd")

    assert analyzer.char_count() == 4


def test_sentence_count():
    analyzer = TextAnalyzer("Hello. Python test!")

    assert analyzer.sentence_count() == 2


def test_analyze():
    analyzer = TextAnalyzer("Hello world.")

    assert analyzer.analyze() == {
        "\uae00\uc790\uc218": 11,
        "\ubb38\uc7a5\uc218": 1,
        "\ub2e8\uc5b4\uc218": 2,
    }
