projection(cut = true) union(){
    difference(){
        union(){
            cylinder(h=12, d=72.0, center=true);
        }; // create_cylinder_with_cutout_inner_24mm_outer72.0mm_thickness12mm
        rotate(a=[-0.0043635446551485105, 0.7070888304760513, -0.7071426817872533]){
            translate(v=[0.0, 0.0, 0.0]){
                union(){
                    cube(size=[12.1, 12.1, 12.1], center=true);
                    translate(v=[6.05, 0, -6.0]){
                        cylinder(h=24, d=4.033333333333333);
                    };
                };
            };
            #linear_extrude(height=12){
                rotate(a=[0, 0, 0]){
                    translate(v=[7.199999999999999, 6.383333333333333, -12]){
                        mirror([1, 0, 0]){
                            text(text="test", size=2);
                        };
                    };
                };
            };
        };
    };
};

// 0_create_cylinder_with_cutout_inner_24mm_outer72.0mm_thickness12mm 
// 1_None 
