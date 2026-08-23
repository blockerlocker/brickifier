execute if entity @e[type=marker,tag=brickifier_node] run function zzz:brickifier/tick_active with storage brickifier:settings

execute unless entity @e[type=marker,tag=brickifier_node] if entity @e[type=marker,tag=brickifier_origin] run function zzz:brickifier/conversion_complete