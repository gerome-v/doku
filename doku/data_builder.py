class BaseDataBuilder:
    """Write one-line summary of this class.

    Write multi-line summary of this class. Whatever you want to write you
    can write it here.

    Attributes:
        att_a (int): description of this attribute.
    """
    def __init__(self):
        self.att_a = 0

    def method_a(self, path):
        """
        Args:
            path (str): path of the file to read.
        """
        print(f"Loading path: {path}...")
