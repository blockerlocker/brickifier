import os, sys, urllib.request, json, math
from pathlib import Path


if len(sys.argv) > 1:
    MCVERSION = sys.argv[1]
else:
#### SET MINECRAFT VERSION MANUALLY HERE ####
    MCVERSION = "26.3-snapshot-9"


os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not Path.cwd().name == "data":
    print("Working directory not named 'data'! bldp generation scripts must be stored within the 'data' folder of your pack to generate correctly!")
    input("Press Enter to exit program...")
    sys.exit()

if not Path("bldp.py").is_file():
    with open("bldp.py", "w", encoding="utf-8") as bldp_main:
        bldp_main.write(urllib.request.urlopen("https://raw.githubusercontent.com/blockerlocker/bldp/main/data/bldp.py").read().decode('utf-8'))

import bldp

TEMP_DIR = "temp_bldp"

bldp.remove_path(TEMP_DIR)
bldp.remove_path("bldp/tags/block/color")

bldp.unpack_client(MCVERSION,TEMP_DIR,("assets/minecraft/blockstates","assets/minecraft/models/block","assets/minecraft/textures"))

override_map = {
    "grass_block": "green",
    "short_grass": "lime",
    "tall_grass": "lime",
    "fern": "lime",
    "large_fern": "lime",
    "lily_pad": "green",
    "vine": "green",
    "oak_leaves": "lime",
    "birch_leaves": "lime",
    "acacia_leaves": "lime",
    "spruce_leaves": "green",
    "dark_oak_leaves": "green",
    "cherry_leaves": "pink",
    "dirt": "brown",
    "dirt_path": "yellow",
    "rooted_dirt": "brown",
    "firefly_bush": "yellow",
    "wildflowers": "yellow",
    "birch_button": "white",
    "birch_fence": "white",
    "birch_fence_gate": "white",
    "birch_planks": "white",
    "birch_pressure_plate": "white",
    "birch_sign": "white",
    "birch_slab": "white",
    "birch_stairs": "white",
    "birch_wall_sign": "white",
    "birch_hanging_sign": "white",
    "birch_sapling": "lime",
    "birch_shelf": "white",
    "birch_wall_hanging_sign": "white",
    "oak_button": "yellow",
    "oak_fence": "yellow",
    "oak_fence_gate": "yellow",
    "oak_planks": "yellow",
    "oak_pressure_plate": "yellow",
    "oak_sign": "yellow",
    "oak_slab": "yellow",
    "oak_stairs": "yellow",
    "oak_wall_sign": "yellow",
    "oak_hanging_sign": "yellow",
    "oak_sapling": "lime",
    "oak_shelf": "yellow",
    "oak_wall_hanging_sign": "yellow",
    "oak_log": "brown",
    "oak_wood": "brown",
    "cherry_button": "pink",
    "cherry_fence": "pink",
    "cherry_fence_gate": "pink",
    "cherry_planks": "pink",
    "cherry_pressure_plate": "pink",
    "cherry_sign": "pink",
    "cherry_slab": "pink",
    "cherry_stairs": "pink",
    "cherry_wall_sign": "pink",
    "cherry_hanging_sign": "pink",
    "cherry_sapling": "pink",
    "cherry_shelf": "pink",
    "cherry_wall_hanging_sign": "pink",
    "pink_petals": "pink",
    "cherry_log": "purple",
    "cherry_wood": "purple",
    "pale_oak_log": "gray",
    "pale_oak_wood": "gray",
    "leaf_litter": "brown",
    "ice": "light_blue",
    "packed_ice": "light_blue",
    "blue_ice": "light_blue",
    "seagrass": "lime",
    "tall_seagrass": "lime",
    "water": "blue"
}

print("--Getting average colors of concrete blocks")
color_map = {
    "black": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/black_concrete.png"),
    "blue": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/blue_concrete.png"),
    "brown": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/brown_concrete.png"),
    "cyan": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/cyan_concrete.png"),
    "gray": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/gray_concrete.png"),
    "green": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/green_concrete.png"),
    "light_blue": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/light_blue_concrete.png"),
    "light_gray": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/light_gray_concrete.png"),
    "lime": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/lime_concrete.png"),
    "magenta": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/magenta_concrete.png"),
    "orange": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/orange_concrete.png"),
    "pink": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/pink_concrete.png"),
    "purple": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/purple_concrete.png"),
    "red": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/red_concrete.png"),
    "white": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/white_concrete.png"),
    "yellow": bldp.average_color(f"{TEMP_DIR}/assets/minecraft/textures/block/yellow_concrete.png")
}

print("--Sorting blocks by color")
block_dict = {}
blockstate_dir = f"{TEMP_DIR}/assets/minecraft/blockstates/"
for file in os.listdir(blockstate_dir):

    block_id = file.replace(".json","")

    if block_id in override_map:
        if not override_map[block_id] in block_dict:
            block_dict[override_map[block_id]] = []
        block_dict[override_map[block_id]].append(block_id)
    elif not block_id in ["item_frame", "glow_item_frame", "air"]:
        with open(f"{blockstate_dir}/{file}", "r") as blockstate_json:
            blockstate_raw = json.load(blockstate_json)

        model_paths = []

        def append_if_new(array,new_path):
            if not new_path in array:
                array.append(new_path)

        if "variants" in blockstate_raw:
            for key in blockstate_raw["variants"]:
                if "model" in blockstate_raw["variants"][key]:
                    append_if_new(model_paths,blockstate_raw["variants"][key]["model"])
                else:
                    for random_variant in blockstate_raw["variants"][key]:
                        append_if_new(model_paths,random_variant["model"])
                
        elif "multipart" in blockstate_raw:
            for part in blockstate_raw["multipart"]:
                if "model" in part["apply"]:
                    append_if_new(model_paths,part["apply"]["model"])
                else:
                    for application in part["apply"]:
                        append_if_new(model_paths,application["model"])

        texture_paths = []

        for model_path in model_paths:
            if model_path[0:10] == "minecraft:":
                model_path = model_path[10:]
            actual_model_path = f"{TEMP_DIR}/assets/minecraft/models/{model_path}.json"
            with open (actual_model_path, "r") as model_json:
                model_raw = json.load(model_json)

            if "textures" in model_raw:
                for key in model_raw["textures"]:
                    if "sprite" in model_raw["textures"][key]:
                        append_if_new(texture_paths,model_raw["textures"][key]["sprite"])
                    else:
                        append_if_new(texture_paths,model_raw["textures"][key])

        if len(texture_paths) > 0:
            total_r = 0
            total_g = 0
            total_b = 0

            for texture_path in texture_paths:
                if texture_path[0:10] == "minecraft:":
                    texture_path = texture_path[10:]
                if texture_path != "missingno" and texture_path[0:1] != "#":
                    actual_texture_path = f"{TEMP_DIR}/assets/minecraft/textures/{texture_path}.png"
                    add_r, add_g, add_b = bldp.average_color(actual_texture_path)

                    total_r += add_r
                    total_g += add_g
                    total_b += add_b

            total_r /= len(texture_paths)
            total_g /= len(texture_paths)
            total_b /= len(texture_paths)

            block_avg = (total_r,total_g,total_b)

            closest_color = min(color_map, key=lambda color: math.dist(block_avg,color_map[color]))

            if not closest_color in block_dict:
                block_dict[closest_color] = []
            block_dict[closest_color].append(block_id)

for color in block_dict:
    bldp.json_to_file({"values":block_dict[color]},"bldp/tags/block/color",color)

bldp.remove_path(TEMP_DIR)