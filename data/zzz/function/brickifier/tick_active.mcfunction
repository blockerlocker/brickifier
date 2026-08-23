$execute as @e[type=marker,tag=brickifier_node,limit=$(node_chain_limit)] at @s run function zzz:brickifier/convert_block/main with storage brickifier:settings

execute store result storage brickifier:temp all.node_count int 1 if entity @e[type=marker,tag=brickifier_node]

title @a actionbar [{player:blockerlocker},{text:" Brickifier Nodes: ",color:yellow},{storage:"brickifier:temp",nbt:"all.node_count",plain:true,color:aqua}]