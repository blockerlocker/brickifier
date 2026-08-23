execute as @a at @s run playsound minecraft:block.vault.eject_item ui @s ~ ~ ~
tellraw @a ["  ",{text:"< ",color:yellow},{player:blockerlocker},{text:" > Brickifier complete",color:yellow}]
kill @e[type=marker,tag=brickifier_origin]