"""Sample package."""


def test_function() -> str:
    """Returns a test string"""

    return "This is a test"


def cli() -> None:
    """CLI interface"""
    print("Hello, this is a sample command.")


def main() -> None:
    """Main function"""
    print("Hello, you just ran this as a package.")
