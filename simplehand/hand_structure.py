hand_structure = {
    "arm": {
        "pos": [-1, 0, 0],
        "tendon": None,
        "rot_axis": None,
        "max_angle": 0,
        "angle": 0,

        "children": {
            "wrist": {
                "pos": [0, 0, 0],
                "tendon": "wrist",
                "rot_axis": [-1, 0, 0],
                "max_angle": 90,
                "angle": 0,

                "children": {
                    "thumb_base": {
                        "pos": [0, -0.25, 0],
                        "tendon": "thumb",
                        "rot_axis": [1, 0, 0],
                        "max_angle": 45,
                        "angle": 0,

                        "children": {
                            "thumb_mid": {
                                "pos": [0, -0.75, 0],
                                "tendon": "thumb",
                                "rot_axis": [1, 0, 0],
                                "max_angle": 90,
                                "angle": 0,

                                "children": {
                                    "thumb_tip": {
                                        "pos": [0, -1, 0],
                                        "tendon": "thumb",
                                        "rot_axis": None,
                                        "max_angle": 0,
                                        "angle": 0,
                                        "children": {}
                                    }
                                }
                            }
                        }
                    },
                    "index_base": {
                        "pos": [1, -0.75, 0],
                        "tendon": "index",
                        "rot_axis": [0, 1, 0],
                        "max_angle": 90,
                        "angle": 0,

                        "children": {
                            "index_mid1": {
                                "pos": [1.3, -0.75, 0],
                                "tendon": "index",
                                "rot_axis": [0, 1, 0],
                                "max_angle": 110,
                                "angle": 0,

                                "children": {
                                    "index_mid2": {
                                        "pos": [1.8, -0.75, 0],
                                        "tendon": "index",
                                        "rot_axis": [0, 1, 0],
                                        "max_angle": 45,
                                        "angle": 0,

                                        "children": {
                                            "index_tip": {
                                                "pos": [2.3, -0.75, 0],
                                                "tendon": "index",
                                                "rot_axis": None,
                                                "max_angle": 0,
                                                "angle": 0,
                                                "children": {}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "middle_base": {
                        "pos": [1, -0.25, 0],
                        "tendon": "middle",
                        "rot_axis": [0, 1, 0],
                        "max_angle": 90,
                        "angle": 0,

                        "children": {
                            "middle_mid1": {
                                "pos": [1.5, -0.25, 0],
                                "tendon": "middle",
                                "rot_axis": [0, 1, 0],
                                "max_angle": 110,
                                "angle": 0,

                                "children": {
                                    "middle_mid2": {
                                        "pos": [2, -0.25, 0],
                                        "tendon": "middle",
                                        "rot_axis": [0, 1, 0],
                                        "max_angle": 45,
                                        "angle": 0,

                                        "children": {
                                            "middle_tip": {
                                                "pos": [2.5, -0.25, 0],
                                                "tendon": "middle",
                                                "rot_axis": None,
                                                "max_angle": 0,
                                                "angle": 0,
                                                "children": {}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "ring_base": {
                        "pos": [1, 0.25, 0],
                        "tendon": "ring",
                        "rot_axis": [0, 1, 0],
                        "max_angle": 90,
                        "angle": 0,

                        "children": {
                            "ring_mid1": {
                                "pos": [1.3, 0.25, 0],
                                "tendon": "ring",
                                "rot_axis": [0, 1, 0],
                                "max_angle": 110,
                                "angle": 0,

                                "children": {
                                    "ring_mid2": {
                                        "pos": [1.8, 0.25, 0],
                                        "tendon": "ring",
                                        "rot_axis": [0, 1, 0],
                                        "max_angle": 45,
                                        "angle": 0,

                                        "children": {
                                            "ring_tip": {
                                                "pos": [2.3, 0.25, 0],
                                                "tendon": "ring",
                                                "rot_axis": None,
                                                "max_angle": 0,
                                                "angle": 0,
                                                "children": {}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "pinky_base": {
                        "pos": [0.8, 0.75, 0],
                        "tendon": "pinky",
                        "rot_axis": [0, 1, 0],
                        "max_angle": 90,
                        "angle": 0,

                        "children": {
                            "pinky_mid1": {
                                "pos": [1.2, 0.75, 0],
                                "tendon": "pinky",
                                "rot_axis": [0, 1, 0],
                                "max_angle": 110,
                                "angle": 0,

                                "children": {
                                    "pinky_mid2": {
                                        "pos": [1.6, 0.75, 0],
                                        "tendon": "pinky",
                                        "rot_axis": [0, 1, 0],
                                        "max_angle": 45,
                                        "angle": 0,

                                        "children": {
                                            "pinky_tip": {
                                                "pos": [2.0, 0.75, 0],
                                                "tendon": "pinky",
                                                "rot_axis": None,
                                                "max_angle": 0,
                                                "angle": 0,
                                                "children": {}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
