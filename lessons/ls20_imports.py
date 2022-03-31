"""Examples of importing Python."""

from lessons import ls16_helpers

# Alias a module / imported name as another name
from lessons import ls16_helpers as hp

# Import names defined globally in a module
from lessons.ls16_helpers import powerful, THE_ANSWER

def main() -> None:
    """Entrypoint of program."""
    print(ls16_helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(2, 4))
    print(THE_ANSWER)

if __name__ ==  "__main__":
    main()