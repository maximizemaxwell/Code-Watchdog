# src/dataset/data_loader.py
from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

import numpy as np
import polars as pl
from huggingface_hub import hf_hub_download
from sklearn.model_selection import train_test_split

REPO_ID = "basakdemirok/AIGCodeSet"
CSV_FILES = ["data/created_dataset_with_llms.csv", "data/human_selected_dataset.csv"]


def _download_csvs(repo: str = REPO_ID, csvs: List[str] = CSV_FILES) -> List[Path]:
    # Download CSV files from the Hugging Face Hub
    return [Path(hf_hub_download(repo_id=repo, filename=csv)) for csv in csvs]


def load_code_llm_dataset(
    test_size: float = 0.2,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, pl.DataFrame]:
    """
    Load the Code LLM dataset from the Hugging Face Hub.
    """
    paths = _download_csvs()
    df_list = []
    for path in paths:
        df = pl.read_csv(path, columns=["code", "llm"])
        df_list.append(df)

    df_all: pl.DataFrame = pl.concat(df_list, how="vertical")

    codes = df_all["code"].to_numpy()
    llms = df_all["llm"].to_numpy()

    codes_tr, codes_val, llms_tr, llms_val = train_test_split(
        codes, llms, test_size=test_size, stratify=llms, random_state=seed
    )

    return codes_tr, codes_val, llms_tr, llms_val, df_all
