"""
Print (some) Dunder methods.

These are special methods that start and end with double underscores.
"""

import sys


def main() -> None:
    print(f"annotations: {__annotations__}")
    print(f"builtins: {__builtins__}")
    print(f"cached: {globals().get('__cached__', 'Not defined')}")
    print(f"doc: {__doc__}")
    print(f"file: {__file__}")
    print(f"loader: {globals().get('__loader__', 'Not defined')}")
    print(f"name: {__name__}")
    print(f"package: {__package__}")
    print(f"spec: {__spec__}")

    sys.exit(0)


if __name__ == "__main__":
    main()
