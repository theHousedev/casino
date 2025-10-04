local cardModule = require("game.cards")
local Card = cardModule.Card
local Suit = cardModule.Suit
local Rank = cardModule.Rank

local Deck = {}
Deck.__index = Deck

function Deck:new()
	local deck = {
		cards = {},
	}
	setmetatable(deck, Deck)

	for suit = 1, 4 do
		for rank = 1, 13 do
			table.insert(deck.cards, Card:new(rank, suit))
		end
	end

	deck:shuffle()
	return deck
end

function Deck:shuffle() -- fisher-yates? possibly
	for i = #self.cards, 2, -1 do
		local j = math.random(i)
		self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
	end
end

function Deck:deal(target, count)
	count = count or 4

	for _ = 1, count do
		if #self.cards > 0 then
			table.insert(target, table.remove(self.cards))
		end
	end

	return target
end

function Deck:size()
	return #self.cards
end

return Deck
