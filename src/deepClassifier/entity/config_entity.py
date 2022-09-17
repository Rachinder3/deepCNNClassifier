from dataclasses import dataclass
from pathlib import Path


@dataclass(
    frozen=True
)  ## frozen = True makes it behave like named tuple,we won't be able to change anything
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
