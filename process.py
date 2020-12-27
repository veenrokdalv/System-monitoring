import psutil


class SystemMonitoring:

    def __init__(self):
        super(SystemMonitoring, self).__init__()
        self.prefixes = ['', 'K', 'M', 'G', 'T']
    
    def get_size_memory(self, bytes: int, suffix: str = 'B') -> tuple:
        """Returns the formatted number of bytes of
        kilobytes, megabytes, gigabytes, terabytes, petabytes.

        Args:
            bytes (int): Count bytes
            suffix (str, optional): suffix byte. Defaults to 'B'.

        Returns:
            [typle]: (number, prefix)

        """

        factor = 1024
        for unit in self.prefixes:
            if bytes < factor:
                return (round(bytes, 2), unit)
            bytes /= factor
    
    def get_total_memory(self):
        virtual_memory = psutil.virtual_memory()
        return self.get_size_memory(virtual_memory.total)
    
    def get_used_memory(self):
        virtual_memory = psutil.virtual_memory()
        return self.get_size_memory(virtual_memory.used)
    
    def get_availabel_memory(self):
        virtual_memory = psutil.virtual_memory()
        return self.get_size_memory(virtual_memory.available)
