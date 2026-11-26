# ⚓ Anchor for this module: [[nested-attr-anchor|nested_attr.py]] 


# ⚓ get_nested_attr anchor: [[get-nested-attr-anchor|get_nested_attr()]] 
#* 📝 Takes parent object and retrievs desired attribute through direct dot search
def get_nested_attr(obj: object, attr_path: str):

    from .. import validators as vls

    vls.TypeValidate(str)(value=attr_path, name="function_path")

    try:
        given_items = attr_path.split(".")

        if not all(given_items):
            raise ValueError(f"Provided {obj} path contains an empty attribute!")

        for item in given_items:
            obj = getattr(obj, item)

    except AttributeError as attr_err:
        raise ValueError(
            f"Invalid {obj} function: {attr_path}"
        ) from attr_err

    return obj


# ⚓ find_nested_attr anchor: [[find-nested-attr-anchor|find_nested_attr()]] 
#* 📝 Takes parent object and searches for the desired attribute name recursively
def find_nested_attr(obj: object, some_attr: str):
    from .. import validators as vls

    vls.TypeValidate(str)(
        value=some_attr,
        name="some_attr"
    )

    if not some_attr:
        raise ValueError("Attribute name cannot be empty.")

    visited = set()

    def search(current_obj):
        if id(current_obj) in visited:
            return None

        visited.add(id(current_obj))

        if hasattr(current_obj, some_attr):
            return getattr(current_obj, some_attr)

        for attr_name in dir(current_obj):
            if attr_name.startswith("_"):
                continue

            try:
                attribute = getattr(current_obj, attr_name)
            except Exception:                                   # noqa: BLE001, S112
                continue

            result = search(attribute)

            if result is not None:
                return result

        return None

    result = search(obj)

    if result is None:
        raise AttributeError(
            f"Could not locate attribute: {some_attr}"
        )

    return result