import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-fdx",
    version="1.0.0",
    author="Guilherme Gama",
    author_email="guilhermegama@gmail.com",
    description="FDX Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/busdriverbuddha/python-fdx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Video",
        "Topic :: Text Processing :: Markup :: XML",
    ],
    python_requires=">=3.10",
)
