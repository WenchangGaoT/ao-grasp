import numpy as np
import open3d as o3d
import argparse


def npz_to_ply(npz_path):
    npz_data = np.load(npz_path, allow_pickle=True)['data'].item()['pts']
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(npz_data)
    o3d.io.write_point_cloud('/home/wgao22/ref-codes/ao-grasp/temp.ply', pcd)
    # print(npz_data) 


parser = argparse.ArgumentParser() 
parser.add_argument('--npz_path', type=str)

args = parser.parse_args()
npz_to_ply(args.npz_path)