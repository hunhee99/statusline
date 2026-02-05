# statusline

A tiny, dependency-free status logger for CLI scripts.  
Made because I got tired of spamming `print()` in brute-force / crawling / long loops.

## What it does

`emit()` routes your message automatically:

- If the message starts with `[CHECKING]` (or your custom prefix), it **updates in-place** on a single line (loading-bar vibe).
- Otherwise, it prints a **persistent result line** (won’t be overwritten).

## Install (editable / dev)

```bash
pip install -e .
```

Tip: If you're using a specific interpreter/venv, always install with that same Python:

```bash
python -m pip install -e .
```

## Usage

```python
from statusline import StatusLine

st = StatusLine()  # or: StatusLine(checking_prefix="[PROGRESS]")

st.emit("[CHECKING] probing...")     # updates the same line
st.emit("[CHECKING] still probing...")

st.emit("do not erase this line!")   # printed as a normal line (kept on screen)
```

### Notes
- Prefix matching is simple string logic: `msg.startswith(checking_prefix)`.
- If your editor (e.g., VSCode/Pylance) shows missing-import warnings while it still runs,
your language server is probably using a different interpreter. Select the same interpreter
you used to install this package and restart the language server.

---

## statusline (한국어)

CLI에서 로그 찍는 게 귀찮아서 만든 초경량(의존성 없음) 상태 출력 유틸.
브루트포스/크롤링/긴 반복문 돌릴 때 `print()` 난사하기 싫어서 만들었음.

### 기능

emit() 하나로 자동 분기됨:
- 메시지가 [CHECKING](또는 커스텀 prefix)로 시작하면 한 줄에서 계속 갱신됨(로딩바 느낌)
- 그 외 메시지는 결과 로그로 확정 출력되어 절대 안 지워짐

### 설치 (editable / 개발용)

```bash
pip install -e .
```

팁: 인터프리터/venv를 쓰고 있다면, 항상 같은 파이썬으로 설치해야 함:

```bash
python -m pip install -e .
```

### 사용법

```python
from statusline import StatusLine

st = StatusLine()  # StatusLine(checking_prefix="[PROGRESS]") 처럼 prefix 변경도 가능

st.emit("[CHECKING] 뭐시기...")     # 같은 줄에서 계속 갱신됨
st.emit("[CHECKING] 더 뭐시기...")

st.emit("지워지지 말거라!")         # 결과는 개행으로 확정 출력(안 사라짐)
```
