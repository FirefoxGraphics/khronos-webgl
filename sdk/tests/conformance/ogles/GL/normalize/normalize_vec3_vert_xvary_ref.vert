
/*
Copyright (c) 2019 The Khronos Group Inc.
Use of this source code is governed by an MIT-style license that can be
found in the LICENSE.txt file.
*/


attribute vec4 gtf_Color;
attribute vec4 gtf_Vertex;
uniform mat4 gtf_ModelViewProjectionMatrix;
varying vec4 color;

void main (void)
{
	vec4 tmp_Color = gtf_Color + vec4(0.25);
	color = vec4(tmp_Color.rgb / length(tmp_Color.rgb), 1.0);
	gl_Position = gtf_ModelViewProjectionMatrix * gtf_Vertex;
}
