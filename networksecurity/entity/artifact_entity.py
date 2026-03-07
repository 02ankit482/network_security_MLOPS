from dataclasses import dataclass

#document why we need datclasses

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str