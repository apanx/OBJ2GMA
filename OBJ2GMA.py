import sys
import os

GMA_boilerplate = '2020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020200A20202020202020202020202020202020202020202020202020202020202020202020202020202020205F5F2020202020202020205F5F2D2D2D2D5F5F2020202020200A202020202020202020202020202020202020202020202020202020202020202020202020202020202F20205C5F5F2E2E2D2D272720602D5F5F2D5F5F27272D5F20200A20202020202020202020202020202020202020202020202020202020202020202020202020202028202F20205C2020202060602D2D2C2C2020602D2E2727272760200A2020202020202020202020202020202020202020202020202020202020202020202020202020207C207C202020602D2E2E5F5F20202E2C5C20202020602E202020200A202020202020202020202020202020202020202020202020205F5F5F20202020202020202020202820272E20205C205F5F5F5F605C2029602D5F20202020602E20200A2020202020202020202020202020202020205F5F5F20202028202020602E202020202020202020275C2020205F5F2F2020205F5F5C27202F20603A2D2E2E5F205C200A202020202020202020202020202020202028202020602D2E20602E202020602E202020202020202E7C5C5F2020282020202F202E2D7C207C272E7C202020206060270A202020202020202020202020202020202020602D2E202020602D2E602E202020602E20202020207C272028202C275C2028202857577C205C57296A202020202020200A202020202020202020202E2E2D2D2D272727273A2D2D2D20202020602E5C2020205F5C2020202E7C7C2020272C20205C5F5C5F602F20202060602D2E2020202020200A20202020202020202C272020202020202E2760202E275F602D2C2020206020202820207C20207C27272E202020602E20202020202020205C5F5F2F202020202020200A202020202020202F2020205F20202E2720203A27202820606060202020205F5F205C20205C207C2020205C202E5F3A372C5F5F5F5F5F5F2E2D2720202020202020200A2020202020207C202E2D272F20203A202E2720202E2D602D2E5F202020282020602E5C202027273A202020602D5C202020202F2020202020202020202020202020200A202020202020276020202F20203A27203A202E3A202E2D27273E602D2E20602D2E20602020207C20272E202020207C202028202020202020202020202020202020200A2020202020202020202D20202E27203A27203A202F2020202F205F2820605F3A20605F3A2E20602E2020603B2E20205C20205C2020202020202020202020202020200A2020202020202020207C20207C202E27203A202F7C20207C20285F5F5F28202020282020202020205C202020295C20203B20207C20202020202020202020202020200A20202020202020202E27202E27207C207C207C20602E207C2020205C5C5C602D2D2D3A2E5F5F2D272729202F2020292F2020207C20202020202020202020202020200A20202020202020207C20207C20207C207C207C20207C207C2020202F2F2F20202020202020202020207C2F20202027202020207C20202020202020202020202020200A202020202020202E27202E272020272E272E603B207C2F205C20202F20202020202F202020202020202020202020205C5F5F2F2020202020202020202020202020200A202020202020207C20207C202020207C207C207C2E7C2020207C2020202020202F2D2C5F5F5F5F5F5F5F5C202020202020205C2020202020202020202020202020200A2020202020202F20202F20292020207C207C20277C27205F2F2020202020202F20202020207C202020207C5C202020202020205C20202020202020202020202020200A202020202E3A2E2D27202E2720202E27207C202020292F202020202020202F20202020207C20202020207C20602D2D2C202020205C202020202020202020202020200A2020202020202020202F202020207C20207C20202F207C2020202020207C2020202020207C20202020207C2020202F202020202020292020202020202020202020200A202020202E5F5F2E27202020202F6020203A7C2F5F2F7C2020202020207C2020202020207C2020202020207C2028202020202020207C2020202020202020202020200A20202020602D2E5F5F5F2E2D603B20202F20272020207C2020202020207C2020202020207C2020202020207C20205C2020202020207C2020202020202020202020200A20202020202020202020202E3A5F2D272020202020207C202020202020205C20202020207C202020202020205C2020602E5F5F5F2F202020202020202020202020200A20202020202020202020202020202020202020202020205C5F5F5F5F5F5F5F2920202020205C5F5F5F5F5F5F5F2920202020202020202020202020202020202020200A'

def tab(file, num):
    for i in range(num):
        file.write("\t")

def main(argv):
    if len(argv) > 1:
        filename = argv[1]

    else:
        from Tkinter import Tk
        from tkFileDialog import askopenfilename
        
        Tk().withdraw()
        filename = askopenfilename(filetypes=[('OBJ-model', '*.obj'), ('All files', '*.*')])
        if filename =='':
            sys.exit(0)

    OBJ_file = open(filename, 'r')
    OBJ_data = OBJ_file.readlines()
    OBJ_file.close

    vertices = []
    normals = []
    tverts = []
    group = {}

    current_group = ''
    current_face = 1

    GMA_file = open(os.path.splitext(filename)[0] + ".gma", "w")

    for line in OBJ_data:
        if line.startswith('#'): continue
        if line.startswith('g '):
            current_group = line[2:-1]
            if group.has_key(current_group):
                print 'WARNING - Duplicate object name {}'.format(current_group)
            group[current_group] = []
            continue
        values = line.split()
        if not values: continue
        elif values[0] == 'v':
            vertices.append(map(float, values[1:4]))
        elif values[0] == 'vn':
            normals.append(map(float, values[1:4]))
        elif values[0] == 'vt':
            tverts.append(map(float, values[1:4]))

        elif values[0] == 'f':
            vert = []
            texcoords = []
            norms = []
            facenormal = []
            for v in values[1:]:
                w = v.split('/')
                vert.append(int(w[0]))
                if len(w) >= 2 and len(w[1]) > 0:
                    texcoords.append(int(w[1]))
                else:
                    texcoords.append(0)
                if len(w) >= 3 and len(w[2]) > 0:
                    norms.append(int(w[2]))
                else:
                    norms.append(0)

            facenormal_x = 0
            facenormal_y = 0
            facenormal_z = 0 

            for v in norms:
                facenormal_x += normals[v-1][0]
                facenormal_y += normals[v-1][1]
                facenormal_z += normals[v-1][2]
            facenormal = [facenormal_x / 3, facenormal_y /3, facenormal_z / 3]
            group[current_group].append((vert, norms, texcoords, facenormal))
    print "OBJ loading complete"
    GMA_file.write(GMA_boilerplate.decode('hex'))
    for object in group:
        meshNumFaces = len(group[object])
        vertex_list = []
        map(vertex_list.extend, [x[0] for x in group[object]])
        vertex_list = list(set(vertex_list))
        vertex_list.sort()

        meshNumVerts = len(vertex_list)
        find_OBJ_Vindex = dict(zip(vertex_list, range(meshNumVerts)))

        texcoord_list = []
        map(texcoord_list.extend, [x[2] for x in group[object]])
        texcoord_list = list(set(texcoord_list))
        texcoord_list.sort()

        meshNumTVerts = len(texcoord_list)
        if min(texcoord_list) == 0:
            meshNumTVerts = 0
        else:
            find_OBJ_texcoord_index = dict(zip(texcoord_list, range(meshNumTVerts)))

        GMA_file.write("%s\n" % "*GEOMOBJECT")
        GMA_file.write("%s\n" % "{")
        tab(GMA_file, 1); GMA_file.write("%s\n" % "*NODE_NAME\t{}".format(object))
        print "Creating GEOMOBJECT " + object
        tab(GMA_file, 1); GMA_file.write("%s\n" % "*NODE_SHADEVERTS\t0")
        tab(GMA_file, 1); GMA_file.write("%s\n" % "*NODE_TM")
        tab(GMA_file, 1); GMA_file.write("%s\n" % "{")
        tab(GMA_file, 2); GMA_file.write("%s\n" % ("*NODE_NAME\t" + object))
        tab(GMA_file, 2); GMA_file.write("%s\n" % ("*TM_ROW0 1.000000	0.000000	0.000000"))
        tab(GMA_file, 2); GMA_file.write("%s\n" % ("*TM_ROW1 0.000000	1.000000	0.000000"))
        tab(GMA_file, 2); GMA_file.write("%s\n" % ("*TM_ROW2 0.000000	0.000000	1.000000"))
        tab(GMA_file, 2); GMA_file.write("%s\n" % ("*TM_ROW3 0.000000	0.000000	0.000000"))
        tab(GMA_file, 1); GMA_file.write("%s\n" % "}")

        tab(GMA_file, 1); GMA_file.write("%s\n" % "*MESH")
        tab(GMA_file, 1); GMA_file.write("%s\n" % "{")

        tab(GMA_file, 2); GMA_file.write("%s\n" % "*TIMEVALUE\t0")
        tab(GMA_file, 2); GMA_file.write("%s\n" % "*MESH_NUMVERTEX\t{}".format(meshNumVerts))
        tab(GMA_file, 2); GMA_file.write("%s\n" % "*MESH_NUMFACES\t{}".format(meshNumFaces))

        tab(GMA_file, 2); GMA_file.write("%s\n" % "*MESH_VERTEX_LIST")
        tab(GMA_file, 2); GMA_file.write("%s\n" % "{")

        for i in range(meshNumVerts):
            x = vertices[vertex_list[i] - 1][0] 
            y = vertices[vertex_list[i] - 1][1]
            z = vertices[vertex_list[i] - 1][2]
            tab(GMA_file, 3); GMA_file.write("%s\n" % "*MESH_VERTEX\t{}\t{:f}\t{:f}\t{:f}".format(i, x, y, z))

        tab(GMA_file, 2); GMA_file.write("%s\n" % "}")
        tab(GMA_file, 2); GMA_file.write("%s\n" % "*MESH_FACE_LIST")
        tab(GMA_file, 2); GMA_file.write("%s\n" % "{")
            
        for i in range(meshNumFaces):
            mx = find_OBJ_Vindex[group[object][i][0][2]]
            my = find_OBJ_Vindex[group[object][i][0][1]]
            mz = find_OBJ_Vindex[group[object][i][0][0]]
            tab(GMA_file, 3); GMA_file.write("%s\n" % "*MESH_FACE\t{}\tA:\t{}\tB:\t{}\tC:\t{}\t*MESH_MTLID 0".format(i, mx, my, mz))

        tab(GMA_file, 2); GMA_file.write("%s\n" % "}")
            
        if (meshNumTVerts > 0):
            tab(GMA_file, 2); GMA_file.write("%s\n" % "*MESH_NUMTVERTEX\t{}".format(meshNumTVerts))
            tab(GMA_file, 2); GMA_file.write("%s\n" % "*MESH_TVERTLIST")
            tab(GMA_file, 2); GMA_file.write("%s\n" % "{")
            for i in range(meshNumTVerts):
                x = tverts[texcoord_list[i] - 1][0] 
                y = tverts[texcoord_list[i] - 1][1]
                if len(tverts[texcoord_list[i] - 1]) > 2:
                    z = tverts[texcoord_list[i] - 1][2]
                else:
                    z = 0
                tab(GMA_file, 3); GMA_file.write("%s\n" % "*MESH_TVERT\t{}\t{:f}\t{:f}\t{:f}".format(i, x, y, z))
                    
            tab(GMA_file, 2); GMA_file.write("%s\n" % "}")
            tab(GMA_file, 2); GMA_file.write("%s\n" % "*MESH_NUMTVFACES\t{}".format(meshNumFaces))
            tab(GMA_file, 2); GMA_file.write("%s\n" % "*MESH_TFACELIST")
            tab(GMA_file, 2); GMA_file.write("%s\n" % "{")

            for i in range(meshNumFaces):
                mx = find_OBJ_texcoord_index[group[object][i][2][2]]
                my = find_OBJ_texcoord_index[group[object][i][2][1]]
                mz = find_OBJ_texcoord_index[group[object][i][2][0]]
                tab(GMA_file, 3); GMA_file.write("%s\n" % "*MESH_TFACE\t{}\t{}\t{}\t{}".format(i, mx, my, mz))
                    
            tab(GMA_file, 2); GMA_file.write("%s\n" % "}")

        tab(GMA_file, 2); GMA_file.write("%s\n" % "*MESH_NORMALS")
        tab(GMA_file, 2); GMA_file.write("%s\n" % "{")
        for i in range(meshNumFaces):
            x = group[object][i][3][0]
            y = group[object][i][3][1]
            z = group[object][i][3][2]
            tab(GMA_file, 3); GMA_file.write("%s\n" % "*MESH_FACENORMAL\t{}\t{:f}\t{:f}\t{:f}".format(i, x, y, z))
            for j in range(2,-1,-1):
                f = find_OBJ_Vindex[group[object][i][0][j]]
                x = normals[group[object][i][1][j] - 1][0] 
                y = normals[group[object][i][1][j] - 1][1]
                z = normals[group[object][i][1][j] - 1][2]

                tab(GMA_file, 4); GMA_file.write("%s\n" % "*MESH_VERTEXNORMAL\t{}\t{:f}\t{:f}\t{:f}".format(f, x, y, z))
        tab(GMA_file, 2); GMA_file.write("%s\n" % "}")
        tab(GMA_file, 2); GMA_file.write("%s\n" % "*BACKFACE_CULL\t1")
        tab(GMA_file, 2); GMA_file.write("%s\n" % "*MATERIAL_REF\t0")

        tab(GMA_file, 1); GMA_file.write("%s\n" % "}")
        GMA_file.write("%s\n" % "}")
    GMA_file.close
    print "Conversion complete"
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)