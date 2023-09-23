#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='dazzle-vault',
    # version=VERSION,
    description='SaaS and HR-ops for modern teams',
    # long_description=open('README.rst').read(),
    author='Wilson Gichuhi',
    author_email='winchygichu@gmail.com',
    maintainer='Qodestackr | Wilson Gichuhi',
    maintainer_email='winchygichu@gmail.com',
    url='https://github.com/Qodestackr',
    packages=find_packages(),
    include_package_data=True,
    install_requires=(
        # 'django>=2.2', 'django-countries', 'django-iban', 'django-model-utils', 'django-money',
        # 'django-internationalflavor'
    ),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.11.5',
        'Operating System :: OS Independent',
        'Environment :: Web/Server Environment',
        'Intended Audience :: Developers, HR management, End Users',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 1 - Beta'
    ],
    license='MIT License',
    keywords="dazzlehr django django rest saas cloud-deployment",
)
