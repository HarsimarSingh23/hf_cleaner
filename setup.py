from setuptools import setup, find_packages

setup(
    name="hf_cleaner",
    version="0.1.0",
    author="Your Name",
    author_email="sainiharsimar@gmail.com",
    description="Streamlit UI utility to clean hugging face models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypackage",  # Your GitHub repo
    packages=find_packages(),         # Automatically discover packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)