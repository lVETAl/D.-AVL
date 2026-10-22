class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.h = 1


def h(v):
    return v.h if v else 0


def upd(v):
    v.h = 1 + max(h(v.left), h(v.right))


def bal(v):
    return h(v.right) - h(v.left)


def rot_left(a):
    b = a.right
    a.right, b.left = b.left, a
    upd(a); upd(b)
    return b


def rot_right(a):
    b = a.left
    a.left, b.right = b.right, a
    upd(a); upd(b)
    return b


def balance(v):
    upd(v)
    if bal(v) == 2:
        if bal(v.right) < 0:
            v.right = rot_right(v.right)
        return rot_left(v)
    if bal(v) == -2:
        if bal(v.left) > 0:
            v.left = rot_left(v.left)
        return rot_right(v)
    return v


def add(v, x):
    if v is None:
        return Node(x)
    if x < v.key:
        v.left = add(v.left, x)
    elif x > v.key:
        v.right = add(v.right, x)
    return balance(v)


def delete(v, x):
    if v is None:
        return None
    if x < v.key:
        v.left = delete(v.left, x)
    elif x > v.key:
        v.right = delete(v.right, x)
    elif v.left is None or v.right is None:
        return v.left or v.right
    else:
        m = v.right
        while m.left:
            m = m.left
        v.key = m.key
        v.right = delete(v.right, m.key)
    return balance(v)


def exists(v, x):
    while v and v.key != x:
        v = v.left if x < v.key else v.right
    return v is not None


def next_key(v, x):
    res = None
    while v:
        if v.key >= x:
            res, v = v.key, v.left
        else:
            v = v.right
    return res


def prev_key(v, x):
    res = None
    while v:
        if v.key <= x:
            res, v = v.key, v.right
        else:
            v = v.left
    return res


def preorder(v):
    out, st = [], [v]
    while st:
        v = st.pop()
        out.append(v.key)
        st += [c for c in (v.right, v.left) if c]
    return out


root, out = None, []
for _ in range(int(input())):
    cmd, *arg = input().split()
    x = int(arg[0]) if arg else None
    if cmd == "add":
        root = add(root, x)
    elif cmd == "del":
        root = delete(root, x)
    elif cmd == "exists":
        out.append("YES" if exists(root, x) else "NO")
    elif cmd == "next":
        out.append(str(next_key(root, x)))
    elif cmd == "prev":
        out.append(str(prev_key(root, x)))
    elif cmd == "root":
        out.append(str(root.key) if root else "Empty")
    elif cmd == "height":
        out.append(str(h(root)))
    elif cmd == "print":
        out.append(" ".join(map(str, preorder(root))) if root else "Empty")
print("\n".join(out))
