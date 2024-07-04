class AssertException(Exception):
    """Custom exception for error reporting."""

    def __init__(self, name, step):
        print(f"Assert failed,testcase{name},step:{step} ")
