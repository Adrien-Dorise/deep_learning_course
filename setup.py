from setuptools import setup, find_packages

setup(name="deep_learning_course",
      version="1.0.0",
      description="Deep learning course",
      author="Adrien Dorise",
      author_email="adrien.dorise@hotmail.com",
      url="https://github.com/Adrien-Dorise/deep_learning_course",
      packages=[],
      install_requires=[
            "numpy >= 1.24.2",
            "torch >= 1.13.1",
            "torchvision >= 0.14.1",
            "torchinfo >= 1.8.0",
            "torchview >= 0.2.6",
            "torchviz>=0.0.2",
            "matplotlib >= 3.8.1",
            "scikit-learn >= 1.3.2",
            "pandas >= 2.1.2",
            "opencv-python >= 4.7.0.72",
            "graphviz >= 0.20.1",
            "imgaug >= 0.4.0",
            "tqdm >= 4.66.1",
            "requests >= 2.32.3",
            "tokenizers >= 0.21.0",
            "transformers >= 4.49.0",
            "datasets >= 3.3.2",

      ], 
      python_requires=">=3.10.1",
     )