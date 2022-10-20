TESTMAP = []

flr1 = """
S*_*Test_Spawn 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area
S*_*Test_Spawn 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area 0*_*North_Outside_Area
S*_*Test_Spawn 0*_*East_Outside_Area 0*_*East_Outside_Area U U U U 0*_*West_Outside_Area 0*_*West_Outside_Area
S*_*Test_Spawn 0*_*East_Outside_Area 0*_*East_Outside_Area U R*_*Test_Room R*_*Test_Room U 0*_*West_Outside_Area 0*_*West_Outside_Area
^*_*Test_Stairs 0*_*East_Outside_Area 0*_*East_Outside_Area U R*_*Test_Room R*_*Test_Room D 0*_*West_Outside_Area 0*_*West_Outside_Area
^*_*Test_Stairs 0*_*East_Outside_Area 0*_*East_Outside_Area U W W U 0*_*West_Outside_Area 0*_*West_Outside_Area
^*_*Test_Stairs 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area
^*_*Test_Stairs 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area 0*_*South_Outside_Area
"""

flr2 = """
0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof
0*_*Test_Roof 0f*_*Test_Roof 0f*_*Test_Roof 0f*_*Test_Roof 0f*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof
0*_*Test_Roof 0f*_*Test_Roof 0f*_*Test_Roof 0f*_*Test_Roof 0f*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof
0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof 0*_*Test_Roof
"""

TESTMAP.extend([flr1, flr2])
