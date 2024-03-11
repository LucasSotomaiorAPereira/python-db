from enum import Enum


class OrderStatus(Enum):
    CREATED = 1
    PAID = 2
    DELIVERED = 3
    CANCELED = 4
