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

function Card:new(rank, suit)
	local card = {
		rank = rank,
		suit = suit,
	}
	setmetatable(card, Card)
	return card
end

function Card.filter(cards, targetSuit, targetRank)
	local filteredCards = {}
	for _, card in ipairs(cards) do
		if card.suit == targetSuit and card.rank == targetRank then
			table.insert(filteredCards, card)
		end
	end
	return filteredCards
end

function Card.inTable(cards, targetSuit, targetRank)
	for _, card in ipairs(cards) do
		if card.suit == targetSuit and card.rank == targetRank then
			return true
		end
	end
	return false
end

function Card.count(cards, targetSuit, targetRank)
	if not targetSuit and not targetRank then
		return #cards
	end

	local count = 0
	if targetSuit then
		for _, card in ipairs(cards) do
			if card.suit == targetSuit then
				count = count + 1
			end
		end
	elseif targetRank then
		for _, card in ipairs(cards) do
			if card.rank == targetRank then
				count = count + 1
			end
		end
	end
	return count
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

local Cards = {}
Cards.__index = Cards

function Cards:new(cards)
	local cardsObj = {
		cards = cards,
	}
	setmetatable(cardsObj, Cards)
	return cardsObj
end

function Cards:hasCards()
	return #self.cards > 0
end

function Cards:add(cards)
	for _, card in ipairs(cards) do
		table.insert(self.cards, card)
	end
end

function Cards:remove(index)
	return table.remove(self.cards, index)
end

function Cards:count(suit, rank)
	return Card.count(self.cards, suit, rank)
end

return {
	Suit = Suit,
	Rank = Rank,
	Card = Card,
	Cards = Cards,
}
