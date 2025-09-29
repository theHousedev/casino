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
