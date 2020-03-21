from setuptools import setup

setup(name='rac_schemas',
      version='0.1',
      description='RAC JSON Schemas and validators',
      url='http://github.com/RockefellerArchiveCenter/rac_schemas',
      author='Rockefeller Archive Center',
      author_email='archive@rockarch.org',
      install_requires=['jsonschema'],
      license='MIT',
      packages=['rac_schemas'],
      test_suite='nose.collector',
      tests_require=['nose', 'jsonschema'],
      zip_safe=False)
