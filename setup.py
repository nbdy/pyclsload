from setuptools import setup, find_packages

setup(
    long_description=open("README.md", "r").read(),
    name="pyclsload",
    version="1.4",
    description="importlib wrapper, instantiate class dynamically in one line",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    url="https://github.com/smthnspcl/pwnpy",
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(),
    long_description_content_type="text/markdown",
)
