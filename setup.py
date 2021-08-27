import os
from setuptools import setup, find_packages

name = u"e2x_nbtools"

extension_files = []
extension_path = os.path.join(name, "nbextensions")

for (dirname, dirnames, filenames) in os.walk(extension_path):
    root = os.path.relpath(dirname, extension_path)
    for filename in filenames:
        if not filename.endswith(".pyc"):
            extension_files.append(os.path.join("nbextensions", root, filename))


setup_args = dict(
    name=name,
    version="0.0.1",
    description="Addons for jupyter notebook",
    author="Tim Metzler",
    author_email="tim.metzler@h-brs.de",
    license="MIT",
    url="https://github.com/DigiKlausur/e2x-nbtools",
    keywords=["Notebooks", "Checkpoints"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(),
    package_data={name: extension_files},
    install_requires=["jupyter", "notebook>=6.1.6"],
)

if __name__ == "__main__":
    print(extension_files)
    setup(**setup_args)
