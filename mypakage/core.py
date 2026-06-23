class TextBase:
    """텍스트를 저장하고 토큰화 기능을 제공하는 부모 클래스입니다.

    :ivar text: 객체에 저장된 분석 대상 텍스트입니다.

    사용 예시:
        >>> base = TextBase("hello world")
        >>> base.text
        'hello world'
    """

    def __init__(self, text):
        """TextBase 객체를 초기화합니다.

        :param text: 분석할 텍스트 데이터입니다.
        :return: 반환값이 없습니다.

        사용 예시:
            >>> base = TextBase("sample text")
            >>> base.text
            'sample text'
        """
        self.text = text

    def _tokenize(self):
        """저장된 텍스트를 공백 기준으로 단어 리스트로 나눕니다.

        :return: 공백을 기준으로 분리된 단어 리스트입니다.
        """
        return self.text.split()

    def char_tokenize(self):
        """저장된 텍스트를 공백을 제외한 글자 리스트로 나눕니다.

        :return: 공백을 제외한 글자 리스트입니다.

        사용 예시:
            >>> base = TextBase("ab cd")
            >>> base.char_tokenize()
            ['a', 'b', 'c', 'd']
        """
        return [char for char in self.text if not char.isspace()]
