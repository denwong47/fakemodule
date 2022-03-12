
import types

import fakemodule
from fakemodule import ModuleUnavailable

import quicktest
unittest = quicktest

class TestFakeModule(unittest.TestCase):
    
    def test_ModuleUnavailable(self):
        try:
            import re
        except fakemodule.exceptions as e:
            re = ModuleUnavailable(e)

        try:
            import missing_module
        except fakemodule.exceptions as e:
            missing_module = ModuleUnavailable(e)

        self.assertIsInstance(re, types.ModuleType)
        self.assertIsInstance(missing_module, ModuleUnavailable)
        self.assertIsInstance(missing_module.some_method, ModuleUnavailable)
        self.assertIsInstance(missing_module.some_class.some_prop, ModuleUnavailable)


if (__name__=="__main__"):
    unittest.main()