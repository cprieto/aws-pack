from setuptools import setup 

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='aws-lambda-packer',
      version='0.1',
      description='Packs a Python program as an AWS Lambda Function, ready for deployment',
      long_description=readme(),
      packages = ['lpack'],
      url='https://github.com/cprieto/lpack',
      author='Cristian Prieto',
      author_email='me@cprieto.com',
      license='MIT',
      install_requires = ['pyyaml'],
      keywords = [
          'aws',
          'aws lambda',
          'deployment'],
      classifiers =[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
          'License :: OSI Approved :: MIT License'],
      entry_points = {
          'console_scripts': ['aws-pack=lpack.command_line:main']
          })
