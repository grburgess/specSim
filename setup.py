from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

ext_modules = [Extension("sampler", ["sampler.pyx"]),Extension("evo", ["evo.pyx"])]
setup(
    name = 'sampler module',
    cmdclass = {'build_ext': build_ext},
    ext_modules = cythonize(ext_modules)
)
