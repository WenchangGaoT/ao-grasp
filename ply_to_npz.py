import numpy as np
import open3d as o3d
import argparse


def ply_to_npz(ply_path, npz_path):
    pcd = o3d.io.read_point_cloud(ply_path)
    pcd_arr = np.asarray(pcd) 
    np.savez(npz_path, pcd_arr)
    print(pcd_arr)


parser = argparse.ArgumentParser() 
parser.add_argument('--ply_path') 
parser.add_argument('--npz_path')
args = parser.parse_args() 

ply_to_npz(args.ply_path, args.npz_path)