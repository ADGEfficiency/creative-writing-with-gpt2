"""load a model checkpoint"""
from pathlib import Path
from typing import List


def load_models(base: Path = Path.cwd()) -> List[Path]:
    return [p for p in (base / "models").iterdir() if p.is_dir()]


def load_last_checkpoint(model) -> List[Path]:
    checkpoints = [p for p in model.iterdir() if p.is_dir() and "checkpoint" in str(p)]
    assert len(checkpoints) > 0, "No checkpoint found!"
    return list(sorted(checkpoints))[-1]
