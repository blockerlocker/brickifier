$fill ~ ~ ~ ~1 ~ ~1 $(color)_concrete strict

playsound minecraft:block.deepslate_bricks.place block @a ~ ~ ~ 5 1.5

execute positioned ~2 ~ ~ run function zzz:brickifier/convert_block/summon_node with storage brickifier:temp all
execute positioned ~ ~ ~2 run function zzz:brickifier/convert_block/summon_node with storage brickifier:temp all
execute positioned ~-2 ~ ~ run function zzz:brickifier/convert_block/summon_node with storage brickifier:temp all
execute positioned ~ ~ ~-2 run function zzz:brickifier/convert_block/summon_node with storage brickifier:temp all
execute positioned ~ ~-1 ~ run function zzz:brickifier/convert_block/summon_node with storage brickifier:temp all

execute positioned ~ ~1 ~ unless block ~ ~ ~ #brickifier:ignore run return run function zzz:brickifier/convert_block/main with storage brickifier:settings
execute positioned ~ ~1 ~ unless block ~1 ~ ~ #brickifier:ignore run return run function zzz:brickifier/convert_block/main with storage brickifier:settings
execute positioned ~ ~1 ~ unless block ~ ~ ~1 #brickifier:ignore run return run function zzz:brickifier/convert_block/main with storage brickifier:settings
execute positioned ~ ~1 ~ unless block ~1 ~ ~1 #brickifier:ignore run return run function zzz:brickifier/convert_block/main with storage brickifier:settings

$execute positioned ~ ~1 ~ unless block ~ ~ ~ water unless block ~ ~ ~ #brickifier:concrete_and_stairs run setblock ~ ~ ~ $(color)_concrete_stairs[facing=south,shape=outer_left] strict
$execute positioned ~1 ~1 ~1 unless block ~ ~ ~ water unless block ~ ~ ~ #brickifier:concrete_and_stairs run setblock ~ ~ ~ $(color)_concrete_stairs[facing=north,shape=outer_left] strict
$execute positioned ~ ~1 ~1 unless block ~ ~ ~ water unless block ~ ~ ~ #brickifier:concrete_and_stairs run setblock ~ ~ ~ $(color)_concrete_stairs[facing=east,shape=outer_left] strict
$execute positioned ~1 ~1 ~ unless block ~ ~ ~ water unless block ~ ~ ~ #brickifier:concrete_and_stairs run setblock ~ ~ ~ $(color)_concrete_stairs[facing=west,shape=outer_left] strict

$execute positioned ~ ~1 ~ if block ~ ~ ~ water run setblock ~ ~ ~ $(color)_concrete_stairs[facing=south,shape=outer_left,waterlogged=true] strict
$execute positioned ~1 ~1 ~1 if block ~ ~ ~ water run setblock ~ ~ ~ $(color)_concrete_stairs[facing=north,shape=outer_left,waterlogged=true] strict
$execute positioned ~ ~1 ~1 if block ~ ~ ~ water run setblock ~ ~ ~ $(color)_concrete_stairs[facing=east,shape=outer_left,waterlogged=true] strict
$execute positioned ~1 ~1 ~ if block ~ ~ ~ water run setblock ~ ~ ~ $(color)_concrete_stairs[facing=west,shape=outer_left,waterlogged=true] strict
