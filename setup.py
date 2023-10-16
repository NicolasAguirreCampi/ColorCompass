from setuptools import setup, find_packages

setup(
    name='colorcompass',
    version='1.1.1',
    packages=find_packages(),
    install_requires=[],
    author='Nicolas Aguirre Campi',
    author_email='aguirrecampi.nicolas@gmail.com',
    description='A brief description of your project.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/NicolasAguirreCampi/ColorCompass',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
