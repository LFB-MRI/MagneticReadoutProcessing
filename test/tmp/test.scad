projection(cut = true) union(){
    difference(){
        union(){
            union(){
                difference(){
                    cylinder(h=20.784609690826528, d=146.51150572225254, center=true);
                    cylinder(h=20.78560969082653, d=69.96152422706632, center=true);
                };
            }; // create_cylinder_with_cutout_inner_69.96152422706632mm_outer146.51150572225254mm_thickness20.784609690826528mm
            union(){
                difference(){
                    cylinder(h=20.784609690826528, d=145.51150572225254, center=true);
                    cylinder(h=20.784609690826528, d=151.51150572225254, center=true);
                }; // mount_contruction_helper_cylinder
                translate(v=[0, -79.75575286112627, 0]){
                    difference(){
                        cube(size=[100, 20, 20.784609690826528], center=true); // mount_base
                        union(){
                            translate(v=[40.0, 0, 0]){
                                cylinder(h=20.784609690826528, d=10);
                            }; // mount_hole_a
                            translate(v=[-40.0, 0, 0]){
                                cylinder(h=20.784609690826528, d=10);
                            }; // mount_hole_a
                        };
                    };
                }; // mount_bar_top
            }; // append_mounting_holes_to_base_slice_10_100
        };
        rotate(a=[0.0, 0.0, 179.29289321881345]){
            translate(v=[49.17691453623979, 0.0, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 119.29289321881346]){
            translate(v=[42.588457268119896, 24.588457268119893, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 59.292893218813454]){
            translate(v=[24.588457268119903, 42.588457268119896, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, -0.7071067811865472]){
            translate(v=[3.0112175489374502e-15, 49.17691453623979, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -60.70710678118658]){
            translate(v=[-24.588457268119885, 42.588457268119896, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -120.70710678118655]){
            translate(v=[-42.588457268119896, 24.588457268119893, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 179.29289321881345]){
            translate(v=[-49.17691453623979, 6.0224350978749004e-15, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 119.29289321881346]){
            translate(v=[-42.588457268119896, -24.588457268119903, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, 59.292893218813454]){
            translate(v=[-24.588457268119917, -42.58845726811988, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[0.0, 0.0, -0.7071067811865472]){
            translate(v=[-9.033652646812351e-15, -49.17691453623979, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -60.70710678118658]){
            translate(v=[24.588457268119903, -42.588457268119896, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
        rotate(a=[-0.0, -0.0, -120.70710678118655]){
            translate(v=[42.58845726811988, -24.588457268119917, 0.0]){
                union(){
                    cube(size=[13.0, 13.0, 13.0], center=true); // magpylib.magnet.Cuboid
                    translate(v=[6.5, 0, -10.392304845413264]){
                        cylinder(h=41.569219381653056, d=6.5);
                    }; // annotation_cube
                };
            };
        }; // ops_magnet_
    };
};

// 0_create_cylinder_with_cutout_inner_69.96152422706632mm_outer146.51150572225254mm_thickness20.784609690826528mm 
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
