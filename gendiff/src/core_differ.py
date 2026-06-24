# Core Diff Engine for Gendiff
# Handles the recursive comparison of two structured data objects (dicts/lists)
# without worrying about output formatting.

def calculate_diff(data1, data2):
    """
    Calculates the structural difference between two Python dictionaries.
    Returns a dictionary representing the abstract diff tree where:
    - Keys are the field names from the input data.
    - Values are dictionaries describing the change:
      {
        'status': 'added'|'deleted'|'changed'|'unchanged'|'nested',
        'old_value': ...,
        'new_value': ...,
        'children': ...
      }
    """
    if type(data1) is not type(data2):
        # For type mismatch, we treat it as a change at the root level
        # (though this case is less common for config files)
        return {'status': 'changed', 'old_value': data1, 'new_value': data2}

    diff = {}

    if isinstance(data1, dict):
        keys1 = set(data1.keys())
        keys2 = set(data2.keys())
        all_keys = keys1.union(keys2)

        for key in all_keys:
            val1 = data1.get(key)
            val2 = data2.get(key)

            if key not in keys2:
                # Key removed from file2
                diff[key] = {
                    'status': 'deleted',
                    'old_value': val1,
                    'new_value': None
                }
            elif key not in keys1:
                # Key added in file2
                diff[key] = {
                    'status': 'added',
                    'old_value': None,
                    'new_value': val2
                }
            else:
                # Key exists in both
                if isinstance(val1, dict) and isinstance(val2, dict):
                    # Both values are dictionaries -> recurse
                    nested_diff = calculate_diff(val1, val2)
                    diff[key] = {'status': 'nested', 'children': nested_diff}
                elif val1 != val2:
                    # Values are different (and not both dicts) -> changed
                    diff[key] = {
                        'status': 'changed',
                        'old_value': val1,
                        'new_value': val2
                    }
                else:
                    # Values are identical
                    diff[key] = {
                        'status': 'unchanged',
                        'old_value': val1,
                        'new_value': val2
                    }
    else:
        # Handle case where inputs are not dicts (simple values or lists)
        # For simplicity in this tool, we assume config files map to dicts
        # at top level.
        # If they are simple values and equal -> unchanged, else changed.
        if data1 == data2:
            return {
                'status': 'unchanged',
                'old_value': data1,
                'new_value': data2
            }
        else:
            return {
                'status': 'changed',
                'old_value': data1,
                'new_value': data2
            }

    return diff
