# LLM-assisted by Jules (ChatGPT Codex) / ChatGPT
# Email: 22f3001135@ds.study.iitm.ac.in
# change
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("data/quarterly_mrr_2024.csv")
OUT_DIR = Path("images")
OUT_DIR.mkdir(parents=True, exist_ok=True)

INDUSTRY_TARGET = 15.0

def main():
    df = pd.read_csv(DATA_PATH)
    df["Quarter"] = pd.Categorical(df["Quarter"], categories=['Q1', 'Q2', 'Q3', 'Q4'], ordered=True)
    df = df.sort_values("Quarter")
    avg = round(df["MRR_Growth"].mean(), 2)
    gap = round(INDUSTRY_TARGET - avg, 2)

    print("=== Quarterly MRR Growth (2024) ===")
    print(df.to_string(index=False))
    print(f"Average MRR Growth: {avg}")
    print(f"Industry Target: {INDUSTRY_TARGET}")
    print(f"Gap to Target: {gap}")

    # Line chart vs benchmark
    plt.figure()
    plt.plot(df["Quarter"], df["MRR_Growth"], marker="o")
    plt.axhline(INDUSTRY_TARGET, linestyle="--")
    plt.title("MRR Growth (2024) vs Industry Target")
    plt.xlabel("Quarter")
    plt.ylabel("MRR Growth")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "mrr_line_vs_target.png", dpi=200)
    plt.close()

    # Bars per quarter with target line
    plt.figure()
    plt.bar(df["Quarter"], df["MRR_Growth"])
    plt.axhline(INDUSTRY_TARGET, linestyle="--")
    plt.title("Quarterly MRR Growth (2024)")
    plt.xlabel("Quarter")
    plt.ylabel("MRR Growth")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "mrr_bars_vs_target.png", dpi=200)
    plt.close()

if __name__ == "__main__":
    main()
