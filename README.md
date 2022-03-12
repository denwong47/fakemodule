# fakemodule
 Convenient classes for dealing with optional modules.

## fakemodule.ModuleUnavailable
 ```
 fakemodule.ModuleUnavailable(
     exception:Exception,
     *args,
     **kwargs,
 )
 ```

 Typically, this is used:
 ```
 try:
    import missing_module
 except (ModuleNotFoundError, ImportError) as e:
    missing_module = fakemodule.ModuleUnavailable(
        e
    )
 ```

 This will allow all type hints to ignore the missing module:
 ```
 def func(
     var:missing_module.some_class,
 )
 # missing_module.some_class now returns itself, which is a ModuleUnavailable class object.
 # However unless you raise it, it will not cause an Exception in itself.
 ```
 You can check if the module is available by
 ```
 if (not isinstance(missing_module, ModuleUnavailable)):
    missing_module.do_somthing()
 ```
 or simply
 ```
 if (missing_module):
    missing_module.do_something()
 # bool(missing_module) will return False
 ```