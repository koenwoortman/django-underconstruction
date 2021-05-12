import setuptools

exec(open('django_underconstruction/version.py').read())

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-underconstruction',
    version=__version__,
    author='Koen Woortman',
    author_email='koensw@outlook.com',
    url='https://github.com/koenwoortman/django-underconstruction',
    description="django-underconstruction shows an under construction page",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=['Django>=2.2'],
    license='MIT',
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
