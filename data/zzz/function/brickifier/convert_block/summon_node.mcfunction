execute if entity @n[type=marker,tag=brickifier_node,distance=..0.5] run return fail
execute positioned ~ ~-1 ~ if entity @n[type=marker,tag=brickifier_node,distance=..0.5] run return fail
$execute unless predicate {type:"minecraft:location_check",predicate:{position:{y:{min:$(origin_y)}}}} run return fail

execute if block ~ ~ ~ #brickifier:concrete_and_stairs run return fail
execute if block ~1 ~ ~ #brickifier:concrete_and_stairs run return fail
execute if block ~ ~ ~1 #brickifier:concrete_and_stairs run return fail
execute if block ~1 ~ ~1 #brickifier:concrete_and_stairs run return fail

execute if block ~ ~ ~ #brickifier:ignore if block ~1 ~ ~ #brickifier:ignore if block ~ ~ ~1 #brickifier:ignore if block ~1 ~ ~1 #brickifier:ignore run return fail

summon marker ~ ~ ~ {Tags:[brickifier_node]}