import numpy as np

def calculate_distance(atom1,atom2):
    #两个原子之间的距离
    return np.linalg.norm(atom1-atom2)

def calculate_angle(atom1,atom2,atom3):
    #三个原子形成的键角
    vector1=atom1-atom2
    vector2=atom3-atom2
    dot_product=np.dot(vector1,vector2)
    norm_product=np.linalg.norm(vector1)*np.linalg.norm(vector2)
    angle=np.arccos(dot_product/norm_product)
    return np.degrees(angle)

def calculate_dihedral_angle(atom1,atom2,atom3,atom4):
    #四个原子形成的二面角
    b1=atom2-atom1
    b2=atom3-atom2
    b3=atom4-atom3
    b1xb2=np.cross(b1,b2)
    b2xb3=np.cross(b2,b3)
    b1xb2_x_b2xb3=np.cross(b1xb2,b2xb3)

    angle=np.arctan2(np.dot(b1xb2_x_b2xb3,b2)/np.linalg.norm(b2),np.dot(b1xb2,b2xb3))
    return np.degrees(angle)


atom1=np.array([0.0, 0.0, 0.0])
atom2=np.array([1.0, 0.0, 0.0])
atom3=np.array([1.0, 1.0, 0.0])
atom4=np.array([0.0, 1.0, 1.0])

distance=calculate_distance(atom1,atom2)
angle=calculate_angle(atom1,atom2,atom3)
dihedral_angle=calculate_dihedral_angle(atom1,atom2,atom3,atom4)

print(distance)
print(angle)
print(dihedral_angle)
