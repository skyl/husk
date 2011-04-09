from setuptools import setup, find_packages

version = '0.1'
LONG_DESCRIPTION = """
=====================================
Husk
=====================================

So you don't really have to layout your directories or fill out
setup.py.
"""

setup(
    name="husk",
    version=version,
    description="husk",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='python',
    author='Skylar Saveland',
    author_email='skylar.saveland@gmail.com',
    url='http://github.com/skyl/husk',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)


