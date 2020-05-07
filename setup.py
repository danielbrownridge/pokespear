from setuptools import setup
setup(
    name="pokespear",
    entry_points={
        "console_scripts": [
            "pokespear=pokespear.command_line:main"
        ],
    },
    packages=[
        "pokespear",
    ],
    package_dir={
        "": "src"
    },
    use_scm_version=True,
    setup_requires=[
        "setuptools_scm",
    ]
)
