"""Модуль кластеризации."""


def nearest_center(x, centers):
    """Индекс ближайшего к точке x центра кластера."""
    return min(range(len(centers)), key=lambda i: abs(x - centers[i]))
