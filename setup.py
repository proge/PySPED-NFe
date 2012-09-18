from distutils.core import setup

setup(
    name = "PySPED-NFe",
    packages = [
        'pysped_nfe', 'pysped_nfe.leiaute', 'pysped_nfe.danfe',
        'pysped_nfe.manual_300', 'pysped_nfe.manual_401',
        'pysped_nfe.relato_sped',
        ],
    package_data = {
        'pysped_nfe.danfe': ['fonts/*'],
        'pysped_nfe.leiaute': ['schema/*/*'],
        'pysped_nfe.relato_sped': ['fonts/*'],
        },
    version = "0.0.1",
    description = "Library for SPED NF-e manipulation",
    author = "Daniel Hartmann",
    author_email = "daniel@proge.com.br",
    url = "https://github.com/proge/PySPED-NFe",
    download_url = "https://nodeload.github.com/proge/PySPED-NFe/tarball/v0.0.1",
    keywords = ["sped", "brazil", "brasil", "nfe"],
    install_requires=['PySPED-Tools'],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        ],
    long_description = """\
PySPED NF-e
-----------

NF-e is part of the Brazilian public system of digital bookkeeping (SPED).

This module allows the user to manipulate NF-e by sending, canceling, checking
status, etc.
"""
)