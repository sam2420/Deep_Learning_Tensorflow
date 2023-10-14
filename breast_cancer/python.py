import datetime
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import os
import zipfile
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import itertools
import tensorflow as tf
import pandas as pd

df = pd.read_csv('breast-cancer.csv', on_error='ignore')

print(df.head())
