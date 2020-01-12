
import matplotlib.pyplot as plt
import numpy as np

import experimentdataprocessing as edp
import experimentdatadisplay as edd
import perfeval

# ----- 0 - Data loading and pre-processing + Display of generic info -----
expe4 = edp.load_experiment_once_a_day("./expe_data/", force_reload=False)
print(expe4)
expe4.precompute_adjusted_s()
#edd.plot_age_and_sex(expe4)

# ----- 1 - Display of one subject performance (in interactive plot windows) -----
subject_index = -1  # -1 to disable per-subject data visualization
if (subject_index >= 0) and (subject_index < len(expe4.subjects)):
    subject_curves_visualizer = edd.SubjectCurvesVisualizer(expe4, subject_index, show_radio_selector=True)
    subject_perf_visualizer = edd.SubjectPerformancesVisualizer(expe4, subject_index, show_radio_selector=True)
# 1 bis Save all curve/perf figures to PDF files
# edd.save_all_subjects_to_pdf(expe4)

# ----- 2 - Analysis of performance evaluation function -----
perfs_analyzer = perfeval.Analyzer(expe4)
perfs_analyzer.plot_adjusted_perf_only()
#perfs_analyzer.compare_adjusted([perfeval.EvalType.INGAME, perfeval.EvalType.ADJUSTED_NORM2, perfeval.EvalType.ADJUSTED])
#perfs_analyzer.compare_adjusted()  # default: comparison of best chosen functions

# ----- 3 - Display of global performance results -----
# ----- ----- 3 a) Sorted by method only (p-values not displayed, always very close to 0.0)
# edd.all_perfs_histogram(expe4, perf_eval_type=perfeval.EvalType.INGAME)
# edd.all_perfs_histogram(expe4, perf_eval_type=perfeval.EvalType.FOCUS_ON_ERROR)
# edd.all_perfs_histogram(expe4, perf_eval_type=perfeval.EvalType.FOCUS_ON_TIME)
edd.all_perfs_histogram(expe4, display_KS=False)  # default: adjusted perf eval
# edd.all_perfs_violinplots(expe4, perf_eval_type=perfeval.EvalType.INGAME)
# edd.all_perfs_violinplots(expe4)  # default: adjusted perf eval
# ----- ----- 3 b) Sorted by method and by synth ID
# edd.plot_all_perfs_per_synth(expe4, perf_eval_type=perfeval.EvalType.INGAME)
edd.plot_all_perfs_per_synth(expe4)
# edd.plot_all_perfs_histograms_by_synth(expe4, display_tests=True)
# ----- ----- 3 c) Sorted by method and expertise level
# edd.plot_all_perfs_by_expertise(expe4, perfeval.EvalType.INGAME)
# edd.plot_all_perfs_by_expertise(expe4, perfeval.EvalType.FOCUS_ON_TIME)
# edd.plot_all_perfs_by_expertise(expe4, perfeval.EvalType.FOCUS_ON_ERROR)
# edd.plot_all_perfs_by_expertise(expe4, perfeval.EvalType.ADJUSTED, add_swarm_plot=True)
# ----- ----- 3 d) MEAN perfs, sorted by method and expertise level
# edd.fit_perf_vs_expertise(expe4, perf_eval_type=perfeval.EvalType.INGAME)
#edd.fit_perf_vs_expertise(expe4, perf_eval_type=perfeval.EvalType.ADJUSTED, show_fit_analysis=True)
# edd.fit_perf_vs_expertise(expe4, perf_eval_type=perfeval.EvalType.FOCUS_ON_TIME)
# edd.fit_perf_vs_expertise(expe4, perf_eval_type=perfeval.EvalType.FOCUS_ON_ERROR)

# ----- 4 - Others -----
edd.plot_opinions_on_methods(expe4)

# ----- 5 - Show all previously built figures -----
plt.show()
