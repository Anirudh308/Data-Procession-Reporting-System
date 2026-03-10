"""
Custom Exception Classes

All DPRS-specific exceptions are defined here.
"""


class DPRSException(Exception):
    """Base exception for all DPRS errors."""
    pass


class FileNotFoundError(DPRSException):
    """Raised when input file does not exist."""
    pass


class InvalidFileTypeError(DPRSException):
    """Raised when file format is not CSV or JSON."""
    pass


class SchemaValidationError(DPRSException):
    """Raised when data schema validation fails."""
    pass


class DataProcessingError(DPRSException):
    """Raised when a processing operation fails."""
    pass


class DataIntegrityError(DPRSException):
    """Raised when data validation fails."""
    pass


class InvalidArgumentError(DPRSException):
    """Raised when invalid CLI arguments are provided."""
    pass
