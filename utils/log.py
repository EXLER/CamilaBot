from datetime import datetime


class Colors:
    BLUE = "\033[38;5;15m"
    RED = "\033[38;5;9m"
    YELLOW = "\033[38;5;226m"
    END = "\033[0m"


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def error(message: str):
    print(f"{Colors.RED}{now()} [Camila-bot] {message}{Colors.END}")


def warn(message: str):
    print(f"{Colors.YELLOW}{now()} [Camila-bot] {message}{Colors.END}")


def info(message: str):
    print(f"{Colors.BLUE}{now()} [Camila-bot] {message}{Colors.END}")


def debug(message: str):
    print(f"{now()} [Camila-bot] {message}")
