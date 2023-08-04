projection(cut = true) union(){
    difference(){
        union(){
            cylinder(h=12, d=104, center=true);
        }; // create_cylinder_with_cutout_inner_30mm_outer104mm_thickness12mm
        union(){
            rotate(a=[0, 0, 0.0]){
                translate(v=[23.0, 0.0, 0.0]){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                };
                translate(v=[29.05, 0, 0]){
                    cylinder(h=12, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                linear_extrude(height=12){
                    text(text=123, size=50);
                };
            };
        }; // create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 0.0]
        union(){
            rotate(a=[0, 0, 45.0]){
                translate(v=[23.0, 0.0, 0.0]){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                };
                translate(v=[29.05, 0, 0]){
                    cylinder(h=12, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                linear_extrude(height=12){
                    text(text=123, size=50);
                };
            };
        }; // create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 45.0]
        union(){
            rotate(a=[0, 0, 90.0]){
                translate(v=[23.0, 0.0, 0.0]){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                };
                translate(v=[29.05, 0, 0]){
                    cylinder(h=12, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                linear_extrude(height=12){
                    text(text=123, size=50);
                };
            };
        }; // create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 90.0]
        union(){
            rotate(a=[0, 0, 135.0]){
                translate(v=[23.0, 0.0, 0.0]){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                };
                translate(v=[29.05, 0, 0]){
                    cylinder(h=12, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                linear_extrude(height=12){
                    text(text=123, size=50);
                };
            };
        }; // create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 135.0]
        union(){
            rotate(a=[0, 0, 180.0]){
                translate(v=[23.0, 0.0, 0.0]){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                };
                translate(v=[29.05, 0, 0]){
                    cylinder(h=12, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                linear_extrude(height=12){
                    text(text=123, size=50);
                };
            };
        }; // create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 180.0]
        union(){
            rotate(a=[0, 0, 225.0]){
                translate(v=[23.0, 0.0, 0.0]){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                };
                translate(v=[29.05, 0, 0]){
                    cylinder(h=12, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                linear_extrude(height=12){
                    text(text=123, size=50);
                };
            };
        }; // create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 225.0]
        union(){
            rotate(a=[0, 0, 270.0]){
                translate(v=[23.0, 0.0, 0.0]){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                };
                translate(v=[29.05, 0, 0]){
                    cylinder(h=12, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                linear_extrude(height=12){
                    text(text=123, size=50);
                };
            };
        }; // create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 270.0]
        union(){
            rotate(a=[0, 0, 315.0]){
                translate(v=[23.0, 0.0, 0.0]){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                };
                translate(v=[29.05, 0, 0]){
                    cylinder(h=12, d=4.033333333333333);
                }; // annotation_cube_d12.1_h12
                linear_extrude(height=12){
                    text(text=123, size=50);
                };
            };
        }; // create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 315.0]
    };
};

// 0_create_cylinder_with_cutout_inner_30mm_outer104mm_thickness12mm 
// 1_create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 0.0] 
// 2_create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 45.0] 
// 3_create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 90.0] 
// 4_create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 135.0] 
// 5_create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 180.0] 
// 6_create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 225.0] 
// 7_create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 270.0] 
// 8_create_magnet_pos[23.0, 0.0, 0.0]rot[0, 0, 315.0] 
