def is_even(number: int) -> bool:
    return number % 2 == 0


def calculate_total(prices: list[float]) -> float:
    return sum(prices)


def apply_discount(price: float, percentage: float) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100")
    return round(price * (1 - percentage / 100), 2)
