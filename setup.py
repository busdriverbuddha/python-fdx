import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-fdx-busdriverbuddha",
    version="0.1dev",
    author="Guilherme Gama",
    author_email="guilhermegama@gmail.com",
    description="FDX Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/busdriverbuddha/python-fdx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # TODO: complete licenses and OS
    ],
    python_requires=">=3.8",
)

