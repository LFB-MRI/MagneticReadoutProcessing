projection(cut = true) union(){
    difference(){
        union(){
            union(){
                difference(){
                    cylinder(h=15.2, d=266.1769145362398, center=true);
                    cylinder(h=15.200999999999999, d=41.29385127825613, center=true);
                };
            }; // create_cylinder_with_cutout_inner_41.29385127825613mm_outer266.1769145362398mm_thickness15.2mm
            union(){
                difference(){
                    cylinder(h=15, d=265.1769145362398, center=true);
                    cylinder(h=15, d=268.1769145362398, center=true);
                }; // mount_contruction_helper_cylinder
                translate(v=[0, -135.0884572681199, 0]){
                    difference(){
                        cube(size=[270, 20, 15], center=true); // mount_base
                        union(){
                            translate(v=[125.0, 0, -15]){
                                cylinder(h=22.7, d=10);
                            }; // mount_hole_a
                            translate(v=[-125.0, 0, -15]){
                                cylinder(h=22.7, d=10);
                            }; // mount_hole_a
                        };
                    };
                }; // mount_bar_top
            }; // append_mounting_holes_to_base_slice_10_270
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[112.5, 0.0, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 149.29289321881345]){
                translate(v=[108.66665545752018, 29.117142574033583, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[97.42785792574935, 56.24999999999999, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[79.5495128834866, 79.54951288348659, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[56.250000000000014, 97.42785792574934, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 29.292893218813454]){
                translate(v=[29.117142574033583, 108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[6.8886382452038615e-15, 112.5, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -30.707106781186567]){
                translate(v=[-29.117142574033597, 108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[-56.24999999999997, 97.42785792574935, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-79.54951288348659, 79.5495128834866, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[-97.42785792574935, 56.24999999999999, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -150.70710678118658]){
                translate(v=[-108.66665545752018, 29.117142574033615, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-112.5, 1.3777276490407723e-14, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 149.29289321881345]){
                translate(v=[-108.66665545752018, -29.11714257403359, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[-97.42785792574934, -56.250000000000014, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-79.54951288348661, -79.54951288348659, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[-56.25000000000005, -97.42785792574932, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 29.292893218813454]){
                translate(v=[-29.117142574033572, -108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-2.0665914735611585e-14, -112.5, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -30.707106781186567]){
                translate(v=[29.117142574033533, -108.66665545752019, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[56.250000000000014, -97.42785792574934, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[79.54951288348657, -79.54951288348661, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[97.42785792574932, -56.25000000000005, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -150.70710678118658]){
                translate(v=[108.66665545752018, -29.117142574033576, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[30.0, 0.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[21.213203435596427, 21.213203435596423, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[1.83697019872103e-15, 30.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-21.213203435596423, 21.213203435596427, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-30.0, 3.67394039744206e-15, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-21.21320343559643, -21.213203435596423, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-5.510910596163089e-15, -30.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[21.21320343559642, -21.21320343559643, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[54.0, 0.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[49.88949475560948, 20.66490534771485, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[38.18376618407357, 38.18376618407356, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[20.66490534771485, 49.88949475560948, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[3.3065463576978537e-15, 54.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[-20.664905347714846, 49.88949475560948, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-38.18376618407356, 38.18376618407357, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[-49.88949475560948, 20.664905347714853, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-54.0, 6.6130927153957075e-15, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[-49.88949475560949, -20.664905347714843, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-38.183766184073576, -38.18376618407356, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[-20.664905347714832, -49.88949475560949, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-9.91963907309356e-15, -54.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[20.66490534771486, -49.889494755609476, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[38.183766184073555, -38.183766184073576, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[49.88949475560949, -20.664905347714836, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[112.5, 0.0, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 149.29289321881345]){
                translate(v=[108.66665545752018, 29.117142574033583, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[97.42785792574935, 56.24999999999999, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[79.5495128834866, 79.54951288348659, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[56.250000000000014, 97.42785792574934, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 29.292893218813454]){
                translate(v=[29.117142574033583, 108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[6.8886382452038615e-15, 112.5, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -30.707106781186567]){
                translate(v=[-29.117142574033597, 108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[-56.24999999999997, 97.42785792574935, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-79.54951288348659, 79.5495128834866, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[-97.42785792574935, 56.24999999999999, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -150.70710678118658]){
                translate(v=[-108.66665545752018, 29.117142574033615, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-112.5, 1.3777276490407723e-14, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 149.29289321881345]){
                translate(v=[-108.66665545752018, -29.11714257403359, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[-97.42785792574934, -56.250000000000014, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-79.54951288348661, -79.54951288348659, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[-56.25000000000005, -97.42785792574932, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 29.292893218813454]){
                translate(v=[-29.117142574033572, -108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-2.0665914735611585e-14, -112.5, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -30.707106781186567]){
                translate(v=[29.117142574033533, -108.66665545752019, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[56.250000000000014, -97.42785792574934, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[79.54951288348657, -79.54951288348661, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[97.42785792574932, -56.25000000000005, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -150.70710678118658]){
                translate(v=[108.66665545752018, -29.117142574033576, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[30.0, 0.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[21.213203435596427, 21.213203435596423, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[1.83697019872103e-15, 30.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-21.213203435596423, 21.213203435596427, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-30.0, 3.67394039744206e-15, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-21.21320343559643, -21.213203435596423, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-5.510910596163089e-15, -30.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[21.21320343559642, -21.21320343559643, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[54.0, 0.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[49.88949475560948, 20.66490534771485, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[38.18376618407357, 38.18376618407356, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[20.66490534771485, 49.88949475560948, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[3.3065463576978537e-15, 54.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[-20.664905347714846, 49.88949475560948, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-38.18376618407356, 38.18376618407357, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[-49.88949475560948, 20.664905347714853, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-54.0, 6.6130927153957075e-15, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[-49.88949475560949, -20.664905347714843, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-38.183766184073576, -38.18376618407356, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[-20.664905347714832, -49.88949475560949, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-9.91963907309356e-15, -54.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[20.66490534771486, -49.889494755609476, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[38.183766184073555, -38.183766184073576, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[49.88949475560949, -20.664905347714836, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[112.5, 0.0, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 149.29289321881345]){
                translate(v=[108.66665545752018, 29.117142574033583, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[97.42785792574935, 56.24999999999999, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[79.5495128834866, 79.54951288348659, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[56.250000000000014, 97.42785792574934, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 29.292893218813454]){
                translate(v=[29.117142574033583, 108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[6.8886382452038615e-15, 112.5, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -30.707106781186567]){
                translate(v=[-29.117142574033597, 108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[-56.24999999999997, 97.42785792574935, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-79.54951288348659, 79.5495128834866, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[-97.42785792574935, 56.24999999999999, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -150.70710678118658]){
                translate(v=[-108.66665545752018, 29.117142574033615, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-112.5, 1.3777276490407723e-14, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 149.29289321881345]){
                translate(v=[-108.66665545752018, -29.11714257403359, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 119.29289321881346]){
                translate(v=[-97.42785792574934, -56.250000000000014, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-79.54951288348661, -79.54951288348659, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 59.292893218813454]){
                translate(v=[-56.25000000000005, -97.42785792574932, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 29.292893218813454]){
                translate(v=[-29.117142574033572, -108.66665545752018, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-2.0665914735611585e-14, -112.5, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -30.707106781186567]){
                translate(v=[29.117142574033533, -108.66665545752019, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -60.70710678118658]){
                translate(v=[56.250000000000014, -97.42785792574934, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[79.54951288348657, -79.54951288348661, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -120.70710678118655]){
                translate(v=[97.42785792574932, -56.25000000000005, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -150.70710678118658]){
                translate(v=[108.66665545752018, -29.117142574033576, 0.0]){
                    union(){
                        cube(size=[15.2, 15.2, 15.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[7.6, 0, -7.5]){
                            cylinder(h=30, d=7.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[30.0, 0.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[21.213203435596427, 21.213203435596423, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[1.83697019872103e-15, 30.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-21.213203435596423, 21.213203435596427, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-30.0, 3.67394039744206e-15, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-21.21320343559643, -21.213203435596423, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-5.510910596163089e-15, -30.0, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[21.21320343559642, -21.21320343559643, 0.0]){
                    union(){
                        cube(size=[9.2, 9.2, 9.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[4.6, 0, -7.5]){
                            cylinder(h=30, d=4.6);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[54.0, 0.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[49.88949475560948, 20.66490534771485, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[38.18376618407357, 38.18376618407356, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[20.66490534771485, 49.88949475560948, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[3.3065463576978537e-15, 54.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[-20.664905347714846, 49.88949475560948, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-38.18376618407356, 38.18376618407357, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[-49.88949475560948, 20.664905347714853, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-54.0, 6.6130927153957075e-15, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[-49.88949475560949, -20.664905347714843, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-38.183766184073576, -38.18376618407356, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[-20.664905347714832, -49.88949475560949, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-9.91963907309356e-15, -54.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[20.66490534771486, -49.889494755609476, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[38.183766184073555, -38.183766184073576, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[49.88949475560949, -20.664905347714836, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -7.5]){
                            cylinder(h=30, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
    };
};

// 0_create_cylinder_with_cutout_inner_41.29385127825613mm_outer266.1769145362398mm_thickness15.2mm 
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
// 13_None 
// 14_None 
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
// 27_None 
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
// 44_None 
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
// 65_None 
// 66_None 
// 67_None 
// 68_None 
// 69_None 
// 70_None 
// 71_None 
// 72_None 
// 73_None 
// 74_None 
// 75_None 
// 76_None 
// 77_None 
// 78_None 
// 79_None 
// 80_None 
// 81_None 
// 82_None 
// 83_None 
// 84_None 
// 85_None 
// 86_None 
// 87_None 
// 88_None 
// 89_None 
// 90_None 
// 91_None 
// 92_None 
// 93_None 
// 94_None 
// 95_None 
// 96_None 
// 97_None 
// 98_None 
// 99_None 
// 100_None 
// 101_None 
// 102_None 
// 103_None 
// 104_None 
// 105_None 
// 106_None 
// 107_None 
// 108_None 
// 109_None 
// 110_None 
// 111_None 
// 112_None 
// 113_None 
// 114_None 
// 115_None 
// 116_None 
// 117_None 
// 118_None 
// 119_None 
// 120_None 
// 121_None 
// 122_None 
// 123_None 
// 124_None 
// 125_None 
// 126_None 
// 127_None 
// 128_None 
// 129_None 
// 130_None 
// 131_None 
// 132_None 
// 133_None 
// 134_None 
// 135_None 
// 136_None 
// 137_None 
// 138_None 
// 139_None 
// 140_None 
// 141_None 
// 142_None 
// 143_None 
// 144_None 
