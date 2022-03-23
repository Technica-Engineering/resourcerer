class UnknownCachingStrategy(Exception):
    """Raised when an unknown caching strategy is used"""
    pass


class UknownSource(Exception):
    """Raised when the source has no implemented driver"""
    pass
