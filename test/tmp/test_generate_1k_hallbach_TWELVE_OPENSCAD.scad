projection(cut = true) union(){
    difference(){
        union(){
            union(){
                difference(){
                    cylinder(h=12.0, d=90.0, center=true);
                    cylinder(h=12.001, d=36.0, center=true);
                };
            }; // create_cylinder_with_cutout_inner_36.0mm_outer90.0mm_thickness12.0mm
            union(){
                difference(){
                    cylinder(h=12.0, d=89.0, center=true);
                    cylinder(h=12.0, d=95.0, center=true);
                }; // mount_contruction_helper_cylinder
                translate(v=[0, -51.5, 0]){
                    difference(){
                        cube(size=[100, 20, 12.0], center=true); // mount_base
                        union(){
                            translate(v=[40.0, 0, 0]){
                                cylinder(h=12.0, d=10);
                            }; // mount_hole_a
                            translate(v=[-40.0, 0, 0]){
                                cylinder(h=12.0, d=10);
                            }; // mount_hole_a
                        };
                    };
                }; // mount_bar_top
            }; // append_mounting_holes_to_base_slice_10_100
        };
        rotate(a=[0.0, 0.0, 179.29289321881345]){
            translate(v=[36.0, 0.0, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -135.70710678118655]){
            translate(v=[31.176914536239792, 17.999999999999996, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -90.70710678118654]){
            translate(v=[18.000000000000004, 31.17691453623979, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -45.707106781186546]){
            translate(v=[2.204364238465236e-15, 36.0, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, -0.7071067811865472]){
            translate(v=[-17.999999999999993, 31.176914536239792, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 44.29289321881345]){
            translate(v=[-31.176914536239792, 17.999999999999996, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 89.29289321881345]){
            translate(v=[-36.0, 4.408728476930472e-15, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 134.29289321881345]){
            translate(v=[-31.17691453623979, -18.000000000000004, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 179.29289321881345]){
            translate(v=[-18.000000000000014, -31.17691453623978, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -135.70710678118655]){
            translate(v=[-6.613092715395707e-15, -36.0, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -90.70710678118654]){
            translate(v=[18.000000000000004, -31.17691453623979, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -45.707106781186546]){
            translate(v=[31.17691453623978, -18.000000000000014, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
    };
};

// 0_create_cylinder_with_cutout_inner_36.0mm_outer90.0mm_thickness12.0mm 
// 1_ops_magnet_ 
// 2_ops_magnet_ 
// 3_ops_magnet_ 
// 4_ops_magnet_ 
// 5_ops_magnet_ 
// 6_ops_magnet_ 
// 7_ops_magnet_ 
// 8_ops_magnet_ 
// 9_ops_magnet_ 
// 10_ops_magnet_ 
// 11_ops_magnet_ 
// 12_ops_magnet_ 
