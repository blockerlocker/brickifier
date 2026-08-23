Made for Minecraft 26.3

Lets you convert an area into a toy building block style, made using concrete and concrete stairs. When the command is run, it works until it has converted all connected blocks within a certain radius (more info below.)

| Command | Description |
| --- | --- |
| `/function brickifier:start` | Begin converting blocks, starting at the first block directly below the player. |
| `/function brickifier:stop` | Stop the conversion process early. |
| `/function brickifier:settings` | Adjust settings. |

## Settings
- Node Chain Limit
    - The number of nodes that can place bricks every tick. Defaults to 32.
- Node Distance Limit
    - The maximum distance that nodes can spawn from the starting point (where the start command was triggered). Defaults to 32.
- Node Depth Limit
    - The number of blocks beneath the starting point that nodes have to stay above. Defaults to 8.

## How was this made?
This data pack uses the `color_tags` module from [my data pack library bldp](https://github.com/blockerlocker/bldp), which sorts every block in the game into the 16 Minecraft block color categories. Honestly the sorting isn't perfect and the module needs some improvement, but it works fine enough for now.