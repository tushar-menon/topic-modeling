# -*- coding: utf-8 -*-
"""stochastic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lcFFNqRmbVr3cEgDjRNPaNY8Qv8nWQ4s
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn import decomposition
from scipy import linalg
import matplotlib.pyplot as plt

# %matplotlib inline
np.set_printoptions(suppress=True)

train = fetch_20newsgroups(subset='train',
                           categories=['alt.atheism', 'talk.religion.misc', 'comp.graphics', 'sci.space'], 
                           remove=['headers', 'footers','quotes'])
test = fetch_20newsgroups(subset='test', 
                          categories=['alt.atheism', 'talk.religion.misc', 'comp.graphics', 'sci.space'], 
                            remove=['headers', 'footers','quotes'])
(np.array(train.target_names)[train.target[:3]])

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
vectorizer = CountVectorizer(stop_words='english')
vectors = vectorizer.fit_transform(train.data).todense()

def grads(M, W, H):
    R = W*H-M
    return R@H.T + penalty(W, mu)*lam, W.T@R + penalty(H, mu)*lam

def penalty(M, mu):
    return np.where(M>=mu,0, np.min(M - mu, 0))

def upd(M, W, H, lr):
    dW,dH = grads(M,W,H)
    W -= lr*dW; H -= lr*dH

def report(M,W,H): 
    print(np.linalg.norm(M-W@H), W.min(), H.min(), (W<0).sum(), (H<0).sum())

W = np.abs(np.random.normal(scale=0.01, size=(m,d)))
H = np.abs(np.random.normal(scale=0.01, size=(d,n)))
# Track document frequency
