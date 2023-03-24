from sympy import *
from matplotlib.backends.backend_pgf import PdfPages
import matplotlib.pyplot as plt


plt.rcParams.update({
    'text.usetex': True,
    "pgf.texsystem": "pdflatex",
    "pgf.preamble": "\n".join([
         r"\usepackage[utf8x]{inputenc}",
         r"\usepackage[T1]{fontenc}",
         r"\usepackage{cmbright}",
    ]),
})
print(r'$\alpha')



s, t, K = symbols('s t K')

