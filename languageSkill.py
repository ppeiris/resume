#!/usr/bin/env python

import operator
import numpy as np
import pylab as pl


width = -0.1
barwidth = 0.7
pl.figure(figsize=(7, 6))
skillsPrograming = {
        'PHP (5.x)': 8,
        'Python(numpy,scipy)': 5,
        'C/C++': 9,
        'JavaScript': 7,
        'CoffeeScript': 2,
        'HTML': 10,
        'Mathematica': 6,
        'LaTeX': 7,
        'MATLAB': 2,
        'SQL': 10,
        'Swift': 0.5
}
skill_Programming_Index = np.arange(len(skillsPrograming))
skillsPrograming = sorted(skillsPrograming.items(), key=operator.itemgetter(0))
lanNames = [x[0] for x in skillsPrograming]
lanYears = [x[1] for x in skillsPrograming]

plot2 = pl.subplot(1,1,1)
pl.xticks(())
pl.yticks(())

plot2.set_title('Programing Experience')
plot2.set_xticks(skill_Programming_Index+width)
plot2.set_xticklabels(lanNames, rotation = 80)
plot2.set_xlim([-0.5, len(lanNames) - 0.5])
plot2.set_ylim([0,max(lanYears) + 0.1])
plot2.set_ylabel('Years')
plot2.set_yticks(lanYears)
pl.bar(skill_Programming_Index, lanYears, align="center", width=barwidth, alpha=1, color='gray')
pl.tight_layout()
pl.savefig('lanexp.pdf', bbox_inches = 'tight', format='pdf')
