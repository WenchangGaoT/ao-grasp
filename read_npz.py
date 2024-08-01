import numpy as np
import argparse 

parser = argparse.ArgumentParser() 
parser.add_argument('--npz_path') 
args = parser.parse_args() 


npz_data = np.load(args.npz_path, allow_pickle=True)['data']
print(npz_data)