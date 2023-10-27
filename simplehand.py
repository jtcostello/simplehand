import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Hand:
    def __init__(self):
        # Define the initial positions of the points
        self.positions = {
            "wrist": np.array([0, 0, 0]),
            "thumb_base": np.array([0, 0, 0]),
            "thumb_tip": np.array([2, 1, 0]),
            "idx_base": np.array([1.5, 4, 0]),
            "idx_tip": np.array([1.5, 7, 0]),
            "middle_base": np.array([0.5, 4, 0]),
            "middle_tip": np.array([0.5, 7, 0]),
            "ring_base": np.array([-0.5, 4, 0]),
            "ring_tip": np.array([-0.5, 7, 0]),
            "small_base": np.array([-1.5, 4, 0]),
            "small_tip": np.array([-1.5, 7, 0])
        }
        
        # Store initial positions for reference
        self.initial_positions = self.positions.copy()

        # Define the connections between the points
        self.connections = [
            ("wrist", "idx_base"),
            ("wrist", "small_base"),
            ("wrist", "thumb_base"),
            ("idx_base", "middle_base"),
            ("middle_base", "ring_base"),
            ("ring_base", "small_base"),
            ("idx_base", "idx_tip"),
            ("middle_base", "middle_tip"),
            ("ring_base", "ring_tip"),
            ("small_base", "small_tip"),
            ("thumb_base", "thumb_tip")
        ]

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        
    def draw(self, idx_flexion, mrs_flexion, thumb_flexion):

        def rotate_xz(pos, angle):
            length = np.linalg.norm(pos)
            return np.array([length * np.cos(angle), 0, length * np.sin(angle)])

        def rotate_yz(pos, angle):
            length = np.linalg.norm(pos)
            return np.array([0, length * np.cos(angle), length * np.sin(angle)])

        # Thumb rotation in x-z plane
        thumb_angle = thumb_flexion * np.pi / 2
        thumb_pos = self.positions["thumb_tip"] - self.positions["thumb_base"]
        self.positions["thumb_tip"] = self.positions["thumb_base"] + rotate_xz(thumb_pos, thumb_angle)
        
        # Other fingers rotation in y-z plane
        idx_angle = idx_flexion * np.pi
        idx_pos = self.positions["idx_tip"] - self.positions["idx_base"]
        self.positions["idx_tip"] = self.positions["idx_base"] + rotate_yz(idx_pos, idx_angle)

        mrs_angle = mrs_flexion * np.pi
        for finger in ["middle", "ring", "small"]:
            finger_pos = self.positions[f"{finger}_tip"] - self.positions[f"{finger}_base"]
            self.positions[f"{finger}_tip"] = self.positions[f"{finger}_base"] + rotate_yz(finger_pos, mrs_angle)

        # Draw a dark plane as the "floor"
        w, l = 3, 3
        center = np.array([0, 2, -2])
        xx, yy = np.meshgrid([-w+center[0], w+center[0]], [-l+center[1], l+center[1]])
        zz = np.zeros(xx.shape) + center[2]
        self.ax.plot_surface(xx, yy, zz, color='k', alpha=0.3)

        # fill in the hand triangle
        x = [self.positions["wrist"][0], self.positions["idx_base"][0], self.positions["small_base"][0]]
        y = [self.positions["wrist"][1], self.positions["idx_base"][1], self.positions["small_base"][1]]
        z = [self.positions["wrist"][2], self.positions["idx_base"][2], self.positions["small_base"][2]]
        self.ax.plot_trisurf(x, y, z, color='b', alpha=0.3)

        # Draw spheres for each position
        for key, pos in self.positions.items():
            self.ax.scatter(*pos, s=100, c='b', marker='o')
        
        # Draw lines for each connection
        for start, end in self.connections:
            start_pos = self.positions[start]
            end_pos = self.positions[end]
            self.ax.plot([start_pos[0], end_pos[0]], 
                    [start_pos[1], end_pos[1]], 
                    [start_pos[2], end_pos[2]], 'k-')
            
        self.ax.set_xlim([-3, 3])
        self.ax.set_ylim([-1, 6])
        self.ax.set_zlim([-3, 3])
        self.ax.view_init(45, -45)
        self.ax.set_axis_off()

