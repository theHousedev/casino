# Casino Game Development Plan
This will largely be LLM-supplied code review and plan guidance to help me track things that need to be addressed or developed further. I will contribute some to this myself, which I may use to interface with a given model to try and get productive feedback within the doc. It will be hopefully a useful location for ideas but may not exactly align with my own plan - just inform it to some degree. Information below is not authoritative re: the project direction or coding goals.

## Current Status: C+ Architecture
**Files:** `models.py`, `core.py`, `main.py`, `unit_test.py`

---

## IMMEDIATE FIXES (High Priority)
*Target: Get to B+ before adding new features*

### 1. Fix Dual State Tracking Bug 🔥
**Problem:** Both `self.activePlayer` and `self.playerIndex` track the same thing
**Fix:** Remove `self.activePlayer`, use `getActivePlayer()` method only
```python
# Remove: self.activePlayer = ...
# Use: player = self.getActivePlayer()
```

### 2. Clean Up Type Hints
**Problem:** `# type: ignore` indicates design issues
**Fix:** Proper typing without ignores
```python
def getActivePlayer(self) -> Player:
    return self.players[self.playerIndex]
```

### 3. Add Constants
**Problem:** Magic numbers everywhere
**Fix:** 
```python
CARDS_PER_HAND = 4
INITIAL_TABLE_CARDS = 4
```

### 4. Fix Deck Interface Inconsistency
**Problem:** `deal()` method does too many things
**Fix:** Single responsibility
```python
def deal_card(self) -> Card:  # Only returns
def deal_to_hand(self, target: list[Card], count: int):  # Only adds
```

---

## ARCHITECTURE IMPROVEMENTS (Medium Priority)

### 5. Extract Display Logic
**Move from `core.py` to `display.py`:**
- `showTable()`
- `showPlayer()`
- All print statements

### 6. Remove Dead Code
**Delete unused features:**
- `Player.active` boolean
- `Player.toggleActive()` method

### 7. Consistent Naming Convention
**Pick ONE pattern:**
- Either `player.i` OR `player.index` (not both)
- Either `playerIndex` OR `currentPlayer` (not both)

---

## GAME LOGIC IMPLEMENTATION (Next Phase)

### 8. Input System
**Create abstract input interface:**
```python
class InputInterface(ABC):
    @abstractmethod
    def choose_card(self, cards: list[Card]) -> int:
    @abstractmethod
    def choose_action(self, options: list[str]) -> int:
```

### 9. Turn System
**Implement actual turn logic:**
- Player chooses card from hand
- Choose action: Capture OR Trail
- Execute action
- Next player

### 10. Casino Game Rules
**Core mechanics to implement:**
- **Capture:** Match rank or sum to played card value
- **Trail:** Place card on table when no captures possible
- **Scoring:** Count cards, spades, big/little casino
- **End conditions:** All cards played, final capture

---

## TESTING STRATEGY

### 11. Unit Tests for Core Logic
```python
def test_player_creation()
def test_deck_dealing()
def test_turn_rotation()
def test_capture_logic()
```

### 12. Integration Tests
```python
def test_full_round()
def test_game_completion()
```

---

## TOMORROW'S FOCUS AREAS

**Morning (2-3 hours):**
1. Fix dual state tracking (#1)
2. Add constants (#3)
3. Clean up type hints (#2)

**Afternoon (2-3 hours):**
4. Extract display logic (#5)
5. Remove dead code (#6)
6. Start input system (#8)

**Evening (1-2 hours):**
7. Basic turn implementation (#9)
8. Simple capture logic (matching ranks only)

---

## CURRENT TECHNICAL DEBT

### High Impact:
- Dual state tracking (sync bugs waiting to happen)
- Inconsistent deck interface
- Missing constants

### Medium Impact:
- Mixed concerns (display in game logic)
- Dead code
- Naming inconsistencies

### Low Impact:
- File naming could be clearer
- Some methods could be static

---

## SUCCESS METRICS

**By end of tomorrow:**
- [ ] Architecture grade: B+ or better
- [ ] Player can choose cards via CLI
- [ ] Basic capture logic works (exact rank matches)
- [ ] Turn rotation functional
- [ ] No crashes during normal gameplay

**Stretch goals:**
- [ ] Trail action implemented
- [ ] Simple scoring system
- [ ] Game completion detection

---

## NOTES FOR FUTURE

- GUI abstraction ready when input interface complete
- Consider adding game state persistence later
- Multiplayer over network could use same core logic
- AI opponent implementation after human gameplay solid

---

*Last updated: Today's session*
*Next review: After tomorrow's work session*
