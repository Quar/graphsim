import os
from setuptools import setup, find_packages

# build libtacsim automatically
rootdir = os.path.dirname(os.path.realpath('__file__'))
moddir = os.path.join(rootdir, 'libtacsim')
os.system('cd %s; scons install; cd -' % moddir)

setup(
    name = "graphsim",
    version = '0.2.6.8',
    url = 'https://github.com/caesar0301/graphsim',
    author = 'Xiaming Chen',
    author_email = 'chenxm35@gmail.com',
    description = 'Graph similarity algorithms based on NetworkX.',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    license = "BSC License",
    packages = find_packages(),
    keywords = ['graph', 'graph similarity', 'graph matching'],
    install_requires=[
          'networkx >= 1.11',
          'typedecorator >= 0.0.4',
          'decorator >= 4.0.10',
          'numpy >= 1.12.1'
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: Freely Distributable',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Software Development :: Libraries :: Python Modules',
   ],
)
