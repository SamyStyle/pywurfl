from setuptools import setup
import os.path

# Pau Aliagas was a major contributor to this effort
# Thanks

__author__ = "Sven Mayer <mayer1802@gmial.com>"
__contributors__ = "Pau Aliagas <pau@newtral.org>; Armand Lynch <lyncha@users.sourceforge.net>"
__copyright__ = "Copyright 2015-2017, Sven Mayer"
__license__ = "LGPL"
__url__ = "https://github.com/SamyStyle/pywurfl/"
__version__ = "7.2.2"
__doc__ = \
"""
pywurfl - Python tools for processing and querying the Wireless Universal Resource File (WURFL)
"""


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


doc = __doc__.strip()

setup (name="pywurfl",
       version=__version__,
       author="Armand Lynch",
       author_email="lyncha@users.sourceforge.net",
       contact="Sven Mayer",
       contact_email="mayer1802@gmial.com",
       license=__license__,
       url=__url__,
       packages=['pywurfl', 'pywurfl.algorithms', 'pywurfl.algorithms.wurfl'],
       scripts=['bin/wurfl2python.py'],
       description=doc,
       long_description=read('doc/README'),
       install_requires=['python-Levenshtein'],
       platforms="All",
       classifiers=['Development Status :: 5 - Production/Stable',
                    'Environment :: Console',
                    'Environment :: Web Environment',
                    'Intended Audience :: Developers',
                    'Intended Audience :: Telecommunications Industry',
                    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                    'Natural Language :: English',
                    'Operating System :: OS Independent',
                    'Programming Language :: Python',
                    'Topic :: Database :: Front-Ends',
                    'Topic :: Internet :: WAP',
                    'Topic :: Software Development :: Libraries :: Python Modules',
                    'Topic :: Utilities'
                    ])
