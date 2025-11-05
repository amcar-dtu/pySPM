import importlib.metadata

try:
    __version__ = importlib.metadata.version("pyspm")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"
