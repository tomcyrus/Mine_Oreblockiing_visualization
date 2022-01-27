import pandas as pd
import volpy as vp

survey = vp.load_survey(r'C:\Users\ECHELON\Desktop\raw_data3.csv')
mesh = vp.terrain_mesh(survey.data)
survey.get_bounds()

# Survey plots
plots = vp.terrain_plots(survey)
plots.scatter3d()
plots.contour()
plots.profile()
plots.mesh_plot()
vol_curves = mesh.get_volume_curves(step=1.0)
mesh.plot_curves(vol_curves)

# Just a volume from the mesh
mesh.get_volume()
