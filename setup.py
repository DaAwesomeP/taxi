import pathlib

import setuptools

readme = (pathlib.Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="taxi",
    version="0.1.0a0",
    description="Opinionated Axidraw interface",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Antoine Beyeler",
    author_email="abeyeler@ab-ware.com",
    url="https://github.com/plottertools/taxi",
    license="MIT",
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires=">=3.7,<3.10",
    package_data={"taxi": ["*.kv", "*.json"]},
    install_requires=[
        "kivy>=2.0.0,<3",
        "vpype>=1.7.0,<2",
        "pyaxidraw @ https://cdn.evilmadscientist.com/dl/ad/public/AxiDraw_API.zip",
        "watchgod>=0.7,<1",
        "aiohttp>=3,<4",
    ],
    extras_require={
        "dev": [
            "black>=21,<22",
            "isort>=5,<6",
        ]
    }
)
