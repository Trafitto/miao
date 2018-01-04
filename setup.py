from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()
		
setup(name='miao',
      version='0.1',
      description='Print a cat',
	  long_description=readme(),
      url='https://github.com/Trafitto/miao',
      author='trafitto',
      author_email='develop@trafitto.com',
      license='MIT',
      packages=['miao'],
      zip_safe=False)