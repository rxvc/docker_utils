from setuptools import setup


setup(
    name='docker-utils',
    version='0.0.1',

    author="Rodrigo Vallejo",
    author_email="rxvallejoc@gmail.com",

    description='Common utils for Docker image',

    url="https://github.com/rxvc/docker-utils",

    install_requires=open('requirements.txt').read(),

    packages=['docker'],

    include_package_data=True,

    python_requires='>=2.7',
    setup_requires=['setuptools-git'],

    entry_points={
        "console_scripts": [
            "dconsole = docker.docker_utils.dconsole:main",
        ]
    }
)
