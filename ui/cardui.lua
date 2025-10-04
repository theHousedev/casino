---@diagnostic disable: undefined-global

local CardUI = {}
CardUI.__index = CardUI

function CardUI:new(x, y, card)
	local cardUI = {
		x = x,
		y = y,
		card = card,
		width = 60,
		height = 84,
		dragging = false,
		dragOffsetX = 0,
		dragOffsetY = 0,
		hovered = false,
	}
	setmetatable(cardUI, CardUI)
	return cardUI
end

function CardUI:containsPoint(mx, my)
	return mx >= self.x and mx <= self.x + self.width and my >= self.y and my <= self.y + self.height
end

function CardUI:draw()
	local r, g, b = 1, 1, 1
	if self.hovered or self.dragging then
		r, g, b = 0.9, 0.9, 1
	end

	love.graphics.setColor(r, g, b)
	love.graphics.rectangle("fill", self.x, self.y, self.width, self.height)

	love.graphics.setColor(0, 0, 0)
	love.graphics.rectangle("line", self.x, self.y, self.width, self.height)

	love.graphics.setColor(0, 0, 0)
	love.graphics.printf(tostring(self.card), self.x + 5, self.y + 5, self.width - 10, "center")
end

function CardUI:updateHover(mx, my)
	self.hovered = self:containsPoint(mx, my)
end

function CardUI:startDrag(mx, my)
	if self.hovered then
		self.dragging = true
		self.dragOffsetX = mx - self.x
		self.dragOffsetY = my - self.y
	end
end

function CardUI:drag(mx, my)
	if self.dragging then
		self.x = mx - self.dragOffsetX
		self.y = my - self.dragOffsetY
	end
end

function CardUI:stopDrag()
	self.dragging = false
end

return CardUI
