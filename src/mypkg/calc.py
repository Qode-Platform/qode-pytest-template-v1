"""Trivial code under test — replace with the real package."""

from collections.abc import Iterable


def divide(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ZeroDivisionError("denominator must be non-zero")
    return numerator / denominator


def running_total(values: Iterable[float]) -> list[float]:
    total = 0.0
    out: list[float] = []
    for value in values:
        total += value
        out.append(total)
    return out
