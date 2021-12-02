
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dewloosh",                     
    version="0.0.1",                        
    author="dewloosh",
    author_email = 'dewloosh@gmail.com',
    url = 'https://github.com/dewloosh/dewloosh',   
    download_url = 'https://github.com/dewloosh/dewloosh/archive/refs/tags/0_0_1.zip',                     
    description="A collection of tools for common developer utility",
    long_description=long_description,   
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),   
    classifiers=[
        'Development Status :: 3 - Alpha',     
        'License :: OSI Approved :: MIT License',   
        'Programming Language :: Python :: 3',
		'Operating System :: OS Independent'
    ],                                      
    python_requires='>=3.6',                
    py_modules=["dewloosh"],             
    package_dir={'':'src'},     
    install_requires=[            
          'setuptools',
          'wheel',
      ],
)

