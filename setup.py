import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="django-edge",
    version="0.0.1",
    author="Okonkwo mandy",
    author_email="okonkwomandy101@gmail.com",
    description=("A package that helps you setup django so that you can focus on the important things."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mandyiee/django_edge.git",
    project_urls={
        "Bug Tracker": "https://github.com/Mandyiee/django_edge.git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["bs4"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "django_edge = edge.cli:main",
        ]
    }
)