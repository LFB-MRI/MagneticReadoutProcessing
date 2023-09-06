projection(cut = true) union(){
    difference(){
        union(){
            union(){
                difference(){
                    cylinder(h=12.2, d=286.9415316289918, center=true);
                    cylinder(h=12.200999999999999, d=227.05846837100816, center=true);
                };
            }; // create_cylinder_with_cutout_inner_227.05846837100816mm_outer286.9415316289918mm_thickness12.2mm
            union(){
                difference(){
                    cylinder(h=12, d=285.9415316289918, center=true);
                    cylinder(h=12, d=288.9415316289918, center=true);
                }; // mount_contruction_helper_cylinder
                translate(v=[0, -145.4707658144959, 0]){
                    difference(){
                        cube(size=[290, 20, 12], center=true); // mount_base
                        union(){
                            translate(v=[135.0, 0, -12]){
                                cylinder(h=18.2, d=10);
                            }; // mount_hole_a
                            translate(v=[-135.0, 0, -12]){
                                cylinder(h=18.2, d=10);
                            }; // mount_hole_a
                        };
                    };
                }; // mount_bar_top
            }; // append_mounting_holes_to_base_slice_10_290
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[126.0, 0.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 156.79289321881345]){
                translate(v=[123.57894533080703, 24.58138057403216, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[116.40882109642213, 48.21811247800131, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 111.79289321881346]){
                translate(v=[104.7651711501207, 70.00184936046988, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[89.095454429505, 89.09545442950498, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 66.79289321881346]){
                translate(v=[70.00184936046989, 104.7651711501207, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[48.218112478001316, 116.40882109642213, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 21.792893218813454]){
                translate(v=[24.58138057403217, 123.57894533080703, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[7.715274834628325e-15, 126.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -23.207106781186575]){
                translate(v=[-24.581380574032153, 123.57894533080703, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[-48.2181124780013, 116.40882109642213, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -68.20710678118657]){
                translate(v=[-70.00184936046989, 104.76517115012068, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[-89.09545442950498, 89.095454429505, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -113.20710678118657]){
                translate(v=[-104.76517115012071, 70.00184936046988, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[-116.40882109642213, 48.21811247800132, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -158.20710678118658]){
                translate(v=[-123.57894533080703, 24.58138057403215, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 179.29289321881345]){
                translate(v=[-126.0, 1.543054966925665e-14, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 156.79289321881345]){
                translate(v=[-123.57894533080703, -24.581380574032174, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 134.29289321881345]){
                translate(v=[-116.40882109642214, -48.218112478001295, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 111.79289321881346]){
                translate(v=[-104.7651711501207, -70.00184936046989, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 89.29289321881345]){
                translate(v=[-89.09545442950501, -89.09545442950498, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 66.79289321881346]){
                translate(v=[-70.00184936046988, -104.7651711501207, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 44.29289321881345]){
                translate(v=[-48.21811247800128, -116.40882109642214, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, 21.792893218813454]){
                translate(v=[-24.581380574032213, -123.57894533080702, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[0.0, 0.0, -0.7071067811865472]){
                translate(v=[-2.3145824503884975e-14, -126.0, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -23.207106781186575]){
                translate(v=[24.581380574032167, -123.57894533080703, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -45.707106781186546]){
                translate(v=[48.21811247800134, -116.40882109642212, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -68.20710678118657]){
                translate(v=[70.00184936046983, -104.76517115012072, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -90.70710678118654]){
                translate(v=[89.09545442950497, -89.09545442950501, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -113.20710678118657]){
                translate(v=[104.7651711501207, -70.00184936046988, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -135.70710678118655]){
                translate(v=[116.40882109642214, -48.21811247800129, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
        union(){
            rotate(a=[-0.0, -0.0, -158.20710678118658]){
                translate(v=[123.57894533080702, -24.58138057403222, 0.0]){
                    union(){
                        cube(size=[12.2, 12.2, 12.2], center=true); // magpylib.magnet.Cuboid
                        translate(v=[6.1, 0, -6.0]){
                            cylinder(h=24, d=6.1);
                        }; // annotation_cube
                    };
                };
            }; // ops_magnet_
        };
    };
};

// 0_create_cylinder_with_cutout_inner_227.05846837100816mm_outer286.9415316289918mm_thickness12.2mm 
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
