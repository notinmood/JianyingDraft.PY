--@input float curTime = 0.0{"widget":"slider","min":0,"max":1}

local exports = exports or {}
local SeekModeScript = SeekModeScript or {}
SeekModeScript.__index = SeekModeScript
 
function SeekModeScript.new(construct, ...)
    local self = setmetatable({}, SeekModeScript)
    if construct and SeekModeScript.constructor then SeekModeScript.constructor(self, ...) end
    self.startTime = 0.0
    self.endTime = 3.0
    self.curTime = 0.0
    self.width = 0
    self.height = 0
    return self
end

function SeekModeScript:constructor()

end

function SeekModeScript:onUpdate(comp, detalTime)
    --测试用
    --local props = comp.entity:getComponent("ScriptComponent").properties
    --if props:has("curTime") then
        --self:seekToTime(comp, props:get("curTime"))
    --end
    --实际用
    self:seekToTime(comp, self.curTime - self.startTime)
end

function SeekModeScript:onStart(comp)
    self.EASpeed = 1.0
    self.animSeqCom = comp.entity:getComponent("AnimSeqComponent")
    self.material = comp.entity:getComponent("Sprite2DRenderer").material
end

function SeekModeScript:seekToTime(comp, time)

    self.animSeqCom:seekToTime(time * self.EASpeed)

    local w = Amaz.BuiltinObject:getInputTextureWidth()
    local h = Amaz.BuiltinObject:getInputTextureHeight()
    if w ~= self.width or h ~= self.height then
        self.width = w
        self.height = h
        self.material:setInt("baseTexWidth", self.width)
        self.material:setInt("baseTexHeight", self.height)
    end
end





function SeekModeScript:onEvent(sys, event)
    --speed【0，0.5，1】【0.5，1，1.5】
    if "effects_adjust_speed" == event.args:get(0) then
        local intensity = event.args:get(1)
        self.EASpeed = 1.5*intensity+0.5
    end
    if "effects_adjust_background_animation" == event.args:get(0) then
        local intensity = event.args:get(1)
        self.material:setFloat("alphaFactor", intensity) 
    end
end










exports.SeekModeScript = SeekModeScript
return exports
