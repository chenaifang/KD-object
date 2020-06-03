from torch.utils.cpp_extension import BuildExtension

#from torch.utils.ffi import _wrap_function
#from torch.utils import ffi as _ffi

import ctypes
#from ._roi_crop.so import lib as _lib, ffi as _ffi
#from lib.model.roi_crop._ext.roi_crop._roi_crop import lib as _lib, ffi as _ffi

#so_lib_path ="F:\\Graduation Project\\code\\code\\Distilling-Object-Detectors\\lib\model\\roi_crop\\_ext\\roi_crop\\_roi_crop.so"

so_lib_path="./_roi_crop.so"
print(so_lib_path)
_lib = ctypes.cdll.LoadLibrary(so_lib_path)
__all__ = []
def _import_symbols(locals):
    for symbol in dir(_lib):
        fn = getattr(_lib, symbol)
        if callable(fn):
            _ffi = BuildExtension(...)
            locals[symbol] = BuildExtension(fn, _ffi)
            #locals[symbol] = _wrap_function(fn, _ffi)
        else:
            locals[symbol] = fn
        __all__.append(symbol)

_import_symbols(locals())
