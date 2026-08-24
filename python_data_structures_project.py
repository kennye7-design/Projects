"""
Python Data Structures Utility Toolkit

A cleaned portfolio version of a Python lab focused on functions,
dictionaries, sets, loops, and basic collection manipulation.
"""

from typing import Any, Dict, Hashable, Iterable, Mapping, Set


def is_unique(mapping: Mapping[Any, Hashable]) -> bool:
    """Return True if every value in a mapping is unique."""
    seen_values = set()
    for value in mapping.values():
        if value in seen_values:
            return False
        seen_values.add(value)
    return True


def intersect(dict1: Mapping[Any, Any], dict2: Mapping[Any, Any]) -> Dict[Any, Any]:
    """Return key-value pairs that appear identically in both dictionaries."""
    result = {}
    for key, value in dict1.items():
        if key in dict2 and dict2[key] == value:
            result[key] = value
    return result


def is_1_to_1(mapping: Mapping[Any, Hashable]) -> bool:
    """Return True when no two keys map to the same value."""
    seen_values = set()
    for value in mapping.values():
        if value in seen_values:
            return False
        seen_values.add(value)
    return True


def reverse(mapping: Mapping[Any, Hashable]) -> Dict[Hashable, Set[Any]]:
    """Reverse a mapping so each original value maps to a set of original keys."""
    reversed_dict = {}
    for key, value in mapping.items():
        if value not in reversed_dict:
            reversed_dict[value] = set()
        reversed_dict[value].add(key)
    return reversed_dict


def max_length(strings: Iterable[str]) -> int:
    """Return the length of the longest string, or 0 for an empty iterable."""
    strings = list(strings)
    if not strings:
        return 0
    return max(len(s) for s in strings)


def has_odd(numbers: Iterable[int]) -> bool:
    """Return True if at least one number in the iterable is odd."""
    for number in numbers:
        if number % 2 != 0:
            return True
    return False


def symmetric_set_difference(set1: Set[Any], set2: Set[Any]) -> Set[Any]:
    """Return elements that appear in exactly one of two sets."""
    result = set()
    for element in set1:
        if element not in set2:
            result.add(element)
    for element in set2:
        if element not in set1:
            result.add(element)
    return result


def demo() -> None:
    """Run a small demonstration of each utility function."""
    print("is_unique:", is_unique({"a": 1, "b": 2, "c": 3}))
    print("intersect:", intersect({"a": 1, "b": 2}, {"a": 1, "b": 9}))
    print("is_1_to_1:", is_1_to_1({"x": "red", "y": "blue"}))
    print("reverse:", reverse({"a": 1, "b": 2, "c": 1}))
    print("max_length:", max_length({"apple", "banana", "cherry", "date"}))
    print("has_odd:", has_odd({2, 4, 6, 8, 10}))
    print("symmetric_set_difference:",
          symmetric_set_difference({1, 2, 3}, {3, 4, 5}))


if __name__ == "__main__":
    demo()
