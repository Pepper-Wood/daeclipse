"""Model to represent DeviantArt Eclipse Deviation Stats."""


class Stats(object):
    """Model to represent DeviantArt Eclipse Deviation Stats."""

    def __init__(self, input_dict=None):
        """Initialize Stats.

        Args:
            input_dict (dict, optional): Dict of Stats class attrs.
        """
        self.comments = None
        self.favourites = None
        if input_dict is not None and isinstance(input_dict, dict):
            self.from_dict(input_dict)

    def from_dict(self, input_dict):
        """Convert input_dict values to class attributes.

        Args:
            input_dict (dict): Dict containing Stats fields.
        """
        if input_dict is None:
            return
        self.comments = input_dict.get('comments')
        self.favourites = input_dict.get('favourites')
