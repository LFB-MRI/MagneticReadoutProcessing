projection(cut = true) union(){
    difference(){
        union(){
            difference(){
                cylinder(h=12, d=96, center=true);
                cylinder(h=12.00001, d=48, center=true);
            };
        }; // create_cylinder_with_cutout_inner_48mm_outer96mm_thickness12mm
        union(){
            rotate(a=[0, 0, 0.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag0", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 0.0]
        union(){
            rotate(a=[0, 0, 30.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag1", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 30.0]
        union(){
            rotate(a=[0, 0, 60.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag2", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 60.0]
        union(){
            rotate(a=[0, 0, 90.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag3", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 90.0]
        union(){
            rotate(a=[0, 0, 120.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag4", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 120.0]
        union(){
            rotate(a=[0, 0, 150.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag5", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 150.0]
        union(){
            rotate(a=[0, 0, 180.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 180]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag6", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 180.0]
        union(){
            rotate(a=[0, 0, 210.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 180]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag7", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 210.0]
        union(){
            rotate(a=[0, 0, 240.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 180]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag8", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 240.0]
        union(){
            rotate(a=[0, 0, 270.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 180]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag9", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 270.0]
        union(){
            rotate(a=[0, 0, 300.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 180]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 3.0, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag10", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 300.0]
        union(){
            rotate(a=[0, 0, 330.0]){
                translate(v=[32.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 180]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[38.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[43.05, 3.0, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag11", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 330.0]
    };
};

// 0_create_cylinder_with_cutout_inner_48mm_outer96mm_thickness12mm 
// 1_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 0.0] 
// 2_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 30.0] 
// 3_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 60.0] 
// 4_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 90.0] 
// 5_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 120.0] 
// 6_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 150.0] 
// 7_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 180.0] 
// 8_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 210.0] 
// 9_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 240.0] 
// 10_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 270.0] 
// 11_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 300.0] 
// 12_create_magnet_pos[32.0, 0.0, 0.0]rot[0, 0, 330.0] 
