import setuptools

setuptools.setup(
    name="XYZDryZoneTV",
    version="2022.07.23.12.22",
    author="WillEE",
    url="https://github.com/WillEEEEEE/XYZDryZoneTV.git",
    packages=setuptools.find_packages(),
    package_data={
        '': ['**/*.ini', '**/*.json']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
