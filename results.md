# 실행 결과 요약

## 1. pycodestyle 실행 결과

실행 명령:

```bash
python -m pycodestyle setup.py 나의_패키지 테스트
```

실행 결과:

```text
출력 없음
```

`pycodestyle`은 경고가 있을 때만 내용을 출력하므로, 현재 경고는 0건입니다.

## 2. pytest 실행 결과

실행 명령:

```bash
python -m pytest --doctest-modules 나의_패키지 테스트
```

실행 결과:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\황요섭\OneDrive\문서\파이썬_기말과제
collected 13 items

나의_패키지\core.py ...                                                  [ 23%]
나의_패키지\subclass.py ......                                           [ 69%]
테스트\test_core.py ....                                                 [100%]

============================= 13 passed in 0.21s ==============================
```

## 3. pip install . 실행 결과

실행 명령:

```bash
python -m pip install .
```

실행 결과:

```text
Processing .\.
Building wheels for collected packages: text-analyzer-package
Successfully built text-analyzer-package
Installing collected packages: text-analyzer-package
Successfully installed text-analyzer-package-0.1.0
```

패키지가 정상적으로 빌드되고 설치되었습니다.

## 4. 설치 후 import 확인

실행 예시:

```python
from 나의_패키지 import TextAnalyzer

analyzer = TextAnalyzer("Hello world. Python test!")
print(analyzer.analyze())
```

실행 결과:

```text
{'글자수': 22, '문장수': 2, '단어수': 4}
```

## 5. 가상환경에서 설치 후 import 확인

실행 명령:

```bash
python -m venv .venv_check
.\.venv_check\Scripts\python.exe -m pip install .
.\.venv_check\Scripts\python.exe -c "from 나의_패키지 import TextAnalyzer; analyzer = TextAnalyzer('Hello world. Python test!'); print(analyzer.analyze())"
```

실행 결과:

```text
Successfully installed text-analyzer-package-0.1.0
{'글자수': 22, '문장수': 2, '단어수': 4}
```

임시 가상환경에서도 패키지 설치와 import가 정상적으로 동작했습니다.
