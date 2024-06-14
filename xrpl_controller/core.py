"""Core module."""

from datetime import datetime

# The delay value which indicated a drop. This is the max value of an u32 datatype in Rust.
MAX_U32 = 2**32 - 1


def flatten(xss: list[list[int]]) -> list[int]:
    """
    Flatten a 2D list.

    Args:
        xss: A 2D integer list to be flattened.

    Returns:
        list[int]: A flattened list.
    """
    return [x for xs in xss for x in xs]


def validate_ports(port_1: int, port_2: int):
    """
    Validate whether 2 ports are not equal to each other.

    Args:
        port_1: Port 1
        port_2: Port 2

    Raises:
        ValueError: if the ports are equal or if any of the ports are negative.
    """
    if port_1 < 0 or port_2 < 0:
        raise ValueError("Ports must be non-negative")

    if port_1 == port_2:
        raise ValueError(
            f"Received ports can not be equal to each other, value: {port_1}."
        )


def validate_ids(id_1: int, id_2: int):
    """
    Validate whether 2 ports are not equal to each other.

    Args:
        id_1: ID 1
        id_2: ID 2

    Raises:
        ValueError: if the ports are equal or if any of the ports are negative.
    """
    if id_1 < 0 or id_2 < 0:
        raise ValueError("ID's must be non-negative")

    if id_1 == id_2:
        raise ValueError(
            f"Received ID's can not be equal to each other, value: {id_1}."
        )


def format_datetime(time: datetime) -> str:
    """
    Format a datetime to a fixed format.

    Args:
        time: Timestamp

    Returns:
        str: Formatted time
    """
    return time.strftime("%Y_%m_%d_%Hh%Mm")
