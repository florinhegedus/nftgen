from PIL import Image 
from IPython.display import display 
import random
import json
import os
import argparse

def args():
    parser = argparse.ArgumentParser(description='NFT Generator implementation by @florin')
    # data path argument
    parser.add_argument('--source', help='image data path', required=True, type=str)
    parser.add_argument('--output_folder', help='folder for saving the nfts', required=True, type=str)
    args = parser.parse_args()

    return args

args = args()
print(args)
