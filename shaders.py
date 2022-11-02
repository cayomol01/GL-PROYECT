vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;


uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

out vec2 UVs;

void main()
{
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
    UVs = texcoords;
}
'''

fragment_shader ='''
#version 450 core
out vec4 fragColor;

in vec2 UVs;

uniform sampler2D tex;

void main()
{
    fragColor = texture(tex, UVs);
}
'''