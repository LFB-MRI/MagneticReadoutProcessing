union(){
    difference(){
        union(){
            union(){
                difference(){
                    cylinder(h=12, d=137.51150572225254, center=true);
                    cylinder(h=12.001, d=63.96152422706632, center=true);
                };
            }; // create_cylinder_with_cutout_inner_63.96152422706632mm_outer137.51150572225254mm_thickness12mm
            union(){
                difference(){
                    cylinder(h=12, d=136.51150572225254, center=true);
                    cylinder(h=12, d=139.51150572225254, center=true);
                }; // mount_contruction_helper_cylinder
                translate(v=[0, -70.75575286112627, 0]){
                    difference(){
                        cube(size=[140, 20, 12], center=true); // mount_base
                        union(){
                            #translate(v=[60.0, 0, -12]){
                                cylinder(h=19.0, d=10);
                            }; // mount_hole_a
                            translate(v=[-60.0, 0, -12]){
                                cylinder(h=19.0, d=10);
                            }; // mount_hole_a
                        };
                    };
                }; // mount_bar_top
            }; // append_mounting_holes_to_base_slice_10_140
        };
        rotate(a=[0.0, 0.0, 179.29289321881345]){
            translate(v=[43.17691453623979, 0.0, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 89.29289321881345]){
            translate(v=[30.530689059287177, 30.53068905928717, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, -0.7071067811865472]){
            translate(v=[2.6438235091932444e-15, 43.17691453623979, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -90.70710678118654]){
            translate(v=[-30.53068905928717, 30.530689059287177, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 179.29289321881345]){
            translate(v=[-43.17691453623979, 5.287647018386489e-15, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 89.29289321881345]){
            translate(v=[-30.53068905928718, -30.53068905928717, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, -0.7071067811865472]){
            translate(v=[-7.931470527579733e-15, -43.17691453623979, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -90.70710678118654]){
            translate(v=[30.530689059287166, -30.53068905928718, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -6.0]){
                        cylinder(h=24, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
    };
};
// 0_create_cylinder_with_cutout_inner_63.96152422706632mm_outer137.51150572225254mm_thickness12mm 
// 1_ops_magnet_ 
// 2_ops_magnet_ 
// 3_ops_magnet_ 
// 4_ops_magnet_ 
// 5_ops_magnet_ 
// 6_ops_magnet_ 
// 7_ops_magnet_ 
// 8_ops_magnet_ 
