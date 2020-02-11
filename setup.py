from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()


REQUIRED = [

"numpy",
"pandas"

]

setup(
    name="mypackage",
    version="0.1",
    author="Maria Yasar",
    author_email="hello@mariayasar.com",
    description="Example package for lambda school DS Unit 3",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/mariayasar/mypackage",
    keywords="data science",
    packages=find_packages() # ["my_lambdata"]
)