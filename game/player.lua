local cardModule = require("game.card")
local Card = cardModule.Card
local Suit = cardModule.Suit
local Rank = cardModule.Rank
--[[

=================================================================
Player Class
  + hasCards: bool
  + play: Card
  + capture (none, adds to 'stack' table)
  + debugShowHand: string

=================================================================
TODO:
  + add name field? leans towards multiplayer, "login", etc
  + persistent score tracking long-term, stats, etc

--]]

local Player = {}
Player.__index = Player

function Player:new(index)
	local player = {
		index = index,
		hand = {},
		stack = {},
	}
	setmetatable(player, Player)

	return player
end

function Player:hasCards()
	return #self.hand > 0
end

function Player:play(index)
	return table.remove(self.hand, index)
end

function Player:capture(cards)
	table.insert(self.stack, cards)
end

function Player:countAces()
	-- TODO: rank + suit filter helper func?
	-- could be reused for capture/stack logic
end

function Player:countCards()
	return #self.stack
end

function Player:countSpades()
	local spadeCount = 0

	for _, card in ipairs(self.stack) do
		if card.Suit == Suit.Spade then
			spadeCount = spadeCount + 1
		end
	end

	return spadeCount
end

function Player:calcScore()
	local score = 0

	local aces = self:countAces()
	local cards = self:countCards()
	local spades = self:countSpades()
	local big = self:hasBigCasino()
	local little = self:hasLittleCasino()
end

function Player:reset()
	self.hand = {}
	self.stack = {}
	self.isActive = false
end

-- for log/debug purposes
function Player:debugShowHand()
	local handStr = ""

	for i, card in ipairs(self.hand) do
		handStr = handStr .. tostring(card)
		if i < #self.hand then
			handStr = handStr .. " "
		end
	end

	return handStr
end
