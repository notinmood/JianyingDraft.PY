precision highp float;
varying vec2 uv0;

uniform sampler2D inputImageTexture;
uniform sampler2D _MainTex;

uniform int baseTexWidth;
uniform int baseTexHeight;
uniform vec2 fullBlendTexSize;

uniform float alphaFactor;

#define BLEND_MODE blendNormal      //定义叠加模式
#define BLEND(base,blend,blendFun) blendFun(base,blend)

// normal
vec3 blendNormal(vec3 base,vec3 blend){
    return blend;
}

vec3 blendNormal(vec3 base,vec3 blend,float opacity){
    return(blendNormal(base,blend)*opacity+blend*(1.-opacity));
}
// add
float blendAdd(float base,float blend){
    return min(base+blend,1.);
}

vec3 blendAdd(vec3 base,vec3 blend){
    return min(base+blend,vec3(1.));
}

// average
vec3 blendAverage(vec3 base,vec3 blend){
    return(base+blend)/2.;
}

// color burn
float blendColorBurn(float base,float blend){
    return(blend==0.)?blend:max((1.-((1.-base)/blend)),0.);
}

vec3 blendColorBurn(vec3 base,vec3 blend){
    return vec3(blendColorBurn(base.r,blend.r),blendColorBurn(base.g,blend.g),blendColorBurn(base.b,blend.b));
}

//color dodge
float blendColorDodge(float base,float blend){
    return(blend==1.)?blend:min(base/(1.-blend),1.);
}

vec3 blendColorDodge(vec3 base,vec3 blend){
    return vec3(blendColorDodge(base.r,blend.r),blendColorDodge(base.g,blend.g),blendColorDodge(base.b,blend.b));
}

// darken
float blendDarken(float base,float blend){
    return min(blend,base);
}

vec3 blendDarken(vec3 base,vec3 blend){
    return vec3(blendDarken(base.r,blend.r),blendDarken(base.g,blend.g),blendDarken(base.b,blend.b));
}

// difference
vec3 blendDifference(vec3 base,vec3 blend){
    return abs(base-blend);
}

// exclusion
vec3 blendExclusion(vec3 base,vec3 blend){
    return base+blend-2.*base*blend;
}

// reflect
float blendReflect(float base,float blend){
    return(blend==1.)?blend:min(base*base/(1.-blend),1.);
}

vec3 blendReflect(vec3 base,vec3 blend){
    return vec3(blendReflect(base.r,blend.r),blendReflect(base.g,blend.g),blendReflect(base.b,blend.b));
}

// glow
vec3 blendGlow(vec3 base,vec3 blend){
    return blendReflect(blend,base);
}

// hard light
float blendHardLight(float base,float blend){
    return base<.5?(2.*base*blend):(1.-2.*(1.-base)*(1.-blend));
}

vec3 blendHardLight(vec3 base,vec3 blend){
    return vec3(blendHardLight(base.r,blend.r),blendHardLight(base.g,blend.g),blendHardLight(base.b,blend.b));
}

// hard mix
float blendHardMix(float base,float blend){
    if(blend<.5){
        float vividLight=blendColorBurn(base,(2.*blend));
        return(vividLight<.5)?0.:1.;
    }else{
        float vividLight=blendColorDodge(base,(2.*(blend-.5)));
        return(vividLight<.5)?0.:1.;
    }
}

vec3 blendHardMix(vec3 base,vec3 blend){
    return vec3(blendHardMix(base.r,blend.r),blendHardMix(base.g,blend.g),blendHardMix(base.b,blend.b));
}

// lighten
float blendLighten(float base,float blend){
    return max(blend,base);
}

vec3 blendLighten(vec3 base,vec3 blend){
    return vec3(blendLighten(base.r,blend.r),blendLighten(base.g,blend.g),blendLighten(base.b,blend.b));
}

// linear burn
float blendLinearBurn(float base,float blend){
    return max(base+blend-1.,0.);
}

vec3 blendLinearBurn(vec3 base,vec3 blend){
    return max(base+blend-vec3(1.),vec3(0.));
}

// linear dodge
float blendLinearDodge(float base,float blend){
    return min(base+blend,1.);
}

vec3 blendLinearDodge(vec3 base,vec3 blend){
    return min(base+blend,vec3(1.));
}

// linear light
float blendLinearLight(float base,float blend){
    return blend<.5?blendLinearBurn(base,(2.*blend)):blendLinearDodge(base,(2.*(blend-.5)));
}

vec3 blendLinearLight(vec3 base,vec3 blend){
    return vec3(blendLinearLight(base.r,blend.r),blendLinearLight(base.g,blend.g),blendLinearLight(base.b,blend.b));
}

// multiply
vec3 blendMultiply(vec3 base,vec3 blend){
    return base*blend;
}

// negation
vec3 blendNegation(vec3 base,vec3 blend){
    return vec3(1.)-abs(vec3(1.)-base-blend);
}

// overlay
float blendOverlay(float base,float blend){
    return base<.5?(2.*base*blend):(1.-2.*(1.-base)*(1.-blend));
}

vec3 blendOverlay(vec3 base,vec3 blend){
    return vec3(blendOverlay(base.r,blend.r),blendOverlay(base.g,blend.g),blendOverlay(base.b,blend.b));
}

// phoenix
vec3 blendPhoenix(vec3 base,vec3 blend){
    return min(base,blend)-max(base,blend)+vec3(1.);
}

// pin light
float blendPinLight(float base,float blend){
    return(blend<.5)?blendDarken(base,(2.*blend)):blendLighten(base,(2.*(blend-.5)));
}

vec3 blendPinLight(vec3 base,vec3 blend){
    return vec3(blendPinLight(base.r,blend.r),blendPinLight(base.g,blend.g),blendPinLight(base.b,blend.b));
}

// screen
float blendScreen(float base,float blend){
    return 1.-((1.-base)*(1.-blend));
}

vec3 blendScreen(vec3 base,vec3 blend){
    return vec3(blendScreen(base.r,blend.r),blendScreen(base.g,blend.g),blendScreen(base.b,blend.b));
}

// soft light
float blendSoftLight(float base,float blend){
    return(blend<.5)?(2.*base*blend+base*base*(1.-2.*blend)):(sqrt(base)*(2.*blend-1.)+2.*base*(1.-blend));
}

vec3 blendSoftLight(vec3 base,vec3 blend){
    return vec3(blendSoftLight(base.r,blend.r),blendSoftLight(base.g,blend.g),blendSoftLight(base.b,blend.b));
}

// substract
float blendSubstract(float base,float blend){
    return max(base+blend-1.,0.);
}

vec3 blendSubstract(vec3 base,vec3 blend){
    return max(base+blend-vec3(1.),vec3(0.));
}

// vivid light
float blendVividLight(float base,float blend){
    return(blend<.5)?blendColorBurn(base,(2.*blend)):blendColorDodge(base,(2.*(blend-.5)));
}

vec3 blendVividLight(vec3 base,vec3 blend){
    return vec3(blendVividLight(base.r,blend.r),blendVividLight(base.g,blend.g),blendVividLight(base.b,blend.b));
}

// snow color
vec3 RGBToHSL(vec3 color){
    vec3 hsl;
    float fmin=min(min(color.r,color.g),color.b);
    float fmax=max(max(color.r,color.g),color.b);
    float delta=fmax-fmin;
    
    hsl.z=(fmax+fmin)/2.;
    
    if(delta==0.)
    {
        hsl.x=0.;
        hsl.y=0.;
    }
    else
    {
        if(hsl.z<.5)
        hsl.y=delta/(fmax+fmin);
        else
        hsl.y=delta/(2.-fmax-fmin);
        
        float deltaR=(((fmax-color.r)/6.)+(delta/2.))/delta;
        float deltaG=(((fmax-color.g)/6.)+(delta/2.))/delta;
        float deltaB=(((fmax-color.b)/6.)+(delta/2.))/delta;
        
        if(color.r==fmax)
        hsl.x=deltaB-deltaG;
        else if(color.g==fmax)
        hsl.x=(1./3.)+deltaR-deltaB;
        else if(color.b==fmax)
        hsl.x=(2./3.)+deltaG-deltaR;
        
        if(hsl.x<0.)
        hsl.x+=1.;
        else if(hsl.x>1.)
        hsl.x-=1.;
    }
    
    return hsl;
}

float HueToRGB(float f1,float f2,float hue){
    if(hue<0.)
    hue+=1.;
    else if(hue>1.)
    hue-=1.;
    float res;
    if((6.*hue)<1.)
    res=f1+(f2-f1)*6.*hue;
    else if((2.*hue)<1.)
    res=f2;
    else if((3.*hue)<2.)
    res=f1+(f2-f1)*((2./3.)-hue)*6.;
    else
    res=f1;
    return res;
}

vec3 HSLToRGB(vec3 hsl){
    vec3 rgb;
    
    if(hsl.y==0.)
    rgb=vec3(hsl.z);
    else
    {
        float f2;
        
        if(hsl.z<.5)
        f2=hsl.z*(1.+hsl.y);
        else
        f2=(hsl.z+hsl.y)-(hsl.y*hsl.z);
        
        float f1=2.*hsl.z-f2;
        
        rgb.r=HueToRGB(f1,f2,hsl.x+(1./3.));
        rgb.g=HueToRGB(f1,f2,hsl.x);
        rgb.b=HueToRGB(f1,f2,hsl.x-(1./3.));
    }
    
    return rgb;
}

vec3 blendSnowColor(vec3 blend,vec3 bgColor){
    vec3 blendHSL=RGBToHSL(blend);
    vec3 hsl=RGBToHSL(bgColor);
    return HSLToRGB(vec3(blendHSL.r,blendHSL.g,hsl.b));
}

// snow hue
vec3 blendSnowHue(vec3 blend,vec3 bgColor){
    vec3 baseHSL=RGBToHSL(bgColor.rgb);
    return HSLToRGB(vec3(RGBToHSL(blend.rgb).r,baseHSL.g,baseHSL.b));
}

vec3 blendFunc(vec3 base,vec3 blend,float opacity)  //opacity 素材的不透明度
{
    vec3 resultColor=BLEND(base,blend,BLEND_MODE);//叠加模式替换
    resultColor=mix(base,resultColor,opacity);
    return resultColor;
}

vec4 lm_inverse_premult(vec4 color)
{
    vec4 resultColor=vec4(clamp(color.rgb/color.a,0.,1.),color.a);
    return resultColor;
}

vec2 sucaiAlign(vec2 videoUV,vec2 videoSize,vec2 sucaiSize,vec2 anchorImageCoord,float sucaiScale)
{
    vec2 videoImageCoord=videoUV*videoSize;
    vec2 sucaiUV=(videoImageCoord-anchorImageCoord)/(sucaiSize*sucaiScale)+vec2(.5);
    return sucaiUV;
}

vec4 blendColor(sampler2D sucai,vec4 baseColor,vec2 videoSize,vec2 sucaiSize,vec2 anchorImageCoord,float sucaiScale)
{
    lowp vec4 resultColor=baseColor;
    lowp vec4 sucaiColor=baseColor;
    vec2 sucaiUV=sucaiAlign(uv0,videoSize,sucaiSize,anchorImageCoord,sucaiScale);
    if(all(lessThan(vec2(0.),sucaiUV))&&all((lessThan(sucaiUV,vec2(1.)))))
    {
        sucaiUV.y = 1.0-sucaiUV.y;  //amazing-engine素材上下flip
        sucaiColor=texture2D(sucai,sucaiUV);
        //sucaiColor.a*=alphaFactor;
        sucaiColor=lm_inverse_premult(sucaiColor);
        resultColor=vec4(blendFunc(baseColor.rgb,sucaiColor.rgb,sucaiColor.a),1.);
        resultColor=mix(baseColor,resultColor,alphaFactor);
    }
    return resultColor;
}

void main(void)
{
    vec2 baseTextureSize=vec2(baseTexWidth,baseTexHeight);
    vec2 fullBlendAnchor=baseTextureSize*.5;
    float scale=1.;
    
    //外居中对齐
    float baseAspectRatio=baseTextureSize.y/baseTextureSize.x;
    float blendAspectRatio=fullBlendTexSize.y/fullBlendTexSize.x;
    if(baseAspectRatio>=blendAspectRatio){
        scale=baseTextureSize.y/fullBlendTexSize.y;
    }else{
        scale=baseTextureSize.x/fullBlendTexSize.x;
    }
    
    lowp vec4 baseColor=texture2D(inputImageTexture,uv0);
    lowp vec4 resultColor=blendColor(_MainTex,baseColor,baseTextureSize,fullBlendTexSize,
    fullBlendAnchor,scale);
    
    gl_FragColor=resultColor;
}
