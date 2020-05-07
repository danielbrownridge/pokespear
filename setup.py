from setuptools import setup
setup(
    name="pokespear",
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
