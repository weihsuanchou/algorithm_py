def traversal(self, node):
    output = []
    stack = [node]
    while stack:
        cur = stack.pop()
        if cur is None:
            continue
        if type(cur) is int:
            #take current val
            output.append(cur)
        else:
            #it is a node, need to look further from left > m > right, so put left node into stack at last
            stack.append(cur.right)
            stack.append(cur.val)
            stack.append(cur.left)

    return output


