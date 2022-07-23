import setuptools  # type: ignore

__author__: str = "AriArcher"
__author_email__: str = "ari.web.xyz@gmail.com"

MODULE_NAME: str = setuptools.find_packages()[0]

with open("README.md", "r") as desc:
    long_description: str = desc.read()

setuptools.setup(
    name=MODULE_NAME.replace("_", "-"),
    version="0.0.6",
    author=__author__,
    author_email=__author_email__,
    description="Guacamole protocol key mappings for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://ari-web.xyz/gh/{MODULE_NAME}",
    packages=[MODULE_NAME],
    package_dir={MODULE_NAME: MODULE_NAME},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    package_data={
        MODULE_NAME: [
            "py.typed",
            f"{MODULE_NAME}/__init__.pyi",
        ]
    },
    include_package_data=True,
)
