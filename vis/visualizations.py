from pathlib import Path

def make_figures(final_path, preds_path):
    fig = Path("data/outputs/fig1.png")
    fig.touch()
    return fig

