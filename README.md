# 텍스트 분석 패키지

https://github.com/yosop1346-bot/pythoon__


## 1. 프로젝트 개요

이 프로젝트는 입력한 텍스트의 글자수, 문장수, 단어수를 분석하는 간단한
Python 패키지입니다. 부모 클래스와 자식 클래스를 나누어 구성했으며,
공통 기능은 부모 클래스에서 제공하고 실제 분석 기능은 자식 클래스에서
사용하도록 만들었습니다.

## 2. 설치 방법

프로젝트 폴더로 이동한 뒤 패키지를 설치합니다.

```bash
cd "C:\Users\황요섭\OneDrive\문서\파이썬_기말과제"
python -m pip install .
```

테스트와 코드 스타일 검사를 위한 개발 도구는 다음 명령어로 설치할 수 있습니다.

```bash
python -m pip install -r requirements.txt
```

이 패키지의 실행 기능은 Python 표준 라이브러리만 사용합니다.

## 3. 빠른 시작

```python
from 나의_패키지 import TextAnalyzer

analyzer = TextAnalyzer("Hello world. Python is fun!")

print(analyzer.char_count())
print(analyzer.sentence_count())
print(analyzer.word_count())
print(analyzer.analyze())
```

## 4. 주요 기능 설명

- `word_count()`: 텍스트의 단어 수를 계산합니다.
- `char_count()`: 공백을 제외한 글자 수를 계산합니다.
- `sentence_count()`: 마침표, 느낌표, 물음표를 기준으로 문장 수를 계산합니다.
- `analyze()`: 글자수, 문장수, 단어수를 한 번에 딕셔너리로 반환합니다.
- `_tokenize()`: 단어 분리를 위해 내부에서 사용하는 비공개 메서드입니다.

## 5. 테스트 실행 방법

pytest 테스트는 다음 명령어로 실행합니다.

```bash
python -m pytest
```

docstring 안의 사용 예시까지 함께 검사하려면 다음 명령어를 실행합니다.

```bash
python -m pytest --doctest-modules 나의_패키지 테스트
```

PEP 8 코드 스타일 검사는 다음 명령어로 실행합니다.

```bash
python -m pycodestyle 나의_패키지
```

검사 결과가 아무것도 출력되지 않으면 경고가 없다는 뜻입니다.

## 6. 작성자 정보

황요섭
