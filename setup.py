"""
Setup of pyrender Python codebase.

Author: Matthew Matl
Maintainer: Zirui Zhang
"""
import sys
from setuptools import setup

# load __version__
exec(open('pyrender/version.py').read())
__version__ = locals()['__version__']

def get_imageio_dep():
    if sys.version[0] == "2":
        return 'imageio<=2.6.1'
    return 'imageio'

requirements = [
    'freetype-py',                # For font loading
    get_imageio_dep(),            # For Image I/O
    'networkx',                   # For the scene graph
    'numpy',                      # Numpy
    'Pillow',                     # For Trimesh texture conversions
    'pyglet>=1.4.10',             # For the pyglet viewer
    'PyOpenGL~=3.1.0',            # For OpenGL
    'scipy',                      # Because of trimesh missing dep
    'six',                        # For Python 2/3 interop
    'trimesh',                    # For meshes
]

dev_requirements = [
    'flake8',            # Code formatting checker
    'pre-commit',        # Pre-commit hooks
    'pytest',            # Code testing
    'pytest-cov',        # Coverage testing
    'PyVirtualDisplay',  # For headless testing
    'tox',               # Automatic virtualenv testing
    'xvfbwrapper',       # For headless testing
]

docs_requirements = [
    'sphinx',            # General doc library
    'sphinx_rtd_theme',  # RTD theme for sphinx
    'sphinx-automodapi'  # For generating nice tables
]


setup(
    name = 'pyrender',
    version=__version__,
    description='Easy-to-use Python renderer for 3D visualization',
    long_description='A simple implementation of Physically-Based Rendering '
                       '(PBR) in Python. Compliant with the glTF 2.0 standard.',
    author='Matthew Matl',
    author_email='matthewcmatl@gmail.com',
    maintainer="Zirui Zhang",
    maintainer_email="zhangzrjerry@outlook.com",
    license='MIT License',
    url = 'https://github.com/mmatl/pyrender',
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering'
    ],
    keywords = 'rendering graphics opengl 3d visualization pbr gltf',
    packages = ['pyrender', 'pyrender.platforms'],
    setup_requires = requirements,
    install_requires = requirements,
    extras_require={
        'dev': dev_requirements,
        'docs': docs_requirements,
    },
    include_package_data=True
)
