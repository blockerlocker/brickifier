$execute as @e[type=marker,tag=brickifier_node,limit=$(node_chain_limit)] at @s run function zzz:brickifier/convert_block/main with storage brickifier:settings

execute store result storage brickifier:temp all.node_count int 1 if entity @e[type=marker,tag=brickifier_node]

title @a actionbar [{text:"Number of Nodes: "},{storage:"brickifier:temp",nbt:"all.node_count"}]