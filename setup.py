import setuptools

pkg_name="spikewidgets"

setuptools.setup(
    name=pkg_name,
    version="0.1.0",
    author="Jeremy Magland",
    author_email="jmagland@flatironinstitute.org",
    description="Python widgets for use with spike sorting and electrophysiology",
    url="https://github.com/magland/spikewidgets",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'ipython',
        'vdom',
        'ipywidgets'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    )
)