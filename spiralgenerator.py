import femm

#

# Start up and connect to FEMM
femm.openfemm()

# Create a new electrostatics problem
femm.newdocument(0)


########################VARIABLES################################
#coil dimensions#
inner_radius=0;
outer_radius=7.75;
wire_spacing=0.5;
wire_thickness=0.25; #mm
#Current#
i=1; 

#wall dimensions#
wall_distance=5;
wall_radius=3;
wall_thickness=0.5;

#functional variables#
EXPERIMENT=10;
r=0;
r=inner_radius;


# Set up problem type. This sets up problem as an axisymmetric problem with units of micrometers
femm.mi_probdef(0,'micrometers','axi',10**(-8),0,30,0);

# Add materials to our workspace
femm.mi_addmaterial('magnet',1.05,1.05,922850,0,0.667,0,0,1,0,0,0);
femm.mi_addmaterial('air',1,1,0);
femm.mi_addmaterial('10awgcopper',1,1,0,0,58,0,0,1,3,0,0,1,2588);

#define circuit with current i in series
femm.mi_addcircprop('spiral', i, 1);

#draw and label magnet wall
femm.mi_drawrectangle(0,wall_distance,wall_radius,(wall_distance+wall_thickness));
femm.mi_addblocklabel(wall_radius/2,(wall_distance+wall_thickness/2)); 
femm.mi_selectlabel(wall_radius/2,(wall_distance+wall_thickness/2));
femm.mi_setblockprop('magnet',0,1,0,270,0,0);
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
        femm.mi_setblockprop('10awgcopper',0,1,'spiral',None,0,1);
        femm.mi_clearselected();
        r=outer_edge;


#define the air
femm.mi_addblocklabel((wall_radius/2),(wall_distance/2));
femm.mi_selectlabel((wall_radius/2),(wall_distance/2));
femm.mi_setblockprop('air',0,1,0);
femm.mi_clearselected();

femm.mi_makeABC(7,(outer_radius*2),0,0,0) 

femm.mi_zoomnatural();

# Save the geometry to disk so we can analyze it
femm.mi_saveas('spiral.fem');




