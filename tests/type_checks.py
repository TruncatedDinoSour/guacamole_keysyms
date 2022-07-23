import sys
from warnings import filterwarnings as filter_warnings

import guacamole_keysyms


def main() -> int:
    """Entry/main function"""

    print(guacamole_keysyms)

    return 0


if __name__ == "__main__":
    assert main.__annotations__.get("return") is int, "main() should return an integer"

    filter_warnings("error", category=Warning)
    sys.exit(main())
