union(){
    difference(){
        union(){
            union(){
                difference(){
                    cylinder(h=12.2, d=94.94153162899184, center=true);
                    cylinder(h=12.200999999999999, d=35.05846837100817, center=true);
                };
            }; // create_cylinder_with_cutout_inner_35.05846837100817mm_outer94.94153162899184mm_thickness12.2mm
            union(){
                difference(){
                    cylinder(h=12, d=93.94153162899184, center=true);
                    cylinder(h=12, d=96.94153162899184, center=true);
                }; // mount_contruction_helper_cylinder
                translate(v=[0, -49.47076581449592, 0]){
                    difference(){
                        cube(size=[90, 20, 12], center=true); // mount_base
                        union(){
                            translate(v=[35.0, 0, -12]){
                                cylinder(h=18.2, d=10);
                            }; // mount_hole_a
                            translate(v=[-35.0, 0, -12]){
                                cylinder(h=18.2, d=10);
                            }; // mount_hole_a
                        };
                    };
                }; // mount_bar_top
            }; // append_mounting_holes_to_base_slice_10_90
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[112.5, 0.0, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 149.29289321881345]){
                translate(v=[108.66665545752018, 29.117142574033583, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[97.42785792574935, 56.24999999999999, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[79.5495128834866, 79.54951288348659, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[56.250000000000014, 97.42785792574934, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 29.292893218813454]){
                translate(v=[29.117142574033583, 108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[6.8886382452038615e-15, 112.5, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -30.707106781186567]){
                translate(v=[-29.117142574033597, 108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[-56.24999999999997, 97.42785792574935, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-79.54951288348659, 79.5495128834866, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[-97.42785792574935, 56.24999999999999, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -150.70710678118658]){
                translate(v=[-108.66665545752018, 29.117142574033615, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-112.5, 1.3777276490407723e-14, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 149.29289321881345]){
                translate(v=[-108.66665545752018, -29.11714257403359, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[-97.42785792574934, -56.250000000000014, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-79.54951288348661, -79.54951288348659, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[-56.25000000000005, -97.42785792574932, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 29.292893218813454]){
                translate(v=[-29.117142574033572, -108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-2.0665914735611585e-14, -112.5, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -30.707106781186567]){
                translate(v=[29.117142574033533, -108.66665545752019, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[56.250000000000014, -97.42785792574934, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[79.54951288348657, -79.54951288348661, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[97.42785792574932, -56.25000000000005, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -150.70710678118658]){
                translate(v=[108.66665545752018, -29.117142574033576, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -6.0]){
                            cylinder(h=24, d=7.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 7.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t3:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t3:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[30.0, 0.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -6.0]){
                            cylinder(h=24, d=4.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 4.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t4:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t4:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[21.213203435596427, 21.213203435596423, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -6.0]){
                            cylinder(h=24, d=4.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 4.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t4:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t4:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[1.83697019872103e-15, 30.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -6.0]){
                            cylinder(h=24, d=4.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 4.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t4:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t4:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-21.213203435596423, 21.213203435596427, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -6.0]){
                            cylinder(h=24, d=4.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 4.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t4:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t4:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-30.0, 3.67394039744206e-15, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -6.0]){
                            cylinder(h=24, d=4.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 4.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t4:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t4:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-21.21320343559643, -21.213203435596423, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -6.0]){
                            cylinder(h=24, d=4.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 4.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t4:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t4:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-5.510910596163089e-15, -30.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -6.0]){
                            cylinder(h=24, d=4.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 4.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t4:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t4:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[21.21320343559642, -21.21320343559643, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -6.0]){
                            cylinder(h=24, d=4.6);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 4.933333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t4:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t4:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[54.0, 0.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[49.88949475560948, 20.66490534771485, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[38.18376618407357, 38.18376618407356, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[20.66490534771485, 49.88949475560948, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[3.3065463576978537e-15, 54.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[-20.664905347714846, 49.88949475560948, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-38.18376618407356, 38.18376618407357, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[-49.88949475560948, 20.664905347714853, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-54.0, 6.6130927153957075e-15, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[-49.88949475560949, -20.664905347714843, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-38.183766184073576, -38.18376618407356, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[-20.664905347714832, -49.88949475560949, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-9.91963907309356e-15, -54.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[20.66490534771486, -49.889494755609476, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[38.183766184073555, -38.183766184073576, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[49.88949475560949, -20.664905347714836, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[36.0, 0.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[31.176914536239792, 17.999999999999996, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[18.000000000000004, 31.17691453623979, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[2.204364238465236e-15, 36.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[-17.999999999999993, 31.176914536239792, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[-31.176914536239792, 17.999999999999996, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-36.0, 4.408728476930472e-15, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[-31.17691453623979, -18.000000000000004, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[-18.000000000000014, -31.17691453623978, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-6.613092715395707e-15, -36.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[18.000000000000004, -31.17691453623979, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[31.17691453623978, -18.000000000000014, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[126.0, 0.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 156.79289321881345]){
                translate(v=[123.57894533080703, 24.58138057403216, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[116.40882109642213, 48.21811247800131, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 111.79289321881346]){
                translate(v=[104.7651711501207, 70.00184936046988, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[89.095454429505, 89.09545442950498, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 66.79289321881346]){
                translate(v=[70.00184936046989, 104.7651711501207, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[48.218112478001316, 116.40882109642213, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 21.792893218813454]){
                translate(v=[24.58138057403217, 123.57894533080703, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[7.715274834628325e-15, 126.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -23.207106781186575]){
                translate(v=[-24.581380574032153, 123.57894533080703, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[-48.2181124780013, 116.40882109642213, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -68.20710678118657]){
                translate(v=[-70.00184936046989, 104.76517115012068, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-89.09545442950498, 89.095454429505, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -113.20710678118657]){
                translate(v=[-104.76517115012071, 70.00184936046988, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[-116.40882109642213, 48.21811247800132, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -158.20710678118658]){
                translate(v=[-123.57894533080703, 24.58138057403215, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-126.0, 1.543054966925665e-14, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 156.79289321881345]){
                translate(v=[-123.57894533080703, -24.581380574032174, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[-116.40882109642214, -48.218112478001295, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 111.79289321881346]){
                translate(v=[-104.7651711501207, -70.00184936046989, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-89.09545442950501, -89.09545442950498, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 66.79289321881346]){
                translate(v=[-70.00184936046988, -104.7651711501207, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[-48.21811247800128, -116.40882109642214, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 21.792893218813454]){
                translate(v=[-24.581380574032213, -123.57894533080702, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-2.3145824503884975e-14, -126.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -23.207106781186575]){
                translate(v=[24.581380574032167, -123.57894533080703, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[48.21811247800134, -116.40882109642212, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -68.20710678118657]){
                translate(v=[70.00184936046983, -104.76517115012072, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[89.09545442950497, -89.09545442950501, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -113.20710678118657]){
                translate(v=[104.7651711501207, -70.00184936046988, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[116.40882109642214, -48.21811247800129, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -158.20710678118658]){
                translate(v=[123.57894533080702, -24.58138057403222, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[30.0, 0.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[21.213203435596427, 21.213203435596423, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[1.83697019872103e-15, 30.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-21.213203435596423, 21.213203435596427, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-30.0, 3.67394039744206e-15, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-21.21320343559643, -21.213203435596423, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-5.510910596163089e-15, -30.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[21.21320343559642, -21.21320343559643, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                        linear_extrude(height=12){
                            rotate(a=[0, 0, 0]){
                                translate(v=[9.0, 6.433333333333333, -12]){
                                    mirror([1, 0, 0]){
                                        text(text="t2:i0", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i0
        };
    };
};
// 0_create_cylinder_with_cutout_inner_41.29385127825613mm_outer266.1769145362398mm_thickness15.2mm 
// 1_None 
// 2_None 
// 3_None 
// 4_None 
// 5_None 
// 6_None 
// 7_None 
// 8_None 
// 9_None 
// 10_None 
// 11_None 
// 12_None 
// 13_None 
// 14_None 
// 15_None 
// 16_None 
// 17_None 
// 18_None 
// 19_None 
// 20_None 
// 21_None 
// 22_None 
// 23_None 
// 24_None 
// 25_None 
// 26_None 
// 27_None 
// 28_None 
// 29_None 
// 30_None 
// 31_None 
// 32_None 
// 33_None 
// 34_None 
// 35_None 
// 36_None 
// 37_None 
// 38_None 
// 39_None 
// 40_None 
// 41_None 
// 42_None 
// 43_None 
// 44_None 
// 45_None 
// 46_None 
// 47_None 
// 48_None 
// 49_None 
// 50_None 
// 51_None 
// 52_None 
// 53_None 
// 54_None 
// 55_None 
// 56_None 
// 57_None 
// 58_None 
// 59_None 
// 60_None 
// 61_None 
// 62_None 
// 63_None 
// 64_None 
// 65_None 
// 66_None 
// 67_None 
// 68_None 
// 69_None 
// 70_None 
// 71_None 
// 72_None 
// 73_None 
// 74_None 
// 75_None 
// 76_None 
// 77_None 
// 78_None 
// 79_None 
// 80_None 
// 81_None 
// 82_None 
// 83_None 
// 84_None 
// 85_None 
// 86_None 
// 87_None 
// 88_None 
// 89_None 
// 90_None 
// 91_None 
// 92_None 
// 93_None 
// 94_None 
// 95_None 
// 96_None 
// 97_None 
// 98_None 
// 99_None 
// 100_None 
// 101_None 
// 102_None 
// 103_None 
// 104_None 
// 105_None 
// 106_None 
// 107_None 
// 108_None 
// 109_None 
// 110_None 
// 111_None 
// 112_None 
// 113_None 
// 114_None 
// 115_None 
// 116_None 
// 117_None 
// 118_None 
// 119_None 
// 120_None 
// 121_None 
// 122_None 
// 123_None 
// 124_None 
// 125_None 
// 126_None 
// 127_None 
// 128_None 
// 129_None 
// 130_None 
// 131_None 
// 132_None 
// 133_None 
// 134_None 
// 135_None 
// 136_None 
// 137_None 
// 138_None 
// 139_None 
// 140_None 
// 141_None 
// 142_None 
// 143_None 
// 144_None 
// 145_create_cylinder_with_cutout_inner_47.05846837100817mm_outer106.94153162899184mm_thickness12.2mm 
// 146_None 
// 147_None 
// 148_None 
// 149_None 
// 150_None 
// 151_None 
// 152_None 
// 153_None 
// 154_None 
// 155_None 
// 156_None 
// 157_None 
// 158_None 
// 159_None 
// 160_None 
// 161_None 
// 162_None 
// 163_None 
// 164_None 
// 165_None 
// 166_None 
// 167_None 
// 168_None 
// 169_None 
// 170_None 
// 171_None 
// 172_None 
// 173_None 
// 174_None 
// 175_None 
// 176_None 
// 177_None 
// 178_None 
// 179_None 
// 180_None 
// 181_None 
// 182_None 
// 183_None 
// 184_None 
// 185_None 
// 186_None 
// 187_None 
// 188_None 
// 189_None 
// 190_None 
// 191_None 
// 192_None 
// 193_None 
// 194_None 
// 195_None 
// 196_None 
// 197_None 
// 198_None 
// 199_None 
// 200_None 
// 201_None 
// 202_None 
// 203_None 
// 204_None 
// 205_None 
// 206_create_cylinder_with_cutout_inner_227.05846837100816mm_outer286.9415316289918mm_thickness12.2mm 
// 207_None 
// 208_None 
// 209_None 
// 210_None 
// 211_None 
// 212_None 
// 213_None 
// 214_None 
// 215_None 
// 216_None 
// 217_None 
// 218_None 
// 219_None 
// 220_None 
// 221_None 
// 222_None 
// 223_None 
// 224_None 
// 225_None 
// 226_None 
// 227_None 
// 228_None 
// 229_None 
// 230_None 
// 231_None 
// 232_None 
// 233_None 
// 234_None 
// 235_None 
// 236_None 
// 237_None 
// 238_None 
// 239_None 
// 240_None 
// 241_None 
// 242_None 
// 243_None 
// 244_None 
// 245_None 
// 246_None 
// 247_None 
// 248_None 
// 249_None 
// 250_None 
// 251_None 
// 252_None 
// 253_None 
// 254_None 
// 255_None 
// 256_None 
// 257_None 
// 258_None 
// 259_None 
// 260_None 
// 261_None 
// 262_None 
// 263_None 
// 264_None 
// 265_None 
// 266_None 
// 267_None 
// 268_None 
// 269_None 
// 270_None 
// 271_None 
// 272_None 
// 273_None 
// 274_None 
// 275_None 
// 276_None 
// 277_None 
// 278_None 
// 279_None 
// 280_None 
// 281_None 
// 282_None 
// 283_None 
// 284_None 
// 285_None 
// 286_None 
// 287_None 
// 288_None 
// 289_None 
// 290_None 
// 291_None 
// 292_None 
// 293_None 
// 294_None 
// 295_None 
// 296_None 
// 297_None 
// 298_None 
// 299_create_cylinder_with_cutout_inner_35.05846837100817mm_outer94.94153162899184mm_thickness12.2mm 
// 300_None 
// 301_None 
// 302_None 
// 303_None 
// 304_None 
// 305_None 
// 306_None 
// 307_None 
// 308_None 
// 309_None 
// 310_None 
// 311_None 
// 312_None 
// 313_None 
// 314_None 
// 315_None 
// 316_None 
// 317_None 
// 318_None 
// 319_None 
// 320_None 
// 321_None 
// 322_None 
// 323_None 
// 324_None 
// 325_None 
// 326_None 
// 327_None 
// 328_None 
// 329_None 
// 330_None 
// 331_None 
// 332_None 
// 333_None 
// 334_None 
// 335_None 
// 336_None 
// 337_None 
// 338_None 
// 339_None 
// 340_None 
// 341_None 
// 342_None 
// 343_None 
// 344_None 
// 345_None 
// 346_None 
// 347_None 
// 348_None 
// 349_None 
// 350_None 
// 351_None 
// 352_None 
// 353_None 
// 354_None 
// 355_None 
// 356_None 
// 357_None 
// 358_None 
// 359_None 
// 360_None 
// 361_None 
// 362_None 
// 363_None 
// 364_None 
// 365_None 
// 366_None 
// 367_None 
// 368_None 
// 369_None 
// 370_None 
// 371_None 
// 372_None 
// 373_None 
// 374_None 
// 375_None 
// 376_None 
// 377_None 
// 378_None 
// 379_None 
// 380_None 
// 381_None 
// 382_None 
// 383_None 
// 384_None 
// 385_None 
// 386_None 
// 387_None 
// 388_None 
// 389_None 
// 390_None 
// 391_None 
// 392_None 
// 393_None 
// 394_None 
// 395_None 
// 396_None 
// 397_None 
// 398_None 
// 399_None 
