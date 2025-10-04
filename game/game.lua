local Deck = require("game.deck")
local Player = require("game.player")

local Game = {}
Game.__index = Game

function Game:new()
	local game = {
		deck = nil,
		players = {},
		table = {},
		currentPlayer = 1,
		round = 1,
		gameOver = false,
	}
	setmetatable(game, Game)

	return game
end

function Game:initialize(numPlayers)
	numPlayers = numPlayers or 2

	self.deck = Deck:new()

	for i = 1, numPlayers do
		self.players[i] = Player:new(i)
	end

	for _, player in ipairs(self.players) do
		local hand = {}
		self.deck:deal(hand, 4)
		player.hand = hand
	end

	local tableCards = {}
	self.deck:deal(tableCards, 4)
	self.table = tableCards

	self.currentPlayer = 1
	self.gameOver = false
end

function Game:nextTurn()
	self.currentPlayer = self.currentPlayer + 1
	if self.currentPlayer > #self.players then
		self.currentPlayer = 1
	end
end

function Game:playCard(playerIndex, cardIndex)
	local player = self.players[playerIndex]
	if not player or cardIndex < 1 or cardIndex > #player.hand then
		return false, "Invalid card selection"
	end

	local card = player:play(cardIndex)
	table.insert(self.table, card)

	return true, "Card played:" .. card
end

function Game:addToTable(cards)
	for _, card in ipairs(cards) do
		table.insert(self.table, card)
	end
end

function Game:clearTable()
	self.table = {}
end

function Game:calculateScores()
	local scores = {}
	-- TODO:
	-- 1) more complex scoring; add player card counts and spade
	-- counts to a table then do a comparison (works for 2-4)
	-- 2) find distributed aces and add to each player's indexed score

	-- for now, simple player-held scores
	for i, player in ipairs(self.players) do
		scores[i] = player:calcScore()
	end
	return scores
end

function Game:isGameOver()
	return self.gameOver
end

function Game:reset()
	for _, player in ipairs(self.players) do
		player:reset()
	end
	self.table = {}
	self.currentPlayer = 1
	self.gameOver = false
end

return Game
