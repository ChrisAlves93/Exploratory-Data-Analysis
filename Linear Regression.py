import numpy as np
import scipy.stats as sc
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

dataset = pd.read_csv("h/Users/dataset_Facebook.csv")
