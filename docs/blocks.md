| Block Name                                 | Sprite or Stage | Method Name                   | Method Type |
|--------------------------------------------|-----------------|-------------------------------|-------------|
| move (steps) steps                         | Sprite          | move_steps                    | Function    |
| turn right (degrees) degrees               | Sprite          | turn_degrees_right            | Function    |
| turn left (degrees) degrees                | Sprite          | turn_degrees_left             | Function    |
| go to (movement target)                    | Sprite          | goto_target                   | Function    |
| go to x: (x) y: (y)                        | Sprite          | goto                          | Function    |
| glide (seconds) secs to (movement target)  | Sprite          | glide_to_target               | Function    |
| glide (seconds) secs to x: (x) y: (y)      | Sprite          | glide                         | Function    |
| point in direction (direction)             | Sprite          | point                         | Function    |
| point towards (movement target)            | Sprite          | point_towards_target          | Function    |
| change x by (x)                            | Sprite          | change_x                      | Function    |
| set x to (x)                               | Sprite          | set_x                         | Function    |
| change y by (y)                            | Sprite          | change_y                      | Function    |
| set y to (y)                               | Sprite          | set_y                         | Function    |
| if on edge, bounce                         | Sprite          | if_on_edge_bounce             | Function    |
| set rotation style [rotation style]        | Sprite          | set_rotation_style            | Function    |
| (x position)                               | Sprite          | get_x                         | Function    |
| (y position)                               | Sprite          | get_y                         | Function    |
| (direction)                                | Sprite          | get_direction                 | Function    |
| say (message) for (seconds) seconds        | Sprite          | say                           | Function    |
| say (message)                              | Sprite          | say                           | Function    |
| think (message) for (seconds) seconds      | Sprite          | think                         | Function    |
| think (message)                            | Sprite          | think                         | Function    |
| switch costume to (costume)                | Sprite          | set_costume                   | Function    |
| next costume                               | Sprite          | next_costume                  | Function    |
| switch backdrop to (backdrop)              | Both            | switch_backdrop               | Function    |
| next backdrop                              | Both            | next_backdrop                 | Function    |
| change size by (size increase)             | Sprite          | change_size                   | Function    |
| set size to (size)%                        | Sprite          | set_size                      | Function    |
| change [effect] effect by (increase)       | Both            | change_effect                 | Function    |
| set [effect] effect to (number)            | Both            | set_effect                    | Function    |
| clear graphic effects                      | Both            | clear_effects                 | Function    |
| show                                       | Sprite          | show                          | Function    |
| hide                                       | Sprite          | hide                          | Function    |
| go to front layer                          | Sprite          | goto_front                    | Function    |
| go to back layer                           | Sprite          | goto_back                     | Function    |
| go [forward] (number) layers               | Sprite          | go_forward_layers             | Function    |
| go [backward] (number) layers              | Sprite          | go_backward_layers            | Function    |
| (costume [number])                         | Sprite          | get_costume_number            | Function    |
| (costume [name])                           | Sprite          | get_costume_name              | Function    |
| (backdrop [number])                        | Sprite          | get_backdrop_number           | Function    |
| (backdrop [name])                          | Sprite          | get_backdrop_name             | Function    |
| (size)                                     | Sprite          | get_size                      | Function    |
| play sound [sound] until done              | Both            | play_until_done               | Function    |
| start sound [sound]                        | Both            | start_sound                   | Function    |
| stop all sounds                            | Both            | stop_all_sounds               | Function    |
| change [sound effect] effect by (number)   | Both            | change_sound_effect           | Function    |
| set [sound effect] effect to (number)      | Both            | set_sound_effect              | Function    |
| clear sound effects                        | Both            | clear_sound_effects           | Function    |
| change volume by (percentage)              | Both            | change_volume                 | Function    |
| set volume to (volume)                     | Both            | set_volume                    | Function    |
| (volume)                                   | Both            | get_volume                    | Function    |
| when green flag clicked                    | Both            | when_started                  | Decorator   |
| when [key] key pressed                     | Both            | when_key_pressed              | Decorator   |
| when this sprite clicked                   | Both            | when_this_sprite_clicked      | Decorator   |
| when stage clicked                         | Both            | when_stage_clicked            | Decorator   |
| when backdrop switches to [backdrop]       | Both            | when_backdrop_switches        | Decorator   |
| when [loudness] > (number)                 | Both            | when_loudness_is_over         | Decorator   |
| when [timer] > (number)                    | Both            | when_timer_is_over            | Decorator   |
| broadcast [message]                        | Both            | broadcast                     | Function    |
| broadcast [message] and wait               | Both            | broadcast_and_wait            | Function    |
| wait (seconds) seconds                     | Both            | wait                          | Function    |
| repeat (times)                             | Both            | for i in range(times):        | Built-in    |
| forever                                    | Both            | while True:                   | Built-in    |
| if <condition> then                        | Both            | if condition:                 | Built-in    |
| if <condition> then else                   | Both            | if condition: else:           | Built-in    |
| wait until <condition>                     | Both            | wait_until                    | Function    |
| repeat until <condition>                   | Both            | while not condition:          | Function    |
| stop [all]                                 | Both            | stop_all                      | Function    |
| stop [this script]                         | Both            | stop_this_script              | Function    |
| stop [other scripts in sprite]             | Both            | stop_other_scripts            | Function    |
| when I start as a clone                    | Sprite          | when_cloned                   | Decorator   |
| create clone of [cloning target]           | Both            | create_clone                  | Function    |
| delete this clone                          | Sprite          | delete_this_clone             | Function    |
| <touching [collision target]?>             | Sprite          | is_touching                   | Function    |
| <touching color [color]?>                  | Sprite          | is_touching_color             | Function    |
| <color [color 1] is touching [color 2]?>   | Sprite          | is_color_touching_color       | Function    |
| (distance to [collision target])           | Sprite          | distance_to                   | Function    |
| ask (question) and wait                    | Both            | ask                           | Function    |
| (answer)                                   | Both            | get_answer                    | Function    |
| <key [key] pressed?>                       | Both            | is_key_pressed                | Function    |
| <mouse down?>                              | Both            | is_mouse_down                 | Function    |
| (mouse x)                                  | Both            | get_mouse_x                   | Function    |
| (mouse y)                                  | Both            | get_mouse_y                   | Function    |
| set drag mode [draggable \| not draggable] | Both            | set_draggable (true \| false) | Function    |
| (loudness)                                 | Both            | get_loudness                  | Function    |
| (timer)                                    | Both            | get_timer                     | Function    |
| reset timer                                | Both            | reset_timer                   | Function    |
| ([attribute or variable] of [sprite])      | Both            | get_attribute_of (str, str)   | Function    |
| (current [year])                           | Both            | get_year                      | Function    |
| (current [month])                          | Both            | get_month                     | Function    |
| (current [date])                           | Both            | get_date                      | Function    |
| (current [day of week])                    | Both            | get_day_of_week               | Function    |
| (current [hour])                           | Both            | get_hour                      | Function    |
| (current [minute])                         | Both            | get_minute                    | Function    |
| (current [second])                         | Both            | get_second                    | Function    |
| <online?>                                  | Both            | is_online                     | Function    |
| (username)                                 | Both            | get_username                  | Function    |
| pick random (num) to (num)                 | Both            | get_random                    | Function    |
| show variable (variable)                   | Both            | show_variable                 | Function    |
| hide variable (variable)                   | Both            | hide variable                 | Function    |