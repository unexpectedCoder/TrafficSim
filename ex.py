class Ex(Exception):
    """Базовый класс исключений для данной программы."""

    def __init__(self, **kwargs):
        self._src = kwargs['src'] if 'src' in kwargs else None
        self._txt = kwargs['txt'] if 'txt' in kwargs else None

    @property
    def message(self) -> str:
        """Сообщение исключения."""
        res = f"\tИСКЛЮЧЕНИЕ {self.__class__.__name__}"
        if self._src:
            res += f" из '{self._src}'"
        if self._txt:
            res += f": {self._txt}"
        return res + "!"


class ValueExpectedException(Ex):
    """Исключение типа "ожидалось одно, получено другое"."""

    def __init__(self, expected: str, got: str, **kwargs):
        kwargs['txt'] = f"ожидалось {expected}, получено {got}"
        Ex.__init__(self, **kwargs)
