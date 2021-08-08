# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

p_version = "0.1.0"

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="dkc-api",
    version=p_version,
    author="Alexandr Drachenin",
    author_email="alexdrachenin98@gmail.com",
    packages=find_packages(),
    url="https://github.com/Blackgard/dkc-api",
    download_url="https://github.com/Blackgard/dkc-api/tarball/v{0}".format(
        p_version
    ),
    license="MIT",
    description="Connector for connecting via api to DKC. Allows you to easily retrieve product and news data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "python",
        "dkc",
        "api",
        "connector",
        "loader"
    ],
    install_requires=[
        "loguru==0.5.3",
        "requests==2.26.0",
        "pydantic==1.8.2",
        "pytz==2021.1",
        "python-dotenv==0.19.0"
    ],
    python_requires='>=3.9'
)
