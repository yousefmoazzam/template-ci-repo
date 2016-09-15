from setuptools import setup, find_packages

module_name = "module"

setup(
    name=module_name,
    version='',
    description='',
    url='https://github.com/<user/organization>/<repo-name>',
    author='',
    author_email='',
    keywords='',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
    ],
    license='APACHE',
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=[
        'nose>=1.3.0',
        'mock'
    ],
    zip_safe=False,
)
