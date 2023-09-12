projection(cut = true) union(){
    difference(){
        union(){
            union(){
                difference(){
                    cylinder(h=12.2, d=106.94153162899184, center=true);
                    cylinder(h=12.200999999999999, d=47.05846837100817, center=true);
                };
            }; // create_cylinder_with_cutout_inner_47.05846837100817mm_outer106.94153162899184mm_thickness12.2mm
            union(){
                difference(){
                    cylinder(h=12, d=105.94153162899184, center=true);
                    cylinder(h=12, d=108.94153162899184, center=true);
                }; // mount_contruction_helper_cylinder
                translate(v=[0, -55.47076581449592, 0]){
                    difference(){
                        cube(size=[110, 20, 12], center=true); // mount_base
                        union(){
                            translate(v=[45.0, 0, -12]){
                                cylinder(h=18.2, d=10);
                            }; // mount_hole_a
                            translate(v=[-45.0, 0, -12]){
                                cylinder(h=18.2, d=10);
                            }; // mount_hole_a
                        };
                    };
                }; // mount_bar_top
            }; // append_mounting_holes_to_base_slice_10_110
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[36.0, 0.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[31.176914536239792, 17.999999999999996, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[18.000000000000004, 31.17691453623979, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[2.204364238465236e-15, 36.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[-17.999999999999993, 31.176914536239792, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[-31.176914536239792, 17.999999999999996, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-36.0, 4.408728476930472e-15, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[-31.17691453623979, -18.000000000000004, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[-18.000000000000014, -31.17691453623978, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-6.613092715395707e-15, -36.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[18.000000000000004, -31.17691453623979, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[31.17691453623978, -18.000000000000014, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
    };
};

// 0_create_cylinder_with_cutout_inner_47.05846837100817mm_outer106.94153162899184mm_thickness12.2mm 
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
