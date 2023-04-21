import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from Formelsamling.Numerisk_Lineær_Algebra import *
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat, VectorName, NoEscape
from pylatex.utils import italic

geometry_options = {"tmargin": "1cm", "lmargin": "2cm"}
doc = Document(geometry_options=geometry_options)



with doc.create(Section('Opgave 9.1', False)):
    # Opgave beskrivelse:
    doc.append('Bestem mindste kvadraters løsninger i python ved hjælp af QR dekomponering beregnet via forbedret Gram-Schmidt til de følgende problemer:')
    with doc.create(Subsection('a. Find et andengrads polynomium y = ax^2 + bx + c tæt ved punkterne', False)):
        x = np.array([[0.0, 1.9, 3.1, 6.2, 7.1]])
        y = np.array([[4.1, 3.1, 2.9, 4.2, 4.8]])
        doc.append(Math(data=[VectorName('x'), Matrix(x)]))
        doc.append(Math(data=[VectorName('y'), Matrix(y)]))
        x = x[0] # Pakker x ud
        y = y[0]

        cols = 3 
        doc.append('Der er brug for 3 variabler. Dette bliver senere nyttigt, når vi laver en vander matrice.')
        doc.append('Den forbedrede Gram Schmidt bruges til at finde q & r.')
        
        a = np.vander(x, cols)
        q, r = gramSchmidt(forbedretGramSchmidt=True, a=a)
        c = q.T @ y[:, np.newaxis]

        print(c)

        koeffs, definition = back_substitution(r, c, definition = True)
        print(koeffs)
        doc.append('Ved hjælp af back substitution hvor:\n')
        doc.append(definition)
        doc.append('Findes koefficienterne til:')
        doc.append(Math(data=[Matrix(koeffs)]))

        with doc.create(Figure(position='htbp')) as plot: 
            t = np.linspace(0, 7.2, 100)
            fig, ax = plt.subplots()
            ax.plot(x, y, 'o')
            ax.plot(t, np.vander(t, cols) @ koeffs, label = "Approksimeret funktion")
            plot.add_plot(width = NoEscape(r'0.75\textwidth'))
    # + NoEscape(r'Brug\ denne\ omskrivning\ til\ at\ bestemme\ en\ cirkle\ taet\ ved\ datapunkterne'
    with doc.create(Subsection(NoEscape(r'b. Omskriv ligningen for en cirkel $$(x - a)^2 + (y - b)^2 = r^2 $$ til formen $$Ax + By + C = x^2 + y^2$$ med A, B, C kun bestemt af a, b og r.'), False)):
        x = np.array([[-1.2, -0.3, -0.7, -0.6, 1.6, 1.6,  0.1, 1.5]])
        y = np.array([[ 0.8,  1.4, -0.8, -0.5, 1.8,  -1, -0.7, -1.7]])
        
        doc.append(Math(data=[VectorName('x'), Matrix(x)]))
        doc.append(Math(data=[VectorName('y'), Matrix(y)]))
        doc.append('Giv gerne plots der illustrerer datapunkter og den fundne løsning.')
        
        x, y, a, b, r = sp.symbols('x y a b r')
        
        r = sp.sqrt((x**2 + a**2 - 2*a*x) + ( y**2 + b**2 - 2*b*y)) 
        print(sp.simplify(r))

with doc.create(Section('Opgave 9.2', False)):
    iris_dtype = np.dtype([('vals', float, (4,)), ('art', np.str_, 16)])
    vals, labels = np.loadtxt('iris.data', dtype=iris_dtype, delimiter=',', unpack=True)
    iris = vals.T
    u, s, vt = np.linalg.svd(iris, full_matrices=False)
    A = np.diag(s[:2]) @ vt[:2]
    with doc.create(Subsection('a. Hent iris blomster datasættet iris.data. Dette har data for tre forskellige arter iris blomster. Hver linje indeholder fire længdemål, samt artens navn, adskilt af kommategn.', False)): 
        doc.append('')
    
    with doc.create(Subsection('b. Indlæs data i python', False)): 
        doc.append('')
        
    
    with doc.create(Subsection(NoEscape(r'c. Bekraeft at iris er en (4 x 150) matrix af float tal. Beregn dens tynde SVD $$U \Sigma V^T$$'), False)):
        doc.append('')
        doc.append(Math(data=['iris.shape = ', iris.shape]))
        


    with doc.create(Subsection(NoEscape(r'd. Plot data fra de første 2 singulærværdier, dvs. fra de første 2 rækker i $$\sigma V^T,$$ som et scatter plot. Det burde kunne ses at der er en del af datamaengden, der skiller sig ad fra resten.'), False)):
        with doc.create(Figure(position='htbp')) as plot: 
            t = np.linspace(0, 7.2, 100)
            fig, ax = plt.subplots()
            ax.plot(*A, 'o')
            plot.add_plot(width = NoEscape(r'0.75\textwidth'))
    with doc.create(Subsection(NoEscape(r'e. Farvelæg dit plot, så man kan se hvilken art hvert datapunkt svarer til.'), False)):
        with doc.create(Figure(position='htbp')) as plot:
            fig, ax = plt.subplots()
            for lab in np.unique(labels): 
                ax.plot(*(A[:, labels == lab]), 'o')
            plot.add_plot(width = NoEscape(r'0.75\textwidth'))

    
    







"""
with doc.create(Section('Opgave', False)):
    doc.append('Some regular text and some')
    doc.append(italic('italic text. '))
    doc.append(
'''
Also some crazy characters: $&#{}
''')
    with doc.create(Subsection('Math that is incorrect')):
        doc.append(Math(data=['2*3', '=', 9]))

    with doc.create(Subsection('Table of something')):
        with doc.create(Tabular('rc|cl')) as table:
            table.add_hline() 
            table.add_row((1, 2, 3, 4))
            table.add_hline(1, 2)
            table.add_empty_row()
            table.add_row((4, 5, 6, 7))
            

a = np.array([[100, 10, 20]]).T
M = np.matrix([[2, 3, 4],
                [0, 0, 1],
                [0, 0, 2]])

with doc.create(Section('Opgave')):
    with doc.create(Subsection('Correct matrix equations')):
        doc.append(Math(data=[Matrix(M), Matrix(a), '=', Matrix(M * a)]))

    with doc.create(Subsection('Alignat math environment')):
        with doc.create(Alignat(numbering=False, escape=False)) as agn:
            agn.append(r'frac{a}{b} &= 0 \\')
            agn.extend([Matrix(M), Matrix(a), '&=', Matrix(M * a)])

    with doc.create(Subsection('Beautiful graphs')):
        with doc.create(TikZ()):
            plot_options = 'height=4cm, width=6cm, grid=major'
            with doc.create(Axis(options=plot_options)) as plot:
                plot.append(Plot(name='model', func='-x^5 - 242'))
                coordinates = [
                    (-4.77778, 2027.60977),
                    (-3.55556, 347.84069),
                    (-2.33333, 22.58953),
                    (-1.11111, -493.50066),
                    (0.11111, 46.66082),
                    (1.33333, -205.56286),
                    (2.55556, -341.40638),
                    (3.77778, -1169.24780),
                    (5.00000, -3269.56775),
                ]

                plot.append(Plot(name='estimate', coordinates=coordinates))

"""
doc.generate_pdf('Besvarelse opgave 9 ', clean_tex=True)


