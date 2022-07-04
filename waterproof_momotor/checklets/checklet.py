class CheckletReport:
    def __init__(self, result):
        assert isinstance(result, bool)
        self.result = result
        # json stuff?
        # HTML formatted output?
        # I'm not sure what should be here.