from bpy.types import Operator, Panel
import bpy

SPACER = "    "
CURRENT_DIRECTORY = "/Users/JesperBertelsen/Desktop/Crazy/Uni/Programmering/Projekt/Python"
class Snemand(Operator): 
    """Tooltip"""
    bl_idname = "object.snemand_operator"
    bl_label = "Lav en snemand"
    
    def execute(self,context):
        self.indsamlData() #- This is used to gather location data of the object. Only to be used while developing the snowmand. 
        return {'FINISHED'}
    
    
    def writeCollection(self, file, collection): #Used to write python layout code for each collection. 
        collectionsToWrite = [ # I only care about these collections
            "Body - Big blocks",
            "Body - Small blocks",
            "Carrot - Big blocks",
            "Carrot - Small blocks",
            "Hat - Big blocks", 
            "Hat - Small blocks", 
            "Eyes"
            ]
        if collection.name not in collectionsToWrite: return # Check get in or get out.     
        col_name = collection.name.replace(" - ", "_").replace(" ","_") # Ændre text lignede overskrifter til overskrifter som variabler kan have. 
        file.write(f"{SPACER}{col_name} = (\n")
        for object in collection.all_objects:                     
            file.write(SPACER*2 + "(\n")
            file.write(SPACER*3 + "{\n")
            
            file.write(SPACER*4 + "\"x\":" + str(object.location.x) + ",\n")  # x
            file.write(SPACER*4 + "\"y\":" + str(object.location.y) + ",\n")  # y
            file.write(SPACER*4 + "\"z\":" + str(object.location.z) + "\n")  # z
            
            file.write(SPACER*3 + "}\n")
            file.write(SPACER*2 + "),\n") 
        file.write(SPACER + ")\n")   
        
    def indsamlData(self): 
        fileName = "Blocks"
        fileType = "py"
        dataFolder = "Data" 
        url = CURRENT_DIRECTORY + "/" + dataFolder + "/" + fileName + "." + fileType
        with open(url, "w") as fil:
            fil.write("class Blocks:\n")            
            for collection in bpy.data.collections:                
                self.writeCollection(fil, collection)              
            fil.close()

# Creates Addon
       
class MY_PT_PANEL(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "My panel"
    bl_idname = "MY_PT_PANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "My Addon"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        row.label(text="Snemand", icon= "GHOST_ENABLED")
        row = layout.row()
        row.operator(Snemand.bl_idname)

myClasses = [MY_PT_PANEL, Snemand]
 
def register():
    for cls in myClasses:
        bpy.utils.register_class(cls) 

def unregister():
    for cls in myClasses:
        bpy.utils.unregister_class(cls) 

if __name__ == "__main__":
    register()
