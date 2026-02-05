class StatusLine:
    """Single-line progress/status logger for CLI scripts."""
    def __init__(self, checking_prefix="[CHECKING]"):
        self.prev_len = 0
        self.checking_prefix = checking_prefix

    def update_log(self, msg: str):
        width = max(self.prev_len, len(msg))
        print(f"\r{msg:<{width}}", end="", flush=True)
        self.prev_len = width  

    def result_log(self, msg: str):
        width = max(self.prev_len, len(msg))
        print(f"\r{msg:<{width}}")  
        self.prev_len = 0
        
    def emit(self, msg: str):
        if msg.startswith(self.checking_prefix):
            self.update_log(msg)
        else:
            self.result_log(msg)
