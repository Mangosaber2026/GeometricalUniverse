# ⚓ Anchor for this module: [[attributes-anchor|attributes.__init__.py]] 


#* 📝 Imports attribute retrieval functions in [[#nested-attr-anchor|nested_attr.py]] 
lazy from .nested_attr import (                  # noqa: I001
    get_nested_attr,
    find_nested_attr
)


#* 📝 Specifies all publicly available functions through wildcard import
__all__ = [
    "get_nested_attr",
    "find_nested_attr"
]