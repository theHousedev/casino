local Suit = {
	Spade = 1,
	Heart = 2,
	Club = 3,
	Diamond = 4,
}

local Rank = {
	Ace = 1,
	Two = 2,
	Three = 3,
	Four = 4,
	Five = 5,
	Six = 6,
	Seven = 7,
	Eight = 8,
	Nine = 9,
	Ten = 10,
	Jack = 11,
	Queen = 12,
	King = 13,
}

local Card = {}
Card.__index = Card

function Card:new(suit, rank)
	local card = {
		suit = suit,
		rank = rank,
	}
	setmetatable(card, Card)
	return card
end

function Card.filter(cards, targetSuit, targetRank)
	-- TODO: write filter func for card utilities
end

function Card:__tostring()
	local rankSymbols = {
		[1] = "A",
		[2] = "2",
		[3] = "3",
		[4] = "4",
		[5] = "5",
		[6] = "6",
		[7] = "7",
		[8] = "8",
		[9] = "9",
		[10] = "10",
		[11] = "J",
		[12] = "Q",
		[13] = "K",
	}

	local suitSymbols = {
		[1] = "♠",
		[2] = "♥",
		[3] = "♣",
		[4] = "♦",
	}

	return rankSymbols[self.rank] .. suitSymbols[self.suit]
end

return {
	Suit = Suit,
	Rank = Rank,
	Card = Card,
}
