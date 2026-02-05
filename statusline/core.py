class StatusLine:
    def __init__(self, enabled=True, checking_prefix="[CHECKING]"):
        self.enabled = enabled
        self.prev_len = 0
        self.checking_prefix = checking_prefix

    def update_log(self, msg: str):
        if not self.enabled:
            return
        width = max(self.prev_len, len(msg))
        print(f"\r{msg:<{width}}", end="", flush=True)
        self.prev_len = width  

    def result_log(self, msg: str):
        if not self.enabled:
            print(msg)
            return
        width = max(self.prev_len, len(msg))
        print(f"\r{msg:<{width}}")  
        self.prev_len = 0
        
    def emit(self, msg: str):
        if msg.startswith(self.checking_prefix):
            self.update_log(msg)
        else:
            self.result_log(msg)