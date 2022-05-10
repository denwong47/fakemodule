import importlib
from types import ModuleType
from typing import Union

class MetaclassFakeModule(type):
    def __getattr__(self, attr):
        # Returns ModuleUnavailable instead of itself.
        # This allows type hints such as Tuple[] to pass.
        return ModuleUnavailable

    def __nonzero__(self):
        # In case ModuleUnavailable.some_prop is called, return False.
        return False
    __bool__ = __nonzero__

class ModuleUnavailable(ModuleNotFoundError, metaclass=MetaclassFakeModule):
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
        # Returns a class instead of itself.
        # This allows type hints such as Tuple[] to pass.
        return type(self)

    @classmethod
    def load(
        cls,
        name:str,
    )->Union[
        ModuleType,
        "ModuleUnavailable"
    ]:
        """
        Try loading an optional module, return a ModuleUnavailable if not found.

        Example:
        ```python
        np = OptionalModule.load("numpy")
        ```
        """

        try:
            return importlib.import_module(name)
        except (ImportError, ModuleNotFoundError) as e:
            return cls(e)

OptionalModule = ModuleUnavailable # Alias to make OptionalModule.load() make a bit more sense
