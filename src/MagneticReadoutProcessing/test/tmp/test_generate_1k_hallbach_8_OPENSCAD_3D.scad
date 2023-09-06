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
// 0_create_cylinder_with_cutout_inner_35.05846837100817mm_outer94.94153162899184mm_thickness12.2mm 
// 1_None 
// 2_None 
// 3_None 
// 4_None 
// 5_None 
// 6_None 
// 7_None 
// 8_None 
