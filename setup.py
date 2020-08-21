import io

from setuptools import find_packages
from setuptools import setup

# with io.open("README.md", "rt", encoding="utf8") as f:
#     readme = f.read()

setup(
    name="sport",
    version="1.0.0",
    url="https://sport.techtapir.com",
    license="BSD",
    maintainer="Dallan Bhatti",
    maintainer_email="dallan.bhatti@techtapir.com",
    description="SPORT Microservice",
    # long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest", "coverage"]},
)
