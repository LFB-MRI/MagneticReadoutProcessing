# in setup.py
...
requires = [
    'pyramid',
    'pyramid_chameleon', # <-- DELETE THIS LINE
    'pyramid_jinja2',
    ... # other package dependencies
]
...
tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    'tox', # you have to add this one in
]
...
setup(name='MagneticReadoutWebUI',
    version='1.0.0',
    # package metadata
    install_requires=requires,
    entry_points="""\ # Entry points are ways that we can run our code once it has been installed
    [MagneticReadoutWebUI.app_factory]
    main = MagneticReadoutWebUI:main
    """
)