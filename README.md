# statusline

Tiny, dependency-free **single-line status logger** for brute-forcing / crawling / long loops.  
Use it when you want **live progress on one line** but keep **important results printed permanently**.

## Demo

### Without statusline (print spam)

![Without statusline](https://raw.githubusercontent.com/hunhee99/statusline/main/assets/unuse_statusline.gif)

### With statusline

![With statusline](https://raw.githubusercontent.com/hunhee99/statusline/main/assets/use_statusline.gif)

> **Idea:**  
> - Messages starting with `[CHECKING]` update **in-place** on a single line (in-place/single-line status).  
> - Anything else is printed as a **persistent result line** (won’t be overwritten).

---

## What it does

`emit()` routes your message automatically:

- If the message starts with `[CHECKING]` (or your custom prefix), it **updates in-place** on a single line.
- Otherwise, it prints a **persistent result line** (won’t be overwritten).

## Install (PyPI)

```bash
python -m pip install statusline
```

## Install (editable / dev)

```bash
git clone https://github.com/hunhee99/statusline.git
cd statusline
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
