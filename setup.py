from setuptools import setup

setup(
        name='napalm_huawei_usg',
        version='0.0.3',
        description='NAPALM Community Driver for Huawei USG Firewalls.',
        url='https://github.com/ObSec/napalm-huawei-usg',
        author='Mario Oberli',
        author_email='mario.oberli@obsec.ch',
        license='Apache License 2.0',
        packages=['napalm_huawei_usg','napalm_huawei_usg.utils'],
        install_requires=['napalm>=3.0.0',
            ],

        classifiers=[
            'Development Status :: 1 - Planning',
            'Topic :: Utilities',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Operating System :: POSIX :: Linux',
            'Operating System :: MacOS',
        ],
)
