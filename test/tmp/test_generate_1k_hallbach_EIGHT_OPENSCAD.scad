projection(cut = true) union(){
    difference(){
        union(){
            union(){
                difference(){
                    cylinder(h=12.0, d=60.0, center=true);
                    cylinder(h=12.001, d=24.0, center=true);
                };
            }; // create_cylinder_with_cutout_inner_24.0mm_outer60.0mm_thickness12.0mm
            union(){
                difference(){
                    cylinder(h=12.0, d=59.0, center=true);
                    cylinder(h=12.0, d=65.0, center=true);
                }; // mount_contruction_helper_cylinder
                translate(v=[0, -36.5, 0]){
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
            translate(v=[30.0, 0.0, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -90.70710678118654]){
            translate(v=[21.213203435596427, 21.213203435596423, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, -0.7071067811865472]){
            translate(v=[1.83697019872103e-15, 30.0, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 89.29289321881345]){
            translate(v=[-21.213203435596423, 21.213203435596427, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 179.29289321881345]){
            translate(v=[-30.0, 3.67394039744206e-15, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -90.70710678118654]){
            translate(v=[-21.21320343559643, -21.213203435596423, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, -0.7071067811865472]){
            translate(v=[-5.510910596163089e-15, -30.0, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24.0, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 89.29289321881345]){
            translate(v=[21.21320343559642, -21.21320343559643, 0.0]){
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

// 0_create_cylinder_with_cutout_inner_24.0mm_outer60.0mm_thickness12.0mm 
// 1_ops_magnet_ 
// 2_ops_magnet_ 
// 3_ops_magnet_ 
// 4_ops_magnet_ 
// 5_ops_magnet_ 
// 6_ops_magnet_ 
// 7_ops_magnet_ 
// 8_ops_magnet_ 
