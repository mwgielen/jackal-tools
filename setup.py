from setuptools import setup

setup(name='jackal_tools',
      version='0.0.3',
      description='Tools for jackal.',
      author='Matthijs Gielen',
      author_email='github@mwgielen.com',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3 :: Only'
      ],
      requires_python='>=3',
      url='https://github.com/mwgielen/jackal-tools/',
      packages=['jackal_tools'],
      install_requires=['jackal', 'psutil', 'scapy-python3'],
      entry_points={
          'console_scripts': [
              'jk-sniffer = jackal_tools.sniffer:main',
          ]
      })
