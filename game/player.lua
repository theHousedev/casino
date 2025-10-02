local cardModule = require("game.card")
local Card = cardModule.Card
local Cards = cardModule.Cards
local Suit = cardModule.Suit
local Rank = cardModule.Rank
--[[================================================================
Player Class
  + hasCards: bool
  + play: Card
  + capture (none, adds to 'stack' table)
  + debugShowHand: string

================================================================--]]
-- TODO:
-- add name field? leans towards multiplayer, "login", etc
-- persistent score tracking long-term, stats, etc


local Player = {}
Player.__index = Player

function Player:new(index)
	local player = {
		index = index,
		hand = Cards.new({}),
		stack = Cards.new({}),
	}
	setmetatable(player, Player)

	return player
end

function Player:hasStack()
	return self.stack:hasCards()
end

function Player:hasHand()
	return self.hand:hasCards()
end

function Player:play(index)
	return self.hand:remove(index)
end

function Player:capture(cards)
	self.stack:add(cards)
end

function Player:hasBigCasino()
	bigCasino = Card.new(Rank.Ten, Suit.Diamond)
	return
end

function Player:hasLittleCasino()
	return self.stack:count(Rank.Two, Suit.Spade) >= 2
end

function Player:calcScore()
	local score = 0

	local cards = self.stack:count()
	local aces = self.stack:count(nil, Rank.Ace)
	local spades = self.stack:count(Suit.Spade, nil)

	local big = self:hasBigCasino()
	local little = self:hasLittleCasino()
end

function Player:reset()
	self.hand = Cards.new({})
	self.stack = Cards.new({})
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
