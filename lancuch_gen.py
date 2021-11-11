import functools

E = ["A", "B", "C", "D", "E", "F"]
N = 2

# E = ["A", "B"]
# N = 2


def variations(n: int): #generowanie Ek
    _Z=[]
    _v_rec("", n, _Z)
    return _Z

def _v_rec(_s: str, _n: int, _Z_ref: list):
    if _n==0:
        return _Z_ref.append(_s)
    else:
        for e in E:
            _v_rec(_s+e, _n-1, _Z_ref)




class Joint: #kolumna baza-łączące
    def __init__(self, base: str, conns: list):
        self.base = base
        self.conns = conns

    def getMerges(self):
        shift=1
        merges=[]

        while True:
            for conn in self.conns:
                if self.base[shift:] == conn[:-shift+len(self.base)]:
                    merges.append(conn)
            if len(merges) > 0:
                break
            shift += 1
        
        return (merges, shift)
    
    @staticmethod
    def merge(a: str, b: str, bshift: int):
        return a + b[len(a)-bshift:]



def shift_merge(vars: list):
    merged = []

    joints = [Joint(vars[0], vars[1:])]
    # joints.append(Joint(vars[0], vars[1:]))

    while len(joints):
        joint = joints[0]
        merges, bshift = joint.getMerges()
        for merge in merges:
            newConns = joint.conns[:]
            newConns.remove(merge)
            newJoint = Joint(Joint.merge(joint.base, merge, bshift), newConns)

            if len(newJoint.conns) == 0:
                merged.append(newJoint.base)
            else:
                joints.append(newJoint)
        joints.remove(joint)
    return merged


vars = variations(N)
merged = shift_merge(vars)
print(functools.reduce(lambda x, y: x if len(x) < len(y) else y, merged)) #zwraca najmniejszy ciąg