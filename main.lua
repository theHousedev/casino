---@diagnostic disable: undefined-global

local Deck = require("game.deck")
local Player = require("game.player")
local CardUI = require("ui.cardui")

local game = {
	deck = nil,
	player = nil,
	table = {},
}

local cardUIs = {}
local selectedCard = nil

function love.load()
	game.deck = Deck:new()
	game.player = Player:new(1)

	local hand = {}
	game.deck:deal(hand, 4)
	game.player.hand = hand

	cardUIs = {}
	local startX = 100
	local startY = love.graphics.getHeight() - 100
	for i, card in ipairs(game.player.hand) do
		local cardUI = CardUI:new(startX + (i-1) * 70, startY, card)
		table.insert(cardUIs, cardUI)
	end

	print("Game loaded. Deck size:", game.deck:size())
	print("Player hand:", game.player:debugShowHand())
end

function love.update(dt)
	local mx, my = love.mouse.getPosition()

	for _, cardUI in ipairs(cardUIs) do
		cardUI:updateHover(mx, my)
	end

	if draggedCard then
		draggedCard:drag(mx, my)
	end
end

function love.draw()
	love.graphics.setColor(0.2, 0.6, 0.2)
	love.graphics.rectangle("fill", 0, 0, love.graphics.getWidth(), love.graphics.getHeight())

	love.graphics.setColor(1, 1, 1)
	love.graphics.print("Casino Card Game", 10, 10)
	love.graphics.print("Deck: " .. game.deck:size() .. " cards", 10, 30)
	love.graphics.print("Press SPACE to deal a card", 10, 80)

	for _, cardUI in ipairs(cardUIs) do
		cardUI:draw()
	end
end

function love.keypressed(key)
	if key == "space" then
		local newCard = {}
		game.deck:deal(newCard, 1)
		if #newCard > 0 then
			table.insert(game.player.hand, newCard[1])
			local cardUI = CardUI:new(100 + (#cardUIs) * 70, love.graphics.getHeight() - 100, newCard[1])
			table.insert(cardUIs, cardUI)
			print("Dealt card. New hand:", game.player:debugShowHand())
		else
			print("Deck is empty!")
		end
	elseif key == "escape" then
		love.event.quit()
	end
end

function love.mousepressed(x, y, button)
	if button == 1 then
		for i = #cardUIs, 1, -1 do
			local cardUI = cardUIs[i]
			if cardUI:containsPoint(x, y) then
				cardUI:startDrag(x, y)
				draggedCard = cardUI
				break
			end
		end
	end
end

function love.mousereleased(x, y, button)
	if button == 1 and draggedCard then
		draggedCard:stopDrag()
		draggedCard = nil
	end
end
