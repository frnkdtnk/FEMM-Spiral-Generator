import femm

#

# Start up and connect to FEMM
femm.openfemm()
# Create a new msgnetics problem
femm.newdocument(0)


########################VARIABLES################################
#coil dimensions#
inner_radius=2000;
outer_radius=40000;
wire_spacing=188;
wire_thickness=60; 
#Current#
i=1; 

#magnet wall dimensions#
wall_distance=30000;
wall_radius=40000;
wall_thickness=10000;

#functional variables#
EXPERIMENT=1;
r=0;
r=inner_radius;
automesh = 1;
meshsize= 30;
minangle= 1;
# Set up problem type. This sets up problem as an axisymmetric problem with units of micrometers
femm.mi_probdef(0,'micrometers','axi',10**(-8),0,minangle,0);

# Add materials to our workspace
femm.mi_addmaterial('magnet',1.05,1.05,922850,0,0.667,0,0,1,0,0,0);
femm.mi_addmaterial('air',1,1,0);
femm.mi_addmaterial('36awgcopper',1,1,0,i/((wire_thickness/2)**(2)*3.14),58,0,0,1,3,0,0,1,127);#change J applied current

#define circuit with current i in series
femm.mi_addcircprop('spiral', i, 1);

#draw and label magnet wall
femm.mi_drawrectangle(0,wall_distance,wall_radius,(wall_distance+wall_thickness));
femm.mi_addblocklabel(wall_radius/2,(wall_distance+wall_thickness/2)); 
femm.mi_selectlabel(wall_radius/2,(wall_distance+wall_thickness/2));
femm.mi_setblockprop('magnet',automesh,meshsize,0,270,0,0);
femm.mi_clearselected();

#draw and label spiral cross section
while(r<outer_radius):
        if (r==inner_radius):
                pass
        else:
                r=r+wire_spacing;

        inner_edge = r;
        outer_edge = r + wire_thickness;
        femm.mi_drawarc(inner_edge,0,outer_edge,0,180,EXPERIMENT);#mi_drawarc(x1,y1,x2,y2,angle,maxseg)
        femm.mi_addarc(outer_edge,0,inner_edge,0,180,EXPERIMENT);#other half of circle
        femm.mi_addblocklabel(((inner_edge+outer_edge)/2),0); 
        femm.mi_selectlabel(((inner_edge+outer_edge)/2),0);
        femm.mi_setblockprop('36awgcopper',automesh,meshsize,'spiral',0,0,1);
        femm.mi_clearselected();
        r=outer_edge;


#define the air
femm.mi_addblocklabel((wall_radius/2),(wall_distance/2));
femm.mi_selectlabel((wall_radius/2),(wall_distance/2));
femm.mi_setblockprop('air',automesh,meshsize,0);
femm.mi_clearselected();

femm.mi_makeABC(1,((wall_distance+outer_radius+wall_radius)*2),0,0,0) 

femm.mi_zoomnatural();

# Save the geometry to disk so we can analyze it
femm.mi_saveas('spiral.fem');





