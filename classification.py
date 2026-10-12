"""Модуль классификации."""


def predict_label(x, threshold=0.5):
    """Пороговый классификатор: 1, если x >= threshold, иначе 0."""
    return 1 if x >= threshold else 0
