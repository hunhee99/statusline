# statusline

A tiny, dependency-free status logger for CLI scripts.  
Made because I got tired of spamming `print()` in brute-force / crawling / long loops.

## What it does

`emit()` routes your message automatically:

- If the message starts with `[CHECKING]` (or your custom prefix), it **updates in-place** on a single line (loading-bar vibe).
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

Tip: If you're using a specific interpreter/venv, always install with that same Python:

```bash
python -m pip install -e .
```

## Versioning / Release Notes

- PyPI publishes versioned releases. Install a specific version like:

```bash
python -m pip install statusline==X.Y.Z
```

- Git tags match released versions. Check tags or release notes on GitHub if you need
changelogs or want to pin a specific release.

- Note: `0.1.1` removes the `enabled` argument from `StatusLine` to simplify behavior.

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
