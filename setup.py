from setuptools import setup
from pathlib import Path

from lightkube.models import __version__


setup(
    name='lightkube-models-pydantic',
    version=__version__,
    description='Models and Resources for lightkube module based from Pydantic',
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author='Andrew Womeldorf',
    author_email='andrew.womeldorf@gmail.com',
    license='MIT License',
    url='https://github.com/andrew.womeldorf/lightkube-models-pydantic',
    packages=['lightkube.models', 'lightkube.resources'],
    install_requires=["pydantic"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)
