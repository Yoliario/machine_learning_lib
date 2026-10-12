"""Модуль кластеризации."""


def nearest_center(x, centers):
    """Индекс ближайшего к точке x центра кластера."""
    return min(range(len(centers)), key=lambda i: abs(x - centers[i]))


def cluster_sizes(labels):
    """Количество точек в каждом кластере."""
    return {label: labels.count(label) for label in labels
