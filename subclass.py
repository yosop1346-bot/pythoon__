import re

from .core import TextBase


class TextAnalyzer(TextBase):
    """글자수, 문장수, 단어수를 분석하는 클래스입니다.

    :ivar text: 객체에 저장된 분석 대상 텍스트입니다.
    :ivar language: 분석기에서 사용하는 언어 코드입니다.

    사용 예시:
        >>> analyzer = TextAnalyzer("Hello world.")
        >>> analyzer.word_count()
        2
    """

    def __init__(self, text):
        """TextAnalyzer 객체를 초기화합니다.

        :param text: 분석할 텍스트 데이터입니다.
        :return: 반환값이 없습니다.

        사용 예시:
            >>> analyzer = TextAnalyzer("hello")
            >>> analyzer.language
            'ko'
        """
        super().__init__(text)
        self.language = "ko"

    def word_count(self):
        """저장된 텍스트의 전체 단어 수를 계산합니다.

        :return: 텍스트에 포함된 전체 단어 수입니다.

        사용 예시:
            >>> analyzer = TextAnalyzer("Python package test")
            >>> analyzer.word_count()
            3
        """
        return len(self._tokenize())

    def char_count(self):
        """저장된 텍스트의 전체 글자 수를 계산합니다.

        :return: 공백을 제외한 전체 글자 수입니다.

        사용 예시:
            >>> analyzer = TextAnalyzer("ab cd")
            >>> analyzer.char_count()
            4
        """
        return len(self.char_tokenize())

    def sentence_count(self):
        """저장된 텍스트의 전체 문장 수를 계산합니다.

        :return: 텍스트에 포함된 전체 문장 수입니다.

        사용 예시:
            >>> analyzer = TextAnalyzer("Hello. Python test!")
            >>> analyzer.sentence_count()
            2
        """
        sentences = re.split(r"[.!?]+", self.text)
        return len([sentence for sentence in sentences if sentence.strip()])

    def analyze(self):
        """글자수, 문장수, 단어수를 한 번에 분석합니다.

        :return: 글자수, 문장수, 단어수를 담은 딕셔너리입니다.

        사용 예시:
            >>> analyzer = TextAnalyzer("Hello world.")
            >>> analyzer.analyze()["\\ub2e8\\uc5b4\\uc218"]
            2
        """
        return {
            "\uae00\uc790\uc218": self.char_count(),
            "\ubb38\uc7a5\uc218": self.sentence_count(),
            "\ub2e8\uc5b4\uc218": self.word_count(),
        }
