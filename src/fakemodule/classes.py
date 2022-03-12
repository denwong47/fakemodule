class ModuleUnavailable(ModuleNotFoundError):
    """
    If a module is not available for some reason, an instance of this class will be returned from any of the @classmethod constructors.

    It throws an exception immediate upon init. Its purpose is academic currently.
    """
    exception = Exception("Generic Exception for unavailable API.")

    def __init__(self, exception:Exception, *args, **kwargs):
        super().__init__(str(exception), *args, **kwargs)
        self.exception = exception

    def __nonzero__(self):
        return False
    __bool__ = __nonzero__

    def __repr__(self):
        return f"{type(self).__name__}(exception={repr(self.exception)})"

    def __str__(self):
        return f"Module Unavailable: Exception [{type(self.exception).__name__}: {str(self.exception)}] reported"

    def __getattr__(self, attr):
        return self
