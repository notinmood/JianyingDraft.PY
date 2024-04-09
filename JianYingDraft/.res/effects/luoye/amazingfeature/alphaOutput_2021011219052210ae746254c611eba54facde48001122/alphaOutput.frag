precision lowp float;
varying highp vec2 uv0;
uniform sampler2D u_InputTex;
uniform sampler2D u_OutputTex;
void main()
{
    gl_FragColor = vec4(texture2D(u_OutputTex, uv0).rgb, texture2D(u_InputTex, uv0).a);
    //gl_FragColor = vec4(1.0);
}
