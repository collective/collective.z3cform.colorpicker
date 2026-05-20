from setuptools import find_packages
from setuptools import setup

version = "4.0.0.dev0"

long_description = (
    open("README.rst").read() + "\n" + "Contributors\n"
    "============\n"
    + "\n"
    + open("CONTRIBUTORS.rst").read()
    + "\n"
    + open("CHANGES.rst").read()
    + "\n"
)


setup(
    name="collective.z3cform.colorpicker",
    version=version,
    description="Colorpicker widget for Plone",
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="plone z3cform colorpicker widget",
    author="Giorgio Borelli",
    author_email="giorgio@giorgioborelli.it",
    url="http://www.giorgioborelli.it",
    license="GPL",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["collective", "collective.z3cform"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "plone.app.z3cform",
        "plone.z3cform",
        "Products.CMFCore",
        "z3c.form",
        "zope.component",
        "zope.interface",
        "zope.schema",
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
