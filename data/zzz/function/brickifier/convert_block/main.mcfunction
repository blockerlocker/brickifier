execute if entity @s[type=marker,tag=brickifier_node] run kill @s

$execute at @n[type=marker,tag=brickifier_origin] if entity @s[type=marker,tag=brickifier_node,distance=$(node_distance_limit)..] run return fail

execute if block ~ ~ ~ #concrete run return fail

data remove storage brickifier:temp all.color

execute positioned ~1 ~ ~1 run function zzz:brickifier/convert_block/check_color
execute positioned ~ ~ ~1 run function zzz:brickifier/convert_block/check_color
execute positioned ~1 ~ ~ run function zzz:brickifier/convert_block/check_color
function zzz:brickifier/convert_block/check_color

function zzz:brickifier/convert_block/place_brick with storage brickifier:temp all