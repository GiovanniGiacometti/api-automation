def get_scope_url(scope: str) -> str:
    """
    Returns the URL for the given scope.

    Args:
        scope (str): The scope to get the URL for.

    Returns:
        str: The URL for the given scope.
    """
    return f"https://www.googleapis.com/auth/{scope}"
