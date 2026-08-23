execute if entity @e[type=marker,tag=brickifier_origin] run return run function zzz:brickifier/conversion_active

execute unless block ~ ~ ~ #brickifier:all positioned ~ ~-1 ~ run return run function brickifier:start
execute if block ~ ~ ~ #brickifier:ignore positioned ~ ~-1 ~ run return run function brickifier:start

execute as @a at @s run playsound minecraft:block.vault.eject_item ui @s ~ ~ ~
tellraw @a ["  ",{text:"< ",color:yellow},{player:blockerlocker},{text:" > Brickifier started",color:yellow}]

gamerule random_tick_speed 0

execute align xyz summon marker run function zzz:brickifier/start/half_xz

data modify storage brickifier:temp all.x_decimal set string storage brickifier:temp all.half_x -2 -1
data modify storage brickifier:temp all.z_decimal set string storage brickifier:temp all.half_z -2 -1

function zzz:brickifier/start/summon_origin with storage brickifier:settings

data modify storage brickifier:temp all.origin_y set from entity @n[type=marker,tag=brickifier_origin] Pos[1]

execute align xyz if data storage brickifier:temp all{x_decimal:"0",z_decimal:"0"} run return run function zzz:brickifier/convert_block/main with storage brickifier:settings
execute align xyz if data storage brickifier:temp all{x_decimal:"5",z_decimal:"0"} positioned ~-1 ~ ~ run return run function zzz:brickifier/convert_block/main with storage brickifier:settings
execute align xyz if data storage brickifier:temp all{x_decimal:"0",z_decimal:"5"} positioned ~ ~ ~-1 run return run function zzz:brickifier/convert_block/main with storage brickifier:settings
execute align xyz if data storage brickifier:temp all{x_decimal:"5",z_decimal:"5"} positioned ~-1 ~ ~-1 run return run function zzz:brickifier/convert_block/main with storage brickifier:settings