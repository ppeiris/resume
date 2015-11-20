#!/usr/bin/env python

import operator
import numpy as np
import pylab as pl

width = -0.1
barwidth = 0.7
pl.figure(figsize=(7, 6.5))

frameworks = {
    'Zend Framework 1': 4,
    'Zend Framework 2': 3,
    'Backbone.js': 3.5,
    'Marionette.js': 1.5,
    'Bootstrap (CSS3)': 3,
    'Apigility (REST + RPC)': 2,
    'MATLAB': 4,
    'Doctrine ORM 2.x': 2.5,
    'Angular.js': 0.5,
    'Handlebars.js': 2,
    'PHPUnit + Codeception': 4
}
framework_Index = np.arange(len(frameworks))
frameworks = sorted(frameworks.items(), key=operator.itemgetter(0))
frameworkNames = [y[0] for y in frameworks]
frameworksYears = [y[1] for y in frameworks]
plt1 = pl.subplot(1, 1, 1)
pl.xticks(())
pl.yticks(())
plt1.set_title('Framework Experience')
plt1.set_xticks(framework_Index+width)
plt1.set_xticklabels(frameworkNames, rotation = 80)
plt1.set_xlim([-0.5, len(frameworkNames) - 0.5])
plt1.set_ylim([0,max(frameworksYears) + 0.1])
plt1.set_ylabel('Years')
plt1.set_yticks(frameworksYears)
pl.bar(framework_Index, frameworksYears, align="center", width=barwidth, alpha=1, color='gray')
pl.tight_layout()
pl.savefig('frameworkexp.pdf', bbox_inches = 'tight', format='pdf')
