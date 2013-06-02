from setuptools import setup, find_packages

version = '1.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')


setup(
    name='collective.z3cform.colorpicker',
    version=version,
    description="Colorpicker widget for Plone",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='plone z3cform colorpicker widget',
    author='Giorgio Borelli',
    author_email='giorgio@giorgioborelli.it',
    url='http://www.giorgioborelli.it',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['collective', 'collective.z3cform'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CMFCore',
        'plone.app.z3cform',
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
