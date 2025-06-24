import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    #oomp_mode = "project"
    oomp_mode = "oobb"

    test = False
    #test = True

    if typ == "all":
        #no overwrite
        filter = ""; save_type = "all"; navigation = True; overwrite = False; modes = ["3dpr"]; oomp_run = True; test = False
        #default
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = False
        #default
        #filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]
                
        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = ""
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        
        #defining all the plates
        if True:
            plates = []
    
    
            #sizes = ["oobb", "oobe"]
            sizes = ["oobb"]
            
            #base plates
            if True:
                for size in sizes:
                    #all 3m thicks 1x1 to 10x10
                    for wid in range(1, 11):
                        for hei in range(1, 11):
                            if wid >= hei:
                                plates.append({"type": "plate", "width": wid,
                                            "height": hei, "thickness": 3, "size": size})
            #all thicknesses 1x1
            if True:
                depths = []
                for i in range(1, 34):
                    depths.append(i*3)
                for dep in depths:
                    plates.append({"type": "plate", "width": 1, "height": 1,
                            "thickness": dep, "size": size})
                
            #premo_plates
            if True:
                #various plates that also have extra thicknesses
                premo_plates = []
                premo_plates.append([2,1])
                premo_plates.append([3,1])
                premo_plates.append([4,1])
                premo_plates.append([5,1])
                premo_plates.append([7,1])
                premo_plates.append([9,1])
                premo_plates.append([10,1])
                premo_plates.append([11,1])
                premo_plates.append([12,1])
                premo_plates.append([13,1])
                premo_plates.append([15,1])
                premo_plates.append([17,1])
                premo_plates.append([19,1])
                premo_plates.append([20,1])
                premo_plates.append([2,1])
                premo_plates.append([3,3])
                premo_plates.append([5,5])
                premo_plates.append([6,3])
                premo_plates.append([5,3])
                premo_thicknesses = [6, 9, 12, 15,21,30]
                for plate in premo_plates:
                    for thickness in premo_thicknesses:
                        plates.append({"type": "plate", "width": plate[0], "height": plate[1],
                            "thickness": thickness, "size": size})

            #one widers
            if True:
                thicknesses = [3, 6, 9, 12]
                for thickness in thicknesses:
                    for leng in range(2, 35):
                        plates.append({"type": "plate", "width": leng, "height": 1,
                                    "thickness": thickness, "size": size})
            #03s, 05s
            if True:                
                widths = [7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
                heights = [3,5]
                for w in widths:
                    for h in heights:
                        plates.append({"type": "plate", "width": w, "height": h,
                                "thickness": 3, "size": size})
                
            #squares
            if True:
                widths = range(10,21)
                for w in widths:
                    plates.append({"type": "plate", "width": w, "height": w,
                            "thickness": 3, "size": size})
                
            # larger plates of desire
            if True:
                plates.append({"type": "plate", "width": 15, "height": 9,
                            "thickness": 3, "size": size})

                
            # extra fifteens
            if True:
                widths = range(1,21)        
                for w in widths:
                        if w < 15:
                            plates.append({"type": "plate", "width": 15, "height": w,
                                "thickness": 3, "size": size})
                        else:
                            plates.append({"type": "plate", "width": w, "height": 15,
                                "thickness": 3, "size": size})
                
                plates.append({"type": "plate", "width": 15, "height": 14,
                            "thickness": 3, "size": size})
                plates.append({"type": "plate", "width": 15, "height": 13,
                            "thickness": 3, "size": size})
                plates.append({"type": "plate", "width": 15, "height": 12,
                            "thickness": 3, "size": size})
                plates.append({"type": "plate", "width": 15, "height": 11,
                            "thickness": 3, "size": size})
            #special to sort
            if False:    
                size = "oobb"
                plates.append({"type": "plate", "width": 28, "height": 20,
                            "thickness": 3, "size": size, "extra": "paper_sheet_a3"})
                plates.append({"type": "plate", "width": 20, "height": 14,
                            "thickness": 3, "size": size, "extra": "paper_sheet_a4"})
                plates.append({"type": "plate", "width": 14, "height": 10,
                            "thickness": 3, "size": size, "extra": "paper_sheet_a5"})
                plates.append({"type": "plate", "width": 10, "height": 7,
                            "thickness": 3, "size": size, "extra": "paper_sheet_a6"})
                plates.append({"type": "plate", "width": 25, "height": 20,
                            "thickness": 3, "size": size, "extra": "furniture_shelf_ikea_kallax"})
                

                

                size = "oobb"

                #non both_holes ones
                #gorm plates
                #plates.append({"type": "plate", "width": 7, "height": 4, "thickness": 3, "extra":"gorm", "size": size})
                #plates.append({"type": "plate", "width": 5, "height": 2, "thickness": 3, "extra":"gorm", "size": size})

                #ninety_degree plates    
                max = 20
                for i in range(2,max):
                    plates.append({"type": "plate", "width": i, "height": 1, "thickness": 14, "extra":"ninety_degree", "size": size})
                
                cubes = []
                cubes.append([2,2,14])
                cubes.append([3,3,14])
                cubes.append([4,4,14])
                cubes.append([5,5,14])
                cubes.append([2,2,29])
                cubes.append([3,3,29])
                cubes.append([3,3,44])
                
                for cube in cubes:
                    width = cube[0]
                    height = cube[1]
                    thickness = cube[2]
                    plates.append({"type": "plate", "width": width, "height": height, "thickness": thickness, "extra":"ninety_degree", "size": size})


                # l
                thicknesses = [3,6,9,12,15]
                sizes = []
                sizes.append([3,3])
                sizes.append([5,2])
                for thick in thicknesses:
                    for siz in sizes:
                        plates.append({"type": "plate", "width": siz[0], "height": siz[1], "thickness": thick, "extra":"l", "size": size})
                
                # t
                thicknesses = [3,6,9,12,15]
                thicknesses = [3]
                sizes = []
                sizes.append([3,2])    
                sizes.append([3,3])  
                sizes.append([5,2])  
                sizes.append([5,5])  
                for thick in thicknesses:
                    for siz in sizes:
                        plates.append({"type": "plate", "width": siz[0], "height": siz[1], "thickness": thick, "extra":"t", "size": size})

                # u
                thicknesses = [3,6,9,12,15]
                sizes = []
                sizes.append([3,3])
                sizes.append([5,3])
                sizes.append([5,5])
                typs = ["u","u_double"]
                for thick in thicknesses:
                    for siz in sizes:
                        for typ in typs:
                            plates.append({"type": "plate", "width": siz[0], "height": siz[1], "thickness": thick, "extra":typ, "size": size})


                
                # slip_center and slip_end
                widths = [3,5, 7]
                thicknesses = [8.5]
                extras = ["slip_center", "slip_end"]
                for width in widths:
                    for thickness in thicknesses:
                        for extra in extras:
                            pass
                            #plates.append({"type": "plate", "width": width, "height": 1, "thickness": thickness, "extra":extra, "size": size})

                #plates.append({"type": "plate", "width": 3, "height": 3, "thickness": thickness, "extra":"slip_corner", "size": size})

                # labels only the top row of holes
                # t
                thicknesses = [3]
                sizes = []
                sizes.append([3,2])    
                sizes.append([3,3])  
                sizes.append([5,2])  
                sizes.append([5,3]) 
                sizes.append([7,3]) 
                sizes.append([5,5])  
                sizes.append([7,5])
                sizes.append([9,5])
                for thick in thicknesses:
                    for siz in sizes:
                        plates.append({"type": "plate", "width": siz[0], "height": siz[1], "thickness": thick, "extra":"label", "size": size})

            
        
        
        #defining them as parts
        if True:

            extras = []
            extras.append("only_oobb_hole")
            extras.append("only_oobe_hole")            
            extras.append("")
            
            

            part_default = {} 
        
            part_default["project_name"] = project_name
            part_default["full_shift"] = [0, 0, 0]
            part_default["full_rotations"] = [0, 0, 0]
            

            for ex in extras:
                for plate in plates:
                    extra = plate.get("extra", "")
                    wid = plate["width"]
                    hei = plate["height"]
                    dep = plate["thickness"]
                    typ = plate.get("type", "plate")
                    if extra == "" and typ == "plate":
                        part = copy.deepcopy(part_default)
                        p3 = copy.deepcopy(kwargs)
                        p3["width"] = wid
                        p3["height"] = hei
                        p3["thickness"] = dep
                        if ex != "":
                            p3["extra"] = ex
                        part["kwargs"] = p3
                        part["name"] = typ
                        if oomp_mode == "oobb":
                            p3["oomp_size"] = typ
                        if not test:
                            pass
                            parts.append(part)
                    elif extra != "":
                        print(f"Skipping plate {plate} because extra is {extra}")
                    elif typ != "plate":
                        print(f"Skipping plate {plate} because type is {typ}")


        kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []        
        sort.append("name")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        sort.append("extra")
        
        scad_help.generate_navigation(sort = sort)


def get_plate(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    if extra == "":
        p3["both_holes"] = True  
    elif extra == "only_oobb_hole":
        p3["both_holes"] = False  
    elif extra == "only_oobe_hole":
        p3["radius_name"] = "m3"
        p3["both_holes"] = True  
    
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)