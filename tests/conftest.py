import importlib
import os
from types import ModuleType

import pytest


@pytest.fixture
def lesson_module():
    def load(number: int) -> ModuleType:
        package = (
            "solutions"
            if os.environ.get("GRAPH_STUDY_SOLUTIONS") == "1"
            else "exercises"
        )
        return importlib.import_module(f"{package}.lesson_{number:02d}")

    return load
