"""Вспомогательные вычисления."""


def mean(values):
    """Среднее арифметическое списка чисел."""
    return sum(values) / len(values)


def variance(values):
    """Дисперсия списка чисел."""
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / len(values)


def std(values):
    """Стандартное отклонение."""
    return variance(values) ** 0.5
