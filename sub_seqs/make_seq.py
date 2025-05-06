import numpy as np
import pandas as pd
import argparse

def gen_dur_seq(n_trl, low=600, high=1800, step=16.67):
    """
    Generate two duration sequences:
      w1 – a low‐stochasticity random walk scaled into [low, high]
      w2 – a high‐stochasticity version (random shuffle of w1)
    Durations are rounded to the nearest `step` (ms).

    Returns
    -------
    w1, w2 : np.ndarray, np.ndarray
        Arrays of length n_trl with integer durations in ms.
    """
    w = np.cumsum(np.random.randn(n_trl)) # random walk
    w = (w - w.mean()) / w.std() # standardize
    w = (w - w.min()) / (w.max() - w.min())  # now in [0,1]
    w = w * (high - low) + low # scale to [low, high]
    w1 = (np.round(w / step) * step).astype(int)  # round to nearest step 
    w2 = np.random.permutation(w1)

    return w1, w2

def make_sequence(n_trl=100, outfile='durations.csv'):
    """
    Build a single sequence by combining low‐ and high‐stochasticity blocks,
    shuffling trial order, and exporting to CSV with columns:
      trlno, duration, stochasticity
    """
    # generate blocks
    w1, w2 = gen_dur_seq(n_trl)

    # randomly choose block order
    if np.random.rand() < 0.5:
        # low then high
        durations = np.concatenate([w1, w2])
        labels    = np.array(['low'] * n_trl + ['high'] * n_trl)
    else:
        # high then low
        durations = np.concatenate([w2, w1])
        labels    = np.array(['high'] * n_trl + ['low'] * n_trl)

    # build DataFrame
    df = pd.DataFrame({
        'trlno':         np.arange(1, 2*n_trl + 1),
        'duration_ms':   durations,
        'stochasticity': labels
    })
    df.to_csv(outfile, index=False)
    
    print(f"Exported {len(df)} trials to '{outfile}'")

    return df
def main():
	p = argparse.ArgumentParser(
	description="Generate low/high-stochasticity duration blocks and save to CSV"
    )
	p.add_argument("--n_trl",   type=int,   default=100,
                   help="number of trials per block (default: 100)")
	p.add_argument("--outfile", type=str,   default="durations.csv",
                   help="output CSV file (default: durations.csv)")
	args = p.parse_args()
    # generate and export sequence
	make_sequence(n_trl = args.n_trl, outfile=args.outfile)

if __name__ == '__main__':
	main()