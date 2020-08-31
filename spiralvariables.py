#########COIL DIMENSIONS########
#takes input variables and setting for which variable to solve for
#put values for variables below, leave unknown variables as zero
#CAN ONLY SET ONE VARIABLE AS 0 AT A TIME
inner_radius=100;
outer_radius=1100;
wire_spacing=100;
wire_diameter=100; #mm, 10awg magnet wire
turns = 0; #number of turns 

#variables for spiral that will be provided,
#put one if variable will be provided,
#and put 0 if it must be solved for.
#CAN ONLY SOLVE FOR ONE AT A TIME
inner_radius_state = 1;
outer_radius_state = 1;
wire_spacing_state =1;
wire_diameter_state=1;
turns_state = 0;
print(hello)
if (inner_radius_state==0):
    inner_radius=outer_radius-(turns*wire_diameter+(turns-1)*wire_spacing);
    print(inner_radius);
if (outer_radius_state==0):
    outer_radius=inner_radius+wire_thickness+(turns-1)*(wire_thickness+wire_spacing)
    print(outer_radius);
if (wire_spacing_state==0):
    wire_spacing=(outer_radius-inner_radius-turns*wire_diameter)/(turns-1)
    print(wire_spacing);
if (wire_thickness_state==0):
    wire_diameter=(outer_radius-inner_radius-(turns-1)*wire_spacing)/turns
    print(wire_diameter);
if (turns_state==0):
    turns=(outer_radius-inner_radius+wire_spacing)/(wire_diameter+wire_spacing)
    print(turns);


  
