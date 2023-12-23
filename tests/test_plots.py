from matplotlib import pyplot as plt

from stable_baselines3.common.results_plotter import plot_results


def test_plot_results_creates_figure_on_pyplot_stack():
    plot_results(dirs=['./files'])
    assert len(plt.get_fignums()) == 1
