from ..logging import get_logger


class BaseModule(object):
    """Base class for all modules."""

    def __init__(self, config):
        self._logger = None

    def get_all_commands(self):
        """Should return a list of strings containing all commands supported by
        this module. Used to generate a help message.
        """
        return []

    def start(self):
        """Called when the module is loaded."""
        pass

    def stop(self):
        """Called when the module is unloaded. Here you can for example stop the
        execution of all threads the module has created and wait for them to
        finish before returning.
        """
        pass

    @property
    def logger(self):
        if not self._logger:
            self._logger = get_logger(self)
        return self._logger
