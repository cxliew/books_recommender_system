import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_boxplot(dataframe, x_data, y_data, hue_data, title, x_label, y_label, orient):
    """To plot a boxplot with input of details.
    Orient can take a form of 'h' or 'v'.
    hue_data can take a form of None. The output is a boxplot"""
    plt.figure(figsize = (8,5))
    sns.boxplot(x = x_data, y = y_data, hue = hue_data, data = dataframe, orient = orient)
    plt.xlabel(x_label, fontsize = 16)
    plt.ylabel(y_label, fontsize = 16)
    plt.title((title +"\n"), weight = 'bold', fontsize = 14)
    plt.savefig(f'../imgs/{title}.png');
    return plt.show()

def plot_barplot(dataframe, x_data, y_data, hue_data, title, x_label, y_label, orient):
    """To plot a barplot with input of details.
    Orient can take a form of 'h' or 'v'.
    hue_data can take a form of None. The output is a barplot"""
    plt.figure(figsize = (8,5))
    sns.barplot(x = x_data, y = y_data, hue = hue_data, data = dataframe, orient = orient)
    plt.xlabel(x_label, fontsize = 16)
    plt.ylabel(y_label, fontsize = 16)
    plt.title((title +"\n"), weight = 'bold', fontsize = 14)
    plt.savefig(f'../imgs/{title}.png');
    return plt.show()

def numeric_plot_histplot(dataframe, x_data, num_bins, bin_width, bin_range, title, x_label, y_label):
    """To plot a histplot with input of details.
    binrange can take a form of (min, max). The output is a histplot"""
    plt.figure(figsize = (8,5))
    sns.histplot(x = x_data, data = dataframe, bins = num_bins, binwidth = bin_width, binrange = bin_range)
    plt.xlabel(x_label, fontsize = 16)
    plt.ylabel(y_label, fontsize = 16)
    plt.title((title +"\n"), weight = 'bold', fontsize = 14)
    plt.savefig(f'../imgs/{title}.png');
    return plt.show()

def dataframe_plot(dataframe, plot_type, title, x_label, y_label):
    """To plot using the dataframe with specifying the kind of plot.
    Figsize is a tuple size eg (8,5). Kind can take a form of 'line', 'bar', 'barh', 'hist', 'box', 'kde', 'density', 'area', 'pie', 'scatter', 'hexbin'.The output is a specified plot of the dataframe."""
    plt.figure(figsize = (8,5))
    dataframe.plot(kind = plot_type)
    plt.xlabel(x_label, fontsize = 16)
    plt.ylabel(y_label, fontsize = 16)
    plt.title((title +"\n"), weight = 'bold', fontsize = 14)
    plt.savefig(f'../imgs/{title}.png');
    return plt.show()

def plot_countplot(dataframe, x_data, hue_data, title, x_label, y_label):
    """To plot a countplot with input of details.
    hue_data can take a form of None. The output is a countplot"""
    plt.figure(figsize = (8,5))
    sns.countplot(x = x_data, hue = hue_data, data = dataframe)
    plt.xlabel(x_label, fontsize = 16)
    plt.ylabel(y_label, fontsize = 16)
    plt.title((title +"\n"), weight = 'bold', fontsize = 14)
    plt.savefig(f'../imgs/{title}.png');
    return plt.show() 