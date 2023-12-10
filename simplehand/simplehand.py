import numpy as np
import matplotlib.pyplot as plt
import copy
from simplehand.hand_structure import hand_structure

class SuperSimpleHand:
    """V1 of the hand - a single line to represent each finger"""
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
        
    def draw(self, idx_flexion=0, mrs_flexion=0, thumb_flexion=0):

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


class SimpleHand:
    """V2 of the hand - multiple joints per finger"""
    def __init__(self, fig=None, ax=None):
        self.base_structure = hand_structure
        self.hand_structure = copy.deepcopy(self.base_structure)
        if fig is None or ax is None:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(111, projection='3d')
        else:
            self.fig = fig
            self.ax = ax

    def _rotate_point(self, point_pos, parent_pos, axis, degrees):
        # Convert degrees to radians
        theta = -1 * np.radians(degrees)

        # Make the rotation axis a unit vector
        k = np.array(axis) / np.linalg.norm(axis)

        # Translate point to origin (relative to parent_pos)
        v = point_pos - parent_pos

        # Apply Rodrigues' rotation formula
        v_rot = v * np.cos(theta) + np.cross(k, v) * np.sin(theta) + k * np.dot(k, v) * (1 - np.cos(theta))

        # Translate point back to its relative position
        return v_rot + parent_pos

    def _update_position(self, node, parent_node, tendon_flexion_values):
        """Recursively update the position of each node in the hand model.
        Points rotate about the parent node's position.

        Note: if we don't keep track of the original position of each node, the hand will get distorted
        since the calculated distance between nodes will change as the hand flexes. To solve this, we rotate
        each node about the parent's original position, then adjust for the change in parent's position.
        """
        current_pos = np.array(node["pos"])
        node["orig_pos"] = copy.deepcopy(node["pos"])
        if parent_node is not None:
            tendon_name = parent_node["tendon"]
            if tendon_name:
                flexion_value = tendon_flexion_values[tendon_name]
                rotation_angle = flexion_value * parent_node["max_angle"] + parent_node["angle"]
                new_pos = self._rotate_point(current_pos, np.array(parent_node["orig_pos"]), parent_node["rot_axis"],
                                       rotation_angle)
                new_pos = new_pos + np.array(parent_node["pos"]) - np.array(parent_node["orig_pos"])
                node["pos"] = list(new_pos)
                node["angle"] = rotation_angle

        for child_name, child_node in node["children"].items():
            self._update_position(child_node, node, tendon_flexion_values)

    def set_flex(self, th=0, idx=0, mid=0, ri=0, pi=0):
        """Set the positions of each node in the hand model based on the tendon flexion values.
        Flexions should be 0 to 1"""
        self.hand_structure = copy.deepcopy(self.base_structure)
        wr = 0          # TODO: wrist rotation doesn't work yet
        flex_vals_dict = {
            "wrist": wr,
            "thumb": th,
            "index": idx,
            "middle": mid,
            "ring": ri,
            "pinky": pi
        }
        # self.hand_structure['arm']['orig_pos'] = self.hand_structure['arm']['pos']
        self._update_position(self.hand_structure['arm'], None, flex_vals_dict)

    def draw(self, draw_floor=False):
        """Recursively plot the hand model using matplotlib."""
        def plot_node_and_edges(ax, node, parent_pos):
            current_pos = np.array(node["pos"])
            ax.scatter(*current_pos, color='blue', s=50)
            if parent_pos is not None:
                ax.plot3D(*zip(parent_pos, current_pos), color='black')
            for child_node in node["children"].values():
                plot_node_and_edges(ax, child_node, current_pos)

        # Draw a dark plane as the "floor"
        if draw_floor:
            w, l = 2, 2
            center = np.array([0, 0, -1])
            xx, yy = np.meshgrid([-w+center[0], w+center[0]], [-l+center[1], l+center[1]])
            zz = np.zeros(xx.shape) + center[2]
            self.ax.plot_surface(xx, yy, zz, color='k', alpha=0.3)

        # Draw hand
        node = self.hand_structure["arm"]
        plot_node_and_edges(self.ax, node, None)

        # set view
        self.ax.set_xlim3d(-1.5, 1.5)
        self.ax.set_ylim3d(-1.5, 1.5)
        self.ax.set_zlim3d(-1.5, 1.5)
        self.ax.view_init(30, -130)
        self.ax.set_axis_off()


if __name__ == "__main__":
    hand = SimpleHand()
    hand.draw()
    plt.show()

