projection(cut = true) union(){
    difference(){
        union(){
            difference(){
                cylinder(h=12, d=72.0, center=true);
                cylinder(h=12.00001, d=24, center=true);
            };
        }; // create_cylinder_with_cutout_inner_24mm_outer72.0mm_thickness12mm
        union(){
            rotate(a=[0, 0, 0.0]){
                translate(v=[24.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 0.0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[30.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[35.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag0", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 0.0]
        union(){
            rotate(a=[0, 0, 45.0]){
                translate(v=[24.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 45.0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[30.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[35.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag1", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 45.0]
        union(){
            rotate(a=[0, 0, 90.0]){
                translate(v=[24.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 90.0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[30.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[35.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag2", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 90.0]
        union(){
            rotate(a=[0, 0, 135.0]){
                translate(v=[24.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 135.0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[30.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[35.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag3", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 135.0]
        union(){
            rotate(a=[0, 0, 180.0]){
                translate(v=[24.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 0.0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[30.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[35.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag4", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 180.0]
        union(){
            rotate(a=[0, 0, 225.0]){
                translate(v=[24.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 45.0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[30.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[35.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag5", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 225.0]
        union(){
            rotate(a=[0, 0, 270.0]){
                translate(v=[24.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 90.0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[30.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[35.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag6", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 270.0]
        union(){
            rotate(a=[0, 0, 315.0]){
                translate(v=[24.0, 0.0, 0.0]){
                    rotate(a=[0, 0, 135.0]){
                        cube(size=[12.1, 12.1, 12.1], center=true);
                    };
                };
                translate(v=[30.05, 0, -12.1]){
                    cylinder(h=24, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                translate(v=[35.05, 2.4, 0]){
                    linear_extrude(height=12){
                        rotate(a=[0, 0, 90]){
                            mirror([1, 0, 0]){
                                text(text="mag7", size=2);
                            };
                        };
                    };
                };
            };
        }; // create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 315.0]
    };
};

// 0_create_cylinder_with_cutout_inner_24mm_outer72.0mm_thickness12mm 
// 1_create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 0.0] 
// 2_create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 45.0] 
// 3_create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 90.0] 
// 4_create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 135.0] 
// 5_create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 180.0] 
// 6_create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 225.0] 
// 7_create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 270.0] 
// 8_create_magnet_pos[24.0, 0.0, 0.0]rot[0, 0, 315.0] 
