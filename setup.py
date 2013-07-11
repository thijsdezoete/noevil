from distutils.core import setup

setup(
        name="noeval",
        version="1.0",
        description="No eval anymore",
        long_description="This package removes eval from the global scope. Any call to eval will be pass'ed.",
        author="Thijs de Zoete",
        author_email="t@ht5ml.com",
        url="https://www.github.com/thijsdezoete/noevil",
        packages=["noeval"]
)
