projection(cut = true) union(){
    difference(){
        union(){
            union(){
                difference(){
                    cylinder(h=12.0, d=72.0, center=true);
                    cylinder(h=12.001, d=24, center=true);
                };
            }; // create_cylinder_with_cutout_inner_24mm_outer72.0mm_thickness12.0mm
            union(){
                difference(){
                    cylinder(h=12.0, d=71.0, center=true);
                    cylinder(h=12.0, d=77.0, center=true);
                }; // mount_contruction_helper_cylinder
                translate(v=[0, -42.5, 0]){
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
            translate(v=[24.0, 0.0, 0.0]){
                union(){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                    translate(v=[6.05, 0, -6.0]){
                        cylinder(h=24.0, d=6.05);
                    };
                    linear_extrude(height=12.0){
                        rotate(a=[0, 0, 0]){
                            translate(v=[9.0, 6.383333333333333, -12.0]){
                                mirror([1, 0, 0]){
                                    text(text="t2:i0", size=2);
                                };
                            };
                        };
                    };
                };
            };
        };
        rotate(a=[-0.0, -0.0, -90.70710678118654]){
            translate(v=[16.970562748477143, 16.97056274847714, 0.0]){
                union(){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                    translate(v=[6.05, 0, -6.0]){
                        cylinder(h=24.0, d=6.05);
                    };
                    linear_extrude(height=12.0){
                        rotate(a=[0, 0, 0]){
                            translate(v=[9.0, 6.383333333333333, -12.0]){
                                mirror([1, 0, 0]){
                                    text(text="t2:i0", size=2);
                                };
                            };
                        };
                    };
                };
            };
        };
        rotate(a=[0.0, 0.0, -0.7071067811865472]){
            translate(v=[1.4695761589768238e-15, 24.0, 0.0]){
                union(){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                    translate(v=[6.05, 0, -6.0]){
                        cylinder(h=24.0, d=6.05);
                    };
                    linear_extrude(height=12.0){
                        rotate(a=[0, 0, 0]){
                            translate(v=[9.0, 6.383333333333333, -12.0]){
                                mirror([1, 0, 0]){
                                    text(text="t2:i0", size=2);
                                };
                            };
                        };
                    };
                };
            };
        };
        rotate(a=[0.0, 0.0, 89.29289321881345]){
            translate(v=[-16.97056274847714, 16.970562748477143, 0.0]){
                union(){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                    translate(v=[6.05, 0, -6.0]){
                        cylinder(h=24.0, d=6.05);
                    };
                    linear_extrude(height=12.0){
                        rotate(a=[0, 0, 0]){
                            translate(v=[9.0, 6.383333333333333, -12.0]){
                                mirror([1, 0, 0]){
                                    text(text="t2:i0", size=2);
                                };
                            };
                        };
                    };
                };
            };
        };
        rotate(a=[0.0, 0.0, 179.29289321881345]){
            translate(v=[-24.0, 2.9391523179536475e-15, 0.0]){
                union(){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                    translate(v=[6.05, 0, -6.0]){
                        cylinder(h=24.0, d=6.05);
                    };
                    linear_extrude(height=12.0){
                        rotate(a=[0, 0, 0]){
                            translate(v=[9.0, 6.383333333333333, -12.0]){
                                mirror([1, 0, 0]){
                                    text(text="t2:i0", size=2);
                                };
                            };
                        };
                    };
                };
            };
        };
        rotate(a=[-0.0, -0.0, -90.70710678118654]){
            translate(v=[-16.970562748477143, -16.97056274847714, 0.0]){
                union(){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                    translate(v=[6.05, 0, -6.0]){
                        cylinder(h=24.0, d=6.05);
                    };
                    linear_extrude(height=12.0){
                        rotate(a=[0, 0, 0]){
                            translate(v=[9.0, 6.383333333333333, -12.0]){
                                mirror([1, 0, 0]){
                                    text(text="t2:i0", size=2);
                                };
                            };
                        };
                    };
                };
            };
        };
        rotate(a=[0.0, 0.0, -0.7071067811865472]){
            translate(v=[-4.408728476930472e-15, -24.0, 0.0]){
                union(){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                    translate(v=[6.05, 0, -6.0]){
                        cylinder(h=24.0, d=6.05);
                    };
                    linear_extrude(height=12.0){
                        rotate(a=[0, 0, 0]){
                            translate(v=[9.0, 6.383333333333333, -12.0]){
                                mirror([1, 0, 0]){
                                    text(text="t2:i0", size=2);
                                };
                            };
                        };
                    };
                };
            };
        };
        rotate(a=[0.0, 0.0, 89.29289321881345]){
            translate(v=[16.970562748477136, -16.970562748477143, 0.0]){
                union(){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                    translate(v=[6.05, 0, -6.0]){
                        cylinder(h=24.0, d=6.05);
                    };
                    linear_extrude(height=12.0){
                        rotate(a=[0, 0, 0]){
                            translate(v=[9.0, 6.383333333333333, -12.0]){
                                mirror([1, 0, 0]){
                                    text(text="t2:i0", size=2);
                                };
                            };
                        };
                    };
                };
            };
        };
    };
};

// 0_create_cylinder_with_cutout_inner_24mm_outer72.0mm_thickness12.0mm 
// 1_None 
// 2_None 
// 3_None 
// 4_None 
// 5_None 
// 6_None 
// 7_None 
// 8_None 
