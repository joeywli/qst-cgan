#!/usr/bin/env python
from setuptools import setup


requires = ["tensorflow", "qutip", "tqdm"]

setup(
    name="qst_cgan",
    version="0.0.1",
    description="Quantum state tomography with conditional generative adversarial networks",
    author="Shahnawaz Ahmed",
    author_email="shahnawaz.ahmed95@gmail.com",
    packages=["qst_cgan"],
    install_requires=requires,
)
