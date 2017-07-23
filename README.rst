Pack your application ready for AWS Lambda deployment
================================

When we started using AWS Lambdas written in Python, one of the first issues was packing the Python application ready for deployment in AWS. The AWS guidelines details many manual steps to prepare your package and then deploy with the `aws` command line, but well, the packaging needs to be done by you alone.

This simple command line helps with the packaging step, taking into care some steps and making it easier for deployment.

Usage
----

Let's say you have a two file Python application, `app.py` and `stuff.py`, just pack the application using:

::
    aws-pack --files app.py stuff.py

You can specify the name of the output zip file as well, default name for the zipfile is the name of the directory:

::
    aws-pack --files app.py stuff.py --output myapp.zip

If you have a requirement file for PIP (`requirements.txt`) this will install the requirements and include them in the zip file, as recommended by Amazon documentation. Be careful with requirements, some libraries should not be included in the zip file, for example, the `boto3` libraries for access the AWS API, these are automatically included in the environment by the AWS Lambda Engine. To avoid this issue, I recommend creating a separate requirements file with the requirements needed for
running the lambda, for example, `requirements.lambda.txt` without the `boto3` and tests libraries. You can specify which requirement file to use using the following flag:

::
    aws-pack --files app.py stuff.py --output myapp.zip --requirements requirements.lambda.txt


Installation
------------

The command line application is available in PyPI, just install using ``pip``:

::

    pip install aws-lpacker


And start using it.
