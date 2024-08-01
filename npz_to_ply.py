import numpy as np
import open3d as o3d
import argparse


def npz_to_ply(npz_path, ply_path):
    npz_data = np.load(npz_path, allow_pickle=True)
    print(npz_data)
    npz_data = npz_data['data'].item()['pts']
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(npz_data)
    o3d.io.write_point_cloud(ply_path, pcd)
    # print(npz_data) 


parser = argparse.ArgumentParser() 
parser.add_argument('--npz_path', type=str) 
parser.add_argument('--ply_path', type=str, default='temp.ply')

args = parser.parse_args()
npz_to_ply(args.npz_path, args.ply_path)