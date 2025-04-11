class FDXException(Exception):
    """Base exception for all FDX-related errors.

    This exception is raised when any FDX-specific error occurs, such as:
    - Invalid FDX file format
    - Missing required elements in the FDX structure
    - Errors during parsing or manipulation of FDX content

    Examples:
        >>> try:
        ...     screenplay = read_fdx("not_a_real_fdx_file.txt")
        ... except FDXException as e:
        ...     print(f"Error: {e}")
        Error: Not a FinalDraft file.
    """
    pass
