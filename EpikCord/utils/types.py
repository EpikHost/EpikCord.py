from enum import IntEnum
from typing import Any, Callable, Coroutine

AsyncFunction = Callable[..., Coroutine[Any, Any, Any]]
