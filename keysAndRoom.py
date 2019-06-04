
def key_and_room(rooms):
    # get i to generate room nomber row 0 = 0, row 1 = 1 ...
    non_vis = set([i for i in range(1, len(rooms))])

    def helper(room_no):
        for key in rooms[room_no]:
            if key in non_vis:
                non_vis.remove(key)
                #go to the target room, which I have the key
                helper(key)
    helper(0)

    return len(non_vis) == 0