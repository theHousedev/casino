local cardModule = require("game.cards")
local Card = cardModule.Card
local Cards = cardModule.Cards
local Suit = cardModule.Suit
local Rank = cardModule.Rank
local Player = {}
Player.__index = Player

function Player:new(index)
	local player = {
		index = index,
		hand = {},
		stack = Cards.new({}),
	}
	setmetatable(player, Player)

	return player
end

function Player:hasStack()
	return self.stack:hasCards()
end

function Player:hasHand()
	return #self.hand > 0
end

function Player:play(index)
	return table.remove(self.hand, index)
end

function Player:capture(cards)
	self.stack:add(cards)
end

function Player:hasBigCasino()
	return self.stack:hasCards(Card.new(Rank.Ten, Suit.Diamond))
end

function Player:hasLittleCasino()
	return self.stack:hasCards(Card.new(Rank.Two, Suit.Spade))
end

function Player:calcScore()
	local score = 0

	-- determine stack size
	local cards = self.stack:count()
	if cards > 26 then
		score = score + 3
	end

	-- NOTE: score aces
	local aces = self.stack:count(nil, Rank.Ace)
	if aces ~= nil then
		score = score + aces
	end

	-- NOTE: score spades
	local spades = self.stack:count(Suit.Spade, nil)
	if spades ~= nil then
		-- TODO: check spades val > othPlayers:spades()
		score = score + spades
	end

	-- NOTE: scoring big/little casino
	if self:hasBigCasino() then
		score = score + 2
	end

	if self:hasLittleCasino() then
		score = score + 1
	end

	return score
end

function Player:reset()
	self.hand = {}
	self.stack = Cards.new({})
	self.isActive = false
end

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

return Player
