#!/usr/bin/env python
# coding: utf-8
import pandas as pd
df = pd.read_csv('Cleaned_DATASET.csv')
df.to_excel('Cleaned_DATASET.xlsx',index=False)
