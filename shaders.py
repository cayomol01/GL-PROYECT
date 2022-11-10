vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals, 1.0)).xyz;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);

}
'''

fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));

    fragColor = texture(tex, UVs) * intensity;
}
'''

toon_vertex_shader ='''
layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals, 1.0)).xyz;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);

}

'''


toon_fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
	float intensity = dot(norms, normalize(pointLight - pos));

    if (intensity > 0.95)
		fragColor = vec4(1.0,0.5,0.5,1.0);
	else if (intensity > 0.5)
		fragColor = vec4(0.6,0.3,0.3,1.0);
	else if (intensity > 0.25)
		fragColor = vec4(0.4,0.2,0.2,1.0);
	else
		fragColor = vec4(0.2,0.1,0.1,1.0);

}'''


glow_vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals, 1.0)).xyz;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);

}
'''

glow_fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;
uniform vec3 camArr;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    float glowAmount = 1 - dot(norms, camArr);
    vec4 color = vec4(0.0,0,1.0,1.0);
    if (glowAmount<=0)
        glowAmount = 0;
        
        
    color = color* glowAmount;
    

    fragColor = texture(tex, UVs) * intensity + color;
    
}
'''


r_glow_vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals, 1.0)).xyz;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);

}
'''

r_glow_fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;
uniform vec3 camArr;
uniform float time;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    float glowAmount = 1 - dot(norms, camArr);
    vec4 color = vec4(sin(time),cos(time),0,0.5);
    if (glowAmount<=0)
        glowAmount = 0;
        
        
    color = color* glowAmount;
    

    fragColor = texture(tex, UVs) * intensity + (color*0.3);
    
}
'''


toon_r_glow_vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals, 1.0)).xyz;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);

}
'''

toon_r_glow_fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;
uniform vec3 camArr;
uniform float time;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    float glowAmount = 1 - dot(norms, camArr);
    vec4 color = vec4(0,0,0,1.0);
    if (glowAmount<=0)
        glowAmount = 0;
        
    if (intensity > 0.95)
		color = vec4(1.0*sin(time),1*cos(time),1*tan(time),1.0);
	else if (intensity > 0.5)
		color = vec4(0.8*sin(time),0.8*cos(time),0.8*tan(time),1.0);
	else if (intensity > 0.25)
		color = vec4(0.6*sin(time),0.6*cos(time),0.6*tan(time),1.0);
	else
		color = vec4(0.4*sin(time),0.4*cos(time),0.4*tan(time),1.0);

        
    color = color* glowAmount;
    

    fragColor = texture(tex, UVs) * intensity + (color*0.3);
    
}
'''