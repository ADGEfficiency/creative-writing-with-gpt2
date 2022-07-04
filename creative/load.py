from pathlib import Path


def load_models(base: Path=Path.cwd()):
    return [p for p in (base / 'models').iterdir() if p.is_dir()]


def load_last_checkpoint(model):
    checkpoints = [p for p in model.iterdir() if p.is_dir() and 'checkpoint' in str(p)]
    assert len(checkpoints) > 0, "No checkpoint found!"
    return list(sorted(checkpoints))[-1]
