from setuptools import setup, find_packages

VERSION = '1.0.0'
NAME = "pygame_animation"
AUTHOR = "FrickTzy (Kurt Arnoco)"
DESCRIPTION = 'A package for managing animations of pygame surfaces'

with open("README.md", "r") as file:
    long_description = file.read()

URL = 'https://github.com/FrickTzy/Pygame-Animation'

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    url=URL,
    keywords=['python', 'pygame', 'python game', 'python game development',
              'pygame animations', 'python animations', 'pygame animation'],
)