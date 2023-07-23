from setuptools import setup, find_namespace_packages

setup(name='parser_folder_hutnyk',
      version='0.0.1',
      description='parser folder skript',
      author='Leonid Hutnyk',
      author_email='testvvm@example.com',
      license='MIT',
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = parser_folder_hutnyk.clean:run']}
      )