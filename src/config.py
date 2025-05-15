from dataclasses import dataclass


@dataclass
class Config:
    epochs: int = 50
    latent: int = 8
    alpha_fusion: float = 0.6
    seed: int = 42
    code_ds: str = "basakdemirok/AIGCodeset"
    keystroke_ds: str = "dishamodi/Keystroke_Processed"
