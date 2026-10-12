"""Оценка качества моделей."""


def mae(y_true, y_pred):
    """Средняя абсолютная ошибка (MAE)."""
    return sum(abs(t - p) for t, p in zip(y_true, y_pred)) / len(y_true)
