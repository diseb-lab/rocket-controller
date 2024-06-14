"""Core module."""

from datetime import datetime
from typing import Any

import yaml

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


def format_datetime(time: datetime) -> str:
    """
    Format a datetime to a fixed format.

    Args:
        time: Timestamp

    Returns:
        str: Formatted time
    """
    return time.strftime("%Y_%m_%d_%Hh%Mm")


def format_filename(filename: str | None, filetype: str) -> str | None:
    """
    Format a filename, ensuring it ends with a certain filetype extension.

    Args:
        filename: Filename.
        filetype: File extension.

    Returns:
        Formatted filename.
    """
    filetype = "." + filetype if not filetype.startswith(".") else filetype
    return (
        filename + filetype
        if filename is not None and not filename.endswith(filetype)
        else filename
    )


def yaml_to_dict(
    filename: str | None, directory: str, fallback_file: str
) -> dict[str, Any]:
    """
    Read a yaml file into a dictionary.

    Args:
        filename: Name of the yaml file.
        directory: Directory where the yaml file is located.
        fallback_file: Fallback yaml file.

    Returns:
        A dictionary containing all fields in the yaml file.
    """
    formatted_fallback_file = str(format_filename(fallback_file, "yaml"))
    filename = format_filename(filename, "yaml")

    directory = directory + "/" if not directory.endswith("/") else directory
    path = directory + (formatted_fallback_file if filename is None else filename)

    with open(path, "rb") as f:
        result: dict[str, Any] = yaml.safe_load(f)
        result = result if result is not None else {}

    return result
