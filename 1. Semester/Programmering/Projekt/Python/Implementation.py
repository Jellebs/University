# Implementation document
from bpy.types import Operator, Panel
import bpy

# Grundet at filen ikke køres fra min modul placering, er det nødvendigt at gøre et alternativ forsøg på at finde blocks filen.
from sys import path # For at tilføje mit modul, måtte jeg tilføje dens placering til python.
if "/Users/JesperBertelsen/Desktop/Crazy/Uni/Programmering/Projekt/Python/Data" not in path:
    path.append("/Users/JesperBertelsen/Desktop/Crazy/Uni/Programmering/Projekt/Python/Data")
    print(path)
from Blocks import *

class Snemand(Operator): 
    """Tooltip"""
    bl_idname = "object.snemand_operator"
    bl_label = "Lav en snemand"
    index: int = None
    
    def execute(self,context):
        self.bygKrop() # - This is used to build the snowmand with the gathered data. 
        print("Snemand er kaldt")   
        return {'FINISHED'}
                
    def placerBlocks(self, kollektion, størrelse, navn):
        new = True 
        i = 0
        for block in kollektion: 
            x = block["x"] 
            y = block["y"]
            z = block["z"]
            bpy.ops.mesh.primitive_cube_add(size=størrelse, location=(x,y,z))
            i += 1
            if new == True: 
                bpy.ops.object.move_to_collection(collection_index=0, is_new=True, new_collection_name=navn)
                new = False
                if self.index == None: # En måde at undgå mutable defaults
                    self.index = 2
                else: 
                    self.index += 1
            else: 
                bpy.ops.object.move_to_collection(collection_index=self.index)
        print(i) 
        
    def bygKrop(self): 
        self.placerBlocks(Blocks.Body_Big_blocks, 2, "Body - Big blocks")
        self.placerBlocks(Blocks.Body_Small_blocks, 1, "Body - Small blocks")
        self.placerBlocks(Blocks.Hat_Big_blocks, 2, "Hat - Small blocks")
        self.placerBlocks(Blocks.Hat_Small_blocks, 1, "Hat - Small blocks")
        self.placerBlocks(Blocks.Carrot_Big_blocks, 2, "Carrot - Big blocks") 
        self.placerBlocks(Blocks.Carrot_Small_blocks, 1, "Carrot - Small blocks") 
        self.placerBlocks(Blocks.Eyes, 1, "Eyes")  
        

# Creates Addon  
class MY_PT_PANEL(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Jespers Panel"
    bl_idname = "MY_PT_PANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Mit Addon"

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
