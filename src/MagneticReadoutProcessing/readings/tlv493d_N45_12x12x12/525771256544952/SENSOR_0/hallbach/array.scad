projection(cut = true) union(){
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
            rotate(a=[0.0, 0.0, 180.0]){
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
                                        text(text="t2:i6", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i6
        };
        union(){
            rotate(a=[0.0, 0.0, 0.0]){
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
                                        text(text="t2:i4", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i4
        };
        union(){
            rotate(a=[0.0, 0.0, 180.0]){
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
                                        text(text="t2:i5", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i5
        };
        union(){
            rotate(a=[0.0, 0.0, 0.0]){
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
                                        text(text="t2:i1", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i1
        };
        union(){
            rotate(a=[0.0, 0.0, 180.0]){
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
                                        text(text="t2:i6", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i6
        };
        union(){
            rotate(a=[0.0, 0.0, 0.0]){
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
                                        text(text="t2:i4", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i4
        };
        union(){
            rotate(a=[0.0, 0.0, 180.0]){
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
                                        text(text="t2:i5", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i5
        };
        union(){
            rotate(a=[0.0, 0.0, 0.0]){
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
                                        text(text="t2:i1", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i1
        };
        union(){
            rotate(a=[0.0, 0.0, 180.0]){
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
                                        text(text="t2:i6", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i6
        };
        union(){
            rotate(a=[0.0, 0.0, 0.0]){
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
                                        text(text="t2:i4", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i4
        };
        union(){
            rotate(a=[0.0, 0.0, 180.0]){
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
                                        text(text="t2:i5", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i5
        };
        union(){
            rotate(a=[0.0, 0.0, 0.0]){
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
                                        text(text="t2:i1", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i1
        };
        union(){
            rotate(a=[0.0, 0.0, 180.0]){
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
                                        text(text="t2:i6", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i6
        };
        union(){
            rotate(a=[0.0, 0.0, 0.0]){
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
                                        text(text="t2:i4", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i4
        };
        union(){
            rotate(a=[0.0, 0.0, 180.0]){
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
                                        text(text="t2:i5", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i5
        };
        union(){
            rotate(a=[0.0, 0.0, 0.0]){
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
                                        text(text="t2:i1", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i1
        };
        union(){
            rotate(a=[0.0, 0.0, 180.0]){
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
                                        text(text="t2:i6", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i6
        };
        union(){
            rotate(a=[0.0, 0.0, 0.0]){
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
                                        text(text="t2:i4", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i4
        };
        union(){
            rotate(a=[0.0, 0.0, 180.0]){
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
                                        text(text="t2:i5", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i5
        };
        union(){
            rotate(a=[0.0, 0.0, 0.0]){
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
                                        text(text="t2:i1", size=2);
                                    };
                                };
                            };
                        }; // annotation_text
                    };
                };
            }; // ops_magnet_t2:i1
        };
    };
};

// 0_create_cylinder_with_cutout_inner_35.05846837100817mm_outer94.94153162899184mm_thickness12.2mm 
// 1_None 
// 2_None 
// 3_None 
// 4_None 
// 5_create_cylinder_with_cutout_inner_35.05846837100817mm_outer94.94153162899184mm_thickness12.2mm 
// 6_None 
// 7_None 
// 8_None 
// 9_None 
// 10_None 
// 11_None 
// 12_None 
// 13_None 
// 14_create_cylinder_with_cutout_inner_35.05846837100817mm_outer94.94153162899184mm_thickness12.2mm 
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
// 27_create_cylinder_with_cutout_inner_35.05846837100817mm_outer94.94153162899184mm_thickness12.2mm 
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
// 44_create_cylinder_with_cutout_inner_35.05846837100817mm_outer94.94153162899184mm_thickness12.2mm 
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
